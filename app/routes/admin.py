
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from flask_login import login_required, current_user
from functools import wraps
from app.models import User, Question, Option
from app import db
import json
from datetime import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not current_user.is_authenticated or not current_user.is_admin():
            flash('Admin access required'); return redirect(url_for('main.dashboard'))
        return f(*args,**kwargs)
    return decorated

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    users=User.query.count()
    questions=Question.query.count()
    return render_template('admin/dashboard.html', users=users, questions=questions)

@admin_bp.route('/users')
@login_required
@admin_required
def users():
    all_users=User.query.all()
    return render_template('admin/users.html', users=all_users)

@admin_bp.route('/users/<int:user_id>/toggle')
@login_required
@admin_required
def toggle_user(user_id):
    u=User.query.get_or_404(user_id)
    u.is_active=not u.is_active
    db.session.commit()
    return redirect(url_for('admin.users'))

@admin_bp.route('/users/<int:user_id>/delete')
@login_required
@admin_required
def delete_user(user_id):
    u=User.query.get_or_404(user_id)
    db.session.delete(u); db.session.commit()
    return redirect(url_for('admin.users'))

@admin_bp.route('/questions')
@login_required
@admin_required
def questions():
    search = request.args.get('search', '').strip()
    domain = request.args.get('domain', 'All').strip()
    q_type = request.args.get('q_type', 'All').strip()
    difficulty = request.args.get('difficulty', 'All').strip()
    
    query = Question.query
    
    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            (Question.question_text.ilike(search_pattern)) |
            (Question.domain.ilike(search_pattern)) |
            (Question.explanation_correct.ilike(search_pattern))
        )
    if domain and domain != 'All':
        query = query.filter(Question.domain == domain)
    if q_type and q_type != 'All':
        query = query.filter_by(q_type=q_type)
    if difficulty and difficulty != 'All':
        query = query.filter_by(difficulty=difficulty)
        
    qs = query.order_by(Question.id.desc()).all()
    
    db_domains = [d[0] for d in db.session.query(Question.domain).distinct().all() if d[0]]
    standard_domains = ['Cloud Concepts', 'Security & Compliance', 'Cloud Technology & Service', 'Billing, Pricing & Support']
    all_domains = sorted(list(set(db_domains + standard_domains)))

    return render_template('admin/questions.html',
                           questions=qs,
                           search=search,
                           domain=domain,
                           q_type=q_type,
                           difficulty=difficulty,
                           domains=all_domains)


@admin_bp.route('/questions/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_question():
    if request.method == 'POST':
        q_text = request.form.get('question_text', '').strip()
        domain = request.form.get('domain', '').strip()
        difficulty = request.form.get('difficulty', 'medium')
        q_type = request.form.get('q_type', 'single')
        exp_c = request.form.get('explanation_correct', '').strip()
        exp_w = request.form.get('explanation_wrong', '').strip()
        ref_url = request.form.get('reference_url', '').strip()
        
        q = Question(
            question_text=q_text,
            domain=domain,
            difficulty=difficulty,
            q_type=q_type,
            explanation_correct=exp_c,
            explanation_wrong=exp_w,
            reference_url=ref_url,
            created_by=current_user.id
        )
        db.session.add(q)
        db.session.flush()
        
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        opt_idx = 0
        for i in range(1, 9):
            opt_text = request.form.get(f'option_{i}', '').strip()
            is_corr = request.form.get(f'is_correct_{i}') == 'on'
            if opt_text:
                label = labels[opt_idx] if opt_idx < len(labels) else str(opt_idx + 1)
                opt = Option(question_id=q.id, option_text=opt_text, is_correct=is_corr, label=label)
                db.session.add(opt)
                opt_idx += 1
                
        db.session.commit()
        flash('New question created successfully!', 'success')
        return redirect(url_for('admin.questions'))
        
    return render_template('admin/question_form.html', question=None, existing_opts={})

@admin_bp.route('/questions/<int:qid>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_question(qid):
    q = Question.query.get_or_404(qid)
    if request.method == 'POST':
        q.question_text = request.form.get('question_text', '').strip()
        q.domain = request.form.get('domain', '').strip()
        q.difficulty = request.form.get('difficulty', 'medium')
        q.q_type = request.form.get('q_type', 'single')
        q.explanation_correct = request.form.get('explanation_correct', '').strip()
        q.explanation_wrong = request.form.get('explanation_wrong', '').strip()
        q.reference_url = request.form.get('reference_url', '').strip()
        
        Option.query.filter_by(question_id=q.id).delete()
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        opt_idx = 0
        for i in range(1, 9):
            opt_text = request.form.get(f'option_{i}', '').strip()
            is_corr = request.form.get(f'is_correct_{i}') == 'on'
            if opt_text:
                label = labels[opt_idx] if opt_idx < len(labels) else str(opt_idx + 1)
                opt = Option(question_id=q.id, option_text=opt_text, is_correct=is_corr, label=label)
                db.session.add(opt)
                opt_idx += 1
                
        db.session.commit()
        flash(f'Question #{q.id} updated successfully!', 'success')
        return redirect(url_for('admin.questions'))
        
    existing_opts = {idx+1: opt for idx, opt in enumerate(q.options)}
    return render_template('admin/question_form.html', question=q, existing_opts=existing_opts)


@admin_bp.route('/questions/<int:qid>/delete')
@login_required
@admin_required
def delete_question(qid):
    q = Question.query.get_or_404(qid)
    db.session.delete(q)
    db.session.commit()
    flash(f'Question #{qid} deleted successfully.', 'warning')
    return redirect(url_for('admin.questions'))

@admin_bp.route('/questions/deduplicate', methods=['POST'])
@login_required
@admin_required
def deduplicate_questions():
    from sqlalchemy import func
    from app.models import AttemptAnswer
    
    grouped = db.session.query(
        func.lower(func.trim(Question.question_text)), 
        func.count(Question.id)
    ).group_by(func.lower(func.trim(Question.question_text)))\
     .having(func.count(Question.id) > 1).all()

    removed_count = 0
    for norm_text, count in grouped:
        all_qs = Question.query.filter(
            func.lower(func.trim(Question.question_text)) == norm_text
        ).order_by(Question.id.asc()).all()
        
        keeper = all_qs[0]
        duplicates = all_qs[1:]
        
        for dup in duplicates:
            AttemptAnswer.query.filter_by(question_id=dup.id).update({'question_id': keeper.id})
            db.session.delete(dup)
            removed_count += 1

    db.session.commit()
    if removed_count > 0:
        flash(f'Successfully removed {removed_count} duplicate question(s)!', 'success')
    else:
        flash('No duplicate questions were found in the database.', 'info')
        
    return redirect(url_for('admin.questions'))



@admin_bp.route('/import', methods=['GET', 'POST'])
@login_required
@admin_required
def import_md():
    from app.utils.parser import parse_markdown_qa
    if request.method == 'POST':
        file = request.files.get('file')
        default_domain = request.form.get('default_domain', 'Cloud Technology & Service').strip()
        if file and file.filename:
            import os
            path = os.path.join('/tmp', 'upload.md')
            file.save(path)
            parsed = parse_markdown_qa(path)
            
            imported_count = 0
            for item in parsed:
                q_text = item['question_text'][:2000]
                q_domain = item.get('domain')
                if not q_domain or q_domain == 'Imported' or q_domain == 'General':
                    q_domain = default_domain
                    
                q_type = item.get('q_type')
                if not q_type:
                    correct_text = item['correct_text'].lower()
                    q_type = 'multi' if ('select' in q_text.lower() or 'select' in correct_text or '\n-' in item['correct_text']) else 'single'
                
                difficulty = item.get('difficulty', 'medium')
                
                q = Question(
                    question_text=q_text,
                    domain=q_domain,
                    difficulty=difficulty,
                    q_type=q_type,
                    explanation_correct=item['explanation_correct'][:2000],
                    explanation_wrong=item['explanation_wrong'][:2000],
                    created_by=current_user.id
                )
                db.session.add(q)
                db.session.flush()
                
                labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                for idx, opt_text in enumerate(item['options_raw'][:6]):
                    opt_clean = opt_text.strip()
                    if not opt_clean or opt_clean in ['--', '-', '---'] or set(opt_clean) <= {'-', ' '}:
                        continue
                    # Match against individual lines/bullet items in correct_text
                    corr_lines = [cl.strip().lstrip('-*• ').strip().lower() for cl in item['correct_text'].split('\n') if cl.strip()]
                    opt_low = opt_clean.lower()
                    is_correct = any(
                        opt_low == cl or (len(opt_low) > 15 and opt_low in cl) or (len(cl) > 15 and cl in opt_low)
                        for cl in corr_lines
                    ) if corr_lines else (opt_low in item['correct_text'].lower())
                    db.session.add(Option(
                        question_id=q.id,
                        option_text=opt_clean[:500],
                        is_correct=is_correct,
                        label=labels[idx] if idx < len(labels) else str(idx+1)
                    ))
                imported_count += 1
                
            db.session.commit()
            flash(f'Successfully imported {imported_count} question(s) from Markdown file!', 'success')
            return redirect(url_for('admin.questions'))
        else:
            flash('Please upload a valid .md file.', 'danger')
            
    standard_domains = ['Cloud Concepts', 'Security & Compliance', 'Cloud Technology & Service', 'Billing, Pricing & Support']
    return render_template('admin/import.html', domains=standard_domains)


@admin_bp.route('/import/template')
@login_required
@admin_required
def download_import_template():
    template_content = """# AWS Practice Questions Import Template

### 1. Hardware Security Module for Compliance
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Due to strict compliance mandates, an enterprise must use dedicated hardware security modules in the cloud for encryption key storage. Which AWS service fulfills this requirement?

**Options:**
- **[A]** AWS Key Management Service (AWS KMS)
- **[B]** AWS CloudHSM
- **[C]** AWS Secrets Manager
- **[D]** AWS Certificate Manager

**Correct Answer:**
- **[B] AWS CloudHSM**

**Why Correct:**
AWS CloudHSM provides dedicated, single-tenant FIPS 140-2 Level 3 hardware security modules directly in your VPC.

**Why Others Are Incorrect:**
- **AWS KMS:** Multi-tenant shared infrastructure managed by AWS.
- **AWS Secrets Manager:** Manages and rotates credentials/passwords.
- **AWS Certificate Manager:** Deploys SSL/TLS certificates.

---

### 2. Services with Default Encryption (Select Two)
**Domain:** `Security & Compliance` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which of the following AWS storage services have encryption at rest enabled automatically by default? (Select two)

**Options:**
- **[A]** Amazon Elastic Block Store (Amazon EBS)
- **[B]** AWS Storage Gateway
- **[C]** Amazon Elastic File System (Amazon EFS)
- **[D]** Amazon S3 Glacier

**Correct Answer:**
- **[B] AWS Storage Gateway**
- **[D] Amazon S3 Glacier**

**Why Correct:**
All data written to AWS Storage Gateway and Amazon S3 Glacier is automatically encrypted with AES-256 at rest.

**Why Others Are Incorrect:**
EBS and EFS offer encryption, but it must be enabled upon creation or via account-level defaults.
"""
    return Response(
        template_content,
        mimetype="text/markdown",
        headers={"Content-disposition": "attachment; filename=aws_questions_import_template.md"}
    )



@admin_bp.route('/export')
@admin_bp.route('/questions/export')
@login_required
@admin_required
def export_questions():
    search = request.args.get('search', '').strip()
    domain = request.args.get('domain', '').strip()
    q_type = request.args.get('q_type', '').strip()
    difficulty = request.args.get('difficulty', '').strip()
    export_scope = request.args.get('scope', 'all')

    query = Question.query
    if export_scope == 'filtered':
        if search:
            search_pattern = f"%{search}%"
            query = query.filter(
                (Question.question_text.ilike(search_pattern)) |
                (Question.domain.ilike(search_pattern)) |
                (Question.explanation_correct.ilike(search_pattern))
            )
        if domain and domain != 'All':
            query = query.filter(Question.domain == domain)
        if q_type and q_type != 'All':
            query = query.filter_by(q_type=q_type)
        if difficulty and difficulty != 'All':
            query = query.filter_by(difficulty=difficulty)

    questions = query.order_by(Question.id.asc()).all()

    export_data = []
    for q in questions:
        export_data.append({
            "id": q.id,
            "question_text": q.question_text,
            "domain": q.domain,
            "difficulty": q.difficulty,
            "q_type": q.q_type,
            "explanation_correct": q.explanation_correct,
            "explanation_wrong": q.explanation_wrong,
            "reference_url": q.reference_url,
            "is_active": q.is_active,
            "created_at": q.created_at.isoformat() if q.created_at else None,
            "options": [
                {
                    "id": opt.id,
                    "label": opt.label,
                    "option_text": opt.option_text,
                    "is_correct": opt.is_correct
                }
                for opt in q.options
            ]
        })

    json_str = json.dumps(export_data, indent=2, ensure_ascii=False)
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    filename = f"aws_questions_export_{timestamp}.json"

    return Response(
        json_str,
        mimetype='application/json',
        headers={
            'Content-Disposition': f'attachment; filename={filename}',
            'Content-Type': 'application/json; charset=utf-8'
        }
    )

