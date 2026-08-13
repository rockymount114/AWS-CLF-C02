
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Question, Option, Attempt, AttemptAnswer
from app import db
import random, json
from datetime import datetime

quiz_bp = Blueprint('quiz', __name__, url_prefix='/quiz')

@quiz_bp.route('/start', methods=['POST'])
@login_required
def start():
    mode = request.form.get('mode', 'random')
    count = int(request.form.get('count', 10))
    domain = request.form.get('domain')
    q_query = Question.query.filter_by(is_active=True)
    if domain and domain != 'All':
        q_query = q_query.filter(Question.domain.contains(domain))
    all_q = q_query.all()
    selected = random.sample(all_q, min(count, len(all_q))) if all_q else []
    attempt = Attempt(user_id=current_user.id, total=len(selected), mode=mode, domain_filter=domain)
    db.session.add(attempt)
    db.session.commit()
    
    for q in selected:
        aa = AttemptAnswer(attempt_id=attempt.id, question_id=q.id, selected_option_ids='[]', is_correct=False)
        db.session.add(aa)
    db.session.commit()
    return redirect(url_for('quiz.show_question', attempt_id=attempt.id, q_num=1))

@quiz_bp.route('/<int:attempt_id>/question/<int:q_num>', methods=['GET', 'POST'])
@login_required
def show_question(attempt_id, q_num):
    attempt = Attempt.query.get_or_404(attempt_id)
    if attempt.user_id != current_user.id and not current_user.is_admin():
        flash('Unauthorized access to quiz attempt.', 'danger')
        return redirect(url_for('main.dashboard'))
        
    answers = AttemptAnswer.query.filter_by(attempt_id=attempt_id).order_by(AttemptAnswer.id).all()
    if not answers or q_num < 1 or q_num > len(answers):
        return redirect(url_for('quiz.result', attempt_id=attempt_id))
        
    aa = answers[q_num - 1]
    question = Question.query.get_or_404(aa.question_id)
    
    from_result = request.args.get('from_result') == '1'
    is_review = attempt.finished_at is not None or from_result or request.args.get('review') == '1'
    
    if request.method == 'POST':
        selected = request.form.getlist('option')
        aa.selected_option_ids = json.dumps(selected)
        correct_ids = [str(o.id) for o in question.options if o.is_correct]
        aa.is_correct = (set(selected) == set(correct_ids))
        db.session.commit()
        
        if attempt.mode == 'learning':
            selected_ids = [str(x) for x in aa.get_selected_ids()]
            return render_template('quiz/question.html',
                                   question=question,
                                   attempt=attempt,
                                   aa=aa,
                                   q_num=q_num,
                                   total=len(answers),
                                   selected_ids=selected_ids,
                                   is_review=True,
                                   just_submitted=True,
                                   from_result=from_result,
                                   prev_q=q_num - 1 if q_num > 1 else None,
                                   next_q=q_num + 1 if q_num < len(answers) else None)
        
        if q_num < len(answers):
            return redirect(url_for('quiz.show_question', attempt_id=attempt_id, q_num=q_num+1))
        else:
            attempt.finished_at = datetime.utcnow()
            attempt.score = sum(1 for a in answers if a.is_correct)
            db.session.commit()
            return redirect(url_for('quiz.result', attempt_id=attempt_id))
            
    selected_ids = [str(x) for x in aa.get_selected_ids()]
    return render_template('quiz/question.html',
                           question=question,
                           attempt=attempt,
                           aa=aa,
                           q_num=q_num,
                           total=len(answers),
                           selected_ids=selected_ids,
                           is_review=is_review,
                           from_result=from_result,
                           prev_q=q_num - 1 if q_num > 1 else None,
                           next_q=q_num + 1 if q_num < len(answers) else None)

@quiz_bp.route('/<int:attempt_id>/result')
@login_required
def result(attempt_id):
    attempt = Attempt.query.get_or_404(attempt_id)
    if attempt.user_id != current_user.id and not current_user.is_admin():
        flash('Unauthorized access to quiz result.', 'danger')
        return redirect(url_for('main.dashboard'))
        
    answers = AttemptAnswer.query.filter_by(attempt_id=attempt_id).order_by(AttemptAnswer.id).all()
    if not attempt.finished_at:
        attempt.finished_at = datetime.utcnow()
        attempt.score = sum(1 for a in answers if a.is_correct)
        db.session.commit()
        
    wrong_count = sum(1 for a in answers if not a.is_correct)
    total_q = len(answers)
    score_percent = round((attempt.score / total_q * 100)) if total_q > 0 else 0
    scaled_score = 100 + round((attempt.score / total_q * 900)) if total_q > 0 else 100
    
    # Calculate time taken string
    time_taken_str = "Under 1m"
    if attempt.started_at and attempt.finished_at:
        seconds = int((attempt.finished_at - attempt.started_at).total_seconds())
        if seconds >= 60:
            time_taken_str = f"{round(seconds / 60)}m"
        else:
            time_taken_str = f"{seconds}s"

    # Domain breakdown stats
    domain_stats = {}
    for aa in answers:
        d = aa.question.domain if (aa.question and aa.question.domain) else 'General'
        if d not in domain_stats:
            domain_stats[d] = {'correct': 0, 'total': 0}
        domain_stats[d]['total'] += 1
        if aa.is_correct:
            domain_stats[d]['correct'] += 1

    for d, s in domain_stats.items():
        s['percent'] = round((s['correct'] / s['total']) * 100) if s['total'] > 0 else 0

    return render_template('quiz/result.html',
                           attempt=attempt,
                           answers=answers,
                           wrong_count=wrong_count,
                           score_percent=score_percent,
                           scaled_score=scaled_score,
                           time_taken_str=time_taken_str,
                           domain_stats=domain_stats)


@quiz_bp.route('/history')
@login_required
def history():
    attempts = Attempt.query.filter_by(user_id=current_user.id).order_by(Attempt.started_at.desc()).all()
    return render_template('quiz/history.html', attempts=attempts)


