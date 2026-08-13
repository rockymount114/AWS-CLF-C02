
from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Question, Option, Attempt, Bookmark
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def dashboard():
    total_q = Question.query.filter_by(is_active=True).count()
    attempts = Attempt.query.filter_by(user_id=current_user.id).order_by(Attempt.started_at.desc()).all()
    total_attempts = len(attempts)
    
    avg_score = round(sum(a.score_percent for a in attempts) / total_attempts) if total_attempts > 0 else 0
    total_practiced = sum(a.total or 0 for a in attempts)
    
    return render_template('dashboard.html', 
                           total_q=total_q, 
                           attempts=attempts, 
                           total_attempts=total_attempts,
                           avg_score=avg_score,
                           total_practiced=total_practiced)

@main_bp.route('/dashboard')
@login_required
def dashboard2():
    return dashboard()


@main_bp.route('/study')
@login_required
def study_cards():
    domain_filter = request.args.get('domain', 'All').strip()
    standard_domains = ['Cloud Concepts', 'Security & Compliance', 'Cloud Technology & Service', 'Billing, Pricing & Support']
    
    query = Question.query.filter_by(is_active=True)
    if domain_filter and domain_filter != 'All':
        query = query.filter_by(domain=domain_filter)
        
    questions = query.order_by(Question.id.asc()).all()
    user_bookmarks = set(b.question_id for b in Bookmark.query.filter_by(user_id=current_user.id).all())
    
    return render_template('study/cards.html',
                           questions=questions,
                           total_questions=len(questions),
                           domains=standard_domains,
                           selected_domain=domain_filter,
                           user_bookmarks=user_bookmarks)


@main_bp.route('/api/study/questions')
@login_required
def api_study_questions():
    domain_filter = request.args.get('domain', 'All').strip()
    difficulty = request.args.get('difficulty', 'All').strip()
    bookmarked_only = request.args.get('bookmarked', 'false').lower() == 'true'
    
    query = Question.query.filter_by(is_active=True)
    if domain_filter and domain_filter != 'All':
        query = query.filter_by(domain=domain_filter)
    if difficulty and difficulty != 'All':
        query = query.filter_by(difficulty=difficulty)
        
    questions = query.order_by(Question.id.asc()).all()
    user_bookmarks = set(b.question_id for b in Bookmark.query.filter_by(user_id=current_user.id).all())
    
    if bookmarked_only:
        questions = [q for q in questions if q.id in user_bookmarks]
        
    data = []
    for q in questions:
        data.append({
            'id': q.id,
            'question_text': q.question_text,
            'domain': q.domain or 'Cloud Technology & Service',
            'difficulty': q.difficulty or 'medium',
            'q_type': q.q_type or 'single',
            'is_bookmarked': q.id in user_bookmarks,
            'explanation_correct': q.explanation_correct or '',
            'explanation_wrong': q.explanation_wrong or '',
            'reference_url': q.reference_url or '',
            'options': [
                {
                    'id': o.id,
                    'label': o.label,
                    'text': o.option_text,
                    'is_correct': o.is_correct
                }
                for o in q.options
            ]
        })
        
    return jsonify({
        'count': len(data),
        'questions': data
    })


@main_bp.route('/study/bookmark/<int:qid>', methods=['POST'])
@login_required
def toggle_bookmark(qid):
    bm = Bookmark.query.filter_by(user_id=current_user.id, question_id=qid).first()
    if bm:
        db.session.delete(bm)
        db.session.commit()
        return jsonify({'status': 'unbookmarked', 'is_bookmarked': False})
    else:
        new_bm = Bookmark(user_id=current_user.id, question_id=qid)
        db.session.add(new_bm)
        db.session.commit()
        return jsonify({'status': 'bookmarked', 'is_bookmarked': True})


