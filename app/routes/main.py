
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Question, Attempt

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

