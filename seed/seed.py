import os
import sys
import glob
import json
import re

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Question, Option, User
from app.utils.parser import parse_markdown_qa
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    force = '--force' in sys.argv or '-f' in sys.argv
    if Question.query.first() and not force:
        print("DB already has questions, skipping seed (run with --force to reseed)")
        sys.exit(0)

    if force:
        print("Force reseed enabled: clearing existing questions and options...")
        Option.query.delete()
        Question.query.delete()
        db.session.commit()

    # Ensure admin user exists
    admin_user = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_pass = os.environ.get('ADMIN_PASSWORD', 'Admin@123')
    if not User.query.filter_by(username=admin_user).first():
        u = User(
            username=admin_user,
            email=f"{admin_user}@example.com",
            password_hash=generate_password_hash(admin_pass),
            role='admin'
        )
        db.session.add(u)
        db.session.commit()
        print(f"Created default admin user: {admin_user}")

    # 1. Seed from aws_65_FULL_CORRECT_QA.md
    md_path = os.path.join(os.path.dirname(__file__), 'aws_65_FULL_CORRECT_QA.md')
    if os.path.exists(md_path):
        qs = parse_markdown_qa(md_path)
        print(f"Parsed {len(qs)} questions from {md_path}")

        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        for item in qs:
            q = Question(
                question_text=item['question_text'][:2000],
                domain=item.get('domain', 'Cloud Technology & Service'),
                difficulty=item.get('difficulty', 'medium'),
                q_type=item.get('q_type', 'single'),
                explanation_correct=item['explanation_correct'][:2000],
                explanation_wrong=item['explanation_wrong'][:2000]
            )
            db.session.add(q)
            db.session.flush()

            for idx, opt_text in enumerate(item['options_raw'][:6]):
                opt_clean = opt_text.strip()
                if not opt_clean or opt_clean in ['--', '-', '---'] or set(opt_clean) <= {'-', ' '}:
                    continue
                
                corr_lines = [cl.strip().lstrip('-*• ').strip().lower() for cl in item['correct_text'].split('\n') if cl.strip()]
                opt_low = opt_clean.lower()
                is_correct = any(
                    opt_low == cl or (len(opt_low) > 15 and opt_low in cl) or (len(cl) > 15 and cl in opt_low)
                    for cl in corr_lines
                ) if corr_lines else (opt_low in item['correct_text'].lower())
                
                label = labels[idx] if idx < len(labels) else str(idx + 1)
                opt = Option(question_id=q.id, option_text=opt_clean[:500], label=label, is_correct=is_correct)
                db.session.add(opt)

        db.session.commit()
        print(f"Seeded {len(qs)} initial questions from markdown.")

    # 2. Seed from all enriched practice exam JSON files
    enriched_dir = os.path.join(os.path.dirname(__file__), 'enriched')
    enriched_files = sorted(
        glob.glob(os.path.join(enriched_dir, 'exam_*.json')),
        key=lambda x: int(re.search(r'\d+', os.path.basename(x)).group())
    )
    if enriched_files:
        from seed.import_all_exams import import_all_enriched
        print(f"Found {len(enriched_files)} enriched files. Running full import...")
        import_all_enriched()
    else:
        print("No enriched files found in seed/enriched/ yet.")

    total_q = Question.query.count()
    print(f"Done! Database now contains {total_q} questions.")
