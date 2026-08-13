from app import create_app, db
from app.models import Question, Option
from app.utils.parser import parse_markdown_qa
import os, json

app = create_app()
with app.app_context():
    if Question.query.first():
        print("DB already has questions, skipping seed")
        exit(0)
    md_path = os.path.join(os.path.dirname(__file__), 'aws_65_FULL_CORRECT_QA.md')
    if not os.path.exists(md_path):
        print(f"Markdown not found at {md_path}")
        exit(1)
    qs = parse_markdown_qa(md_path)
    print(f"Parsed {len(qs)} questions")
    for item in qs:
        q = Question(
            question_text=item['question_text'][:2000],
            domain='General',
            q_type='multi' if 'Select' in item['question_text'] or 'TWO' in item['correct_text'] else 'single',
            explanation_correct=item['explanation_correct'][:2000],
            explanation_wrong=item['explanation_wrong'][:2000]
        )
        db.session.add(q)
        db.session.flush()
        # Create options
        labels = ['A','B','C','D','E']
        for idx, opt_text in enumerate(item['options_raw'][:5]):
            opt_clean = opt_text.strip()
            if not opt_clean or opt_clean in ['--', '-', '---'] or set(opt_clean) <= {'-', ' '}:
                continue
            is_correct = False
            if opt_clean[:30].lower() in item['correct_text'].lower() or item['correct_text'].lower() in opt_clean.lower():
                is_correct = True
            opt = Option(question_id=q.id, option_text=opt_clean[:500], label=labels[idx] if idx < len(labels) else str(idx), is_correct=is_correct)
            db.session.add(opt)

    db.session.commit()
    print("Seed done")
