import os
import sys
import glob
import json
import re

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Question, Option

VALID_DOMAINS = [
    'Cloud Concepts',
    'Security & Compliance',
    'Cloud Technology & Service',
    'Billing, Pricing & Support'
]

def clean_text(text):
    if not text:
        return ''
    text = re.sub(r'<br\s*/?>', ' ', text, flags=re.I)
    text = re.sub(r'</?[a-zA-Z0-9]+[^>]*>', '', text)
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_key(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def import_all_enriched():
    app = create_app()
    with app.app_context():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        enriched_dir = os.path.join(base_dir, 'enriched')
        enriched_files = sorted(
            glob.glob(os.path.join(enriched_dir, 'exam_*.json')),
            key=lambda x: int(re.search(r'\d+', os.path.basename(x)).group())
        )
        
        if not enriched_files:
            print(f"No enriched files found in {enriched_dir}")
            return False
            
        print(f"Found {len(enriched_files)} enriched exam files in {enriched_dir}.")
        
        # Load existing questions from DB to avoid duplicate insertion
        existing_questions = Question.query.all()
        existing_map = {normalize_key(q.question_text): q for q in existing_questions}
        print(f"Current DB has {len(existing_questions)} existing questions.")
        
        added_count = 0
        updated_count = 0
        skipped_count = 0
        domain_counts = {d: 0 for d in VALID_DOMAINS}
        
        for fpath in enriched_files:
            with open(fpath, 'r', encoding='utf-8') as fp:
                try:
                    q_list = json.load(fp)
                except Exception as e:
                    print(f"Error parsing {fpath}: {e}")
                    continue
                    
            print(f"Processing {os.path.basename(fpath)}: {len(q_list)} questions...")
            for q_data in q_list:
                q_text = clean_text(q_data.get('question_text', ''))
                if not q_text:
                    continue
                    
                key = normalize_key(q_text)
                domain = q_data.get('domain', 'Cloud Technology & Service').strip()
                if domain not in VALID_DOMAINS:
                    # Normalize if slight variation
                    d_lower = domain.lower()
                    if 'concept' in d_lower:
                        domain = 'Cloud Concepts'
                    elif 'security' in d_lower or 'compliance' in d_lower:
                        domain = 'Security & Compliance'
                    elif 'billing' in d_lower or 'pricing' in d_lower or 'support' in d_lower:
                        domain = 'Billing, Pricing & Support'
                    else:
                        domain = 'Cloud Technology & Service'
                
                domain_counts[domain] = domain_counts.get(domain, 0) + 1
                difficulty = q_data.get('difficulty', 'medium').lower()
                if difficulty not in ['easy', 'medium', 'hard']:
                    difficulty = 'medium'
                    
                q_type = q_data.get('q_type', 'single').lower()
                explanation_correct = clean_text(q_data.get('explanation_correct', ''))
                explanation_wrong = clean_text(q_data.get('explanation_wrong', ''))
                reference_url = q_data.get('reference_url', '').strip()
                
                raw_options = q_data.get('options', [])
                if not raw_options:
                    continue
                
                # Check if question already in DB
                if key in existing_map:
                    db_q = existing_map[key]
                    # Update explanation if existing was empty or shorter
                    if explanation_correct and (not db_q.explanation_correct or len(explanation_correct) > len(db_q.explanation_correct)):
                        db_q.explanation_correct = explanation_correct[:4000]
                        if explanation_wrong:
                            db_q.explanation_wrong = explanation_wrong[:4000]
                        if reference_url and not db_q.reference_url:
                            db_q.reference_url = reference_url[:500]
                        updated_count += 1
                    else:
                        skipped_count += 1
                    continue
                
                # Determine correct letters
                correct_letters = q_data.get('correct_letters', [])
                
                # Create new Question
                new_q = Question(
                    question_text=q_text[:3000],
                    domain=domain,
                    difficulty=difficulty,
                    q_type=q_type,
                    explanation_correct=explanation_correct[:4000],
                    explanation_wrong=explanation_wrong[:4000],
                    reference_url=reference_url[:500] if reference_url else None,
                    is_active=True
                )
                db.session.add(new_q)
                db.session.flush()
                
                # Add options
                labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                has_correct = False
                for idx, opt_info in enumerate(raw_options):
                    opt_label = opt_info.get('label') or (labels[idx] if idx < len(labels) else str(idx+1))
                    opt_text = clean_text(opt_info.get('text', ''))
                    if not opt_text:
                        continue
                    
                    is_corr = opt_info.get('is_correct', False)
                    if opt_label in correct_letters or (not is_corr and opt_label.upper() in [c.upper() for c in correct_letters]):
                        is_corr = True
                        
                    if is_corr:
                        has_correct = True
                        
                    db.session.add(Option(
                        question_id=new_q.id,
                        option_text=opt_text[:1000],
                        label=opt_label,
                        is_correct=is_corr
                    ))
                
                if not has_correct and new_q.options:
                    new_q.options[0].is_correct = True
                
                existing_map[key] = new_q
                added_count += 1
                
        db.session.commit()
        
        total_now = Question.query.count()
        total_opts = Option.query.count()
        print("\n=== IMPORT SUMMARY ===")
        print(f"New questions added: {added_count}")
        print(f"Existing questions updated: {updated_count}")
        print(f"Duplicates skipped: {skipped_count}")
        print(f"Total questions in database: {total_now}")
        print(f"Total options in database: {total_opts}")
        print("\n=== DOMAIN BREAKDOWN IN DB ===")
        from collections import Counter
        all_d = Counter(q.domain for q in Question.query.all())
        for d, c in sorted(all_d.items()):
            print(f"  {d}: {c} questions ({c/total_now*100:.1f}%)")
            
        return True

if __name__ == '__main__':
    import_all_enriched()
