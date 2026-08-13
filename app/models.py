from app import db
from flask_login import UserMixin
from datetime import datetime

import json

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='user')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def is_admin(self):
        return self.role == 'admin'

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    domain = db.Column(db.String(100))
    difficulty = db.Column(db.String(20), default='medium')
    q_type = db.Column(db.String(20), default='single') # single/multi
    explanation_correct = db.Column(db.Text)
    explanation_wrong = db.Column(db.Text)
    reference_url = db.Column(db.String(500))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    options = db.relationship('Option', backref='question', cascade='all, delete-orphan', lazy=True, order_by='Option.id')

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    option_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    label = db.Column(db.String(5))

class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer, default=0)
    total = db.Column(db.Integer)
    mode = db.Column(db.String(50))
    domain_filter = db.Column(db.String(100))
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime)
    answers = db.relationship('AttemptAnswer', backref='attempt', lazy=True, order_by='AttemptAnswer.id')

    @property
    def score_percent(self):
        if not self.total or self.total == 0:
            return 0
        return round((self.score / self.total) * 100)

    @property
    def is_passed(self):
        return self.score_percent >= 70

    @property
    def wrong_count(self):
        if not self.answers:
            return 0
        return sum(1 for a in self.answers if not a.is_correct)


class AttemptAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('attempt.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    selected_option_ids = db.Column(db.Text) # JSON list
    is_correct = db.Column(db.Boolean)
    question = db.relationship('Question')

    def get_selected_ids(self):
        if not self.selected_option_ids:
            return []
        try:
            val = json.loads(self.selected_option_ids)
            if isinstance(val, list):
                return [str(x) for x in val]
            return [str(val)]
        except Exception:
            return []

    def is_selected(self, option_id):
        return str(option_id) in self.get_selected_ids()

