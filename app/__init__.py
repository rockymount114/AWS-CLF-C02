from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config_by_name
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV','dev')
    app.config.from_object(config_by_name.get(env, config_by_name['dev']))
    from dotenv import load_dotenv
    load_dotenv()
    # override with env DATABASE_URL
    if os.getenv('DATABASE_URL'):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    if os.getenv('SECRET_KEY'):
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.utils.tz import format_ny_date
    app.jinja_env.filters['ny_date'] = format_ny_date

    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        try:
            return db.session.get(User, int(user_id))
        except Exception:
            return None

    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.quiz import quiz_bp
    from app.routes.admin import admin_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()
        # create admin if not exists
        from app.models import User
        from werkzeug.security import generate_password_hash
        admin_user = os.getenv('ADMIN_USERNAME','admin')
        admin_pass = os.getenv('ADMIN_PASSWORD','Admin@123')
        if not User.query.filter_by(username=admin_user).first():
            u = User(username=admin_user, email='admin@example.com', role='admin', password_hash=generate_password_hash(admin_pass))
            db.session.add(u)
            db.session.commit()
    return app
