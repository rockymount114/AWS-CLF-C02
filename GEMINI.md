# GEMINI.md - AWS Cloud Practitioner Quiz Platform

> Use this file as your master prompt / context for Gemini to build the full Flask app. Drop this file in project root.

## 1. Project Overview
Build a Flask web application that lets users practice AWS Cloud Practitioner exam questions (65+ QAs from markdown). Admin can manage users, add/edit/delete questions and answers, view analytics. Deployable via Docker.

**Tech Stack:**
- Backend: Flask 3.x, Flask-SQLAlchemy, Flask-Login, Flask-Migrate, Flask-WTF
- DB: SQLite for dev, PostgreSQL for prod (config switch)
- Frontend: Jinja2 + Bootstrap 5 + HTMX (optional) or vanilla JS
- Auth: Flask-Login + Werkzeug password hashing + role-based (admin / user)
- Docker: Python 3.11-slim, gunicorn

## 2. Core Features

### For Regular Users:
- Register / Login / Logout
- Dashboard: Total questions, practiced, correct %, weak domains
- Practice Modes:
  - Random Quiz (10, 20, 30, All)
  - By Domain (Cloud Concepts, Security, Technology, Billing)
  - By Mode: Exam Simulation (65 random, timed 90 min) vs Learning Mode (show answer + explanation immediately)
  - Incorrect Only - retry wrong answers
- Question View:
  - Show question text
  - Options as radio (single) or checkbox (multi-select)
  - Submit -> Show Correct / Your answer / Explanation Why Correct + Why Wrong
  - Bookmark question
- Progress tracking: attempts table, score history, domain-wise performance chart (Chart.js)
- Profile page

### For Admin (role=admin):
- Admin Dashboard at /admin
- User Management:
  - List users, search, disable/enable, delete, promote to admin, reset password
  - View user stats: attempts, avg score
- Question Management:
  - CRUD for questions: add/edit/delete
  - Fields: question_text (TEXT), domain (SELECT), difficulty, question_type (single/multi), options (JSON or separate table), correct_answers (JSON list), explanation_correct (TEXT), explanation_wrong (TEXT), reference_url
  - Bulk import: Upload markdown file (like aws_65_FULL_CORRECT_QA.md) or CSV or JSON - parser to auto-extract
  - Bulk export to JSON/CSV
- Settings: Number of questions per quiz, exam time limit

## 3. Data Models (SQLAlchemy)

```python
User(id, username unique, email unique, password_hash, role enum['user','admin'], is_active bool, created_at)
Question(id, question_text TEXT, domain VARCHAR, difficulty enum['easy','medium','hard'], q_type enum['single','multi'], explanation_correct TEXT, explanation_wrong TEXT, reference_url VARCHAR, created_by FK, created_at, is_active bool)
Option(id, question_id FK, option_text TEXT, is_correct bool, label VARCHAR e.g. 'A')
Attempt(id, user_id FK, score INT, total INT, mode VARCHAR, domain_filter VARCHAR, started_at, finished_at, time_taken)
AttemptAnswer(id, attempt_id FK, question_id FK, selected_option_ids JSON, is_correct bool, time_taken)
Bookmark(id, user_id FK, question_id FK, created_at)
```

If you want simpler: Store options as JSON in Question.options_json = [{"label":"A","text":"...","is_correct":true}] - acceptable for MVP.

## 4. Project Structure

```
aws-quiz-app/
├── app/
│   ├── __init__.py (create_app, db init, login_manager)
│   ├── models.py
│   ├── forms.py (WTForms: Login, Register, QuestionForm)
│   ├── routes/
│   │   ├── auth.py
│   │   ├── main.py (dashboard, practice)
│   │   ├── quiz.py (start quiz, submit, result)
│   │   └── admin.py (admin routes, @admin_required)
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/login.html, register.html
│   │   ├── dashboard.html
│   │   ├── quiz/question.html, quiz/result.html, quiz/history.html
│   │   └── admin/users.html, admin/questions.html, admin/question_form.html, admin/import.html
│   ├── static/css/style.css, js/main.js
│   └── utils/parser.py (parse markdown file to extract QAs)
├── migrations/
├── seed/
│   └── aws_65_FULL_CORRECT_QA.md (initial seed file)
│   └── seed.py (script to import markdown into DB)
├── config.py (Dev, Prod, Testing configs from env)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .dockerignore
├── run.py
└── GEMINI.md (this file)
```

## 5. Key Routes to Implement

- `/` -> redirect to dashboard if auth else login
- `/auth/register`, `/auth/login`, `/auth/logout`
- `/dashboard` -> user stats
- `/quiz/start` POST params: mode, count, domain -> creates Attempt, redirects to /quiz/<attempt_id>/question/1
- `/quiz/<attempt_id>/question/<q_num>` GET/POST
- `/quiz/<attempt_id>/result`
- `/api/questions/random?count=10&domain=Technology`
- `/admin` -> admin dashboard
- `/admin/users` -> list + actions
- `/admin/questions` -> CRUD list
- `/admin/questions/new`, `/admin/questions/<id>/edit`, `/admin/questions/<id>/delete`
- `/admin/import` -> upload markdown -> parse -> preview -> confirm import
- `/admin/export` -> download JSON

## 6. Security Requirements
- Use Flask-Login @login_required, custom @admin_required decorator
- CSRF protection via Flask-WTF
- Password hashing: generate_password_hash, check_password_hash
- No SQL injection: use SQLAlchemy ORM
- Validate option belongs to question on submit
- Admin routes protected

## 7. Parser Logic for aws_65_FULL_CORRECT_QA.md

Create `app/utils/parser.py`:

```python
def parse_markdown_qa(file_path):
    # Regex to extract:
    # ### <num>. <title>
    # **Question:** ...
    # - option...
    # **Correct Answer:** ...
    # **Why Correct:** ...
    # **Why Wrong:** ...
    # Return list of dicts
```

Handle both single and multi-select: if Correct Answer contains "Select Two" or contains "+" or list, parse as multi.

For seeding:
```python
from app import create_app, db
from app.models import Question, Option
from app.utils.parser import parse_markdown_qa
# Loop and create Question + Options
```

## 8. UI/UX Guidelines
- Bootstrap 5 clean, mobile responsive
- Question card with domain badge, bookmark icon
- Options as large clickable cards with A, B, C, D
- After submit: highlight correct in green, wrong selected in red, show explanation boxes
- Progress bar top
- Use Chart.js for domain performance on dashboard
- No heavy JS, server-rendered Jinja

## 9. Dockerization

### Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x entrypoint.sh
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
```

### docker-compose.yml
```yaml
version: '3.8'
services:
  web:
    build: .
    ports: ["5000:5000"]
    env_file: .env
    volumes: [".:/app"]
    depends_on: [db]
    command: bash -c "flask db upgrade && python seed/seed.py && gunicorn --bind 0.0.0.0:5000 run:app"
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: aws_quiz
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes: [pgdata:/var/lib/postgresql/data]
    ports: ["5432:5432"]
volumes:
  pgdata:
```

### requirements.txt
```
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-Migrate==4.0.5
Flask-WTF==1.2.1
python-dotenv==1.0.1
gunicorn==22.0.0
psycopg2-binary==2.9.9
WTForms==3.1.2
email-validator==2.1.1
```

### .env.example
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=change-me-super-secret
DATABASE_URL=sqlite:///quiz.db
# For prod: postgresql://postgres:postgres@db:5432/aws_quiz
ADMIN_USERNAME=admin
ADMIN_PASSWORD=Admin@123
```

## 10. Admin Creation & Seed

On first run:
- Create admin user from env ADMIN_USERNAME / ADMIN_PASSWORD if not exists
- If Question table empty, auto-import from seed/aws_65_FULL_CORRECT_QA.md

## 11. Testing Checklist for Gemini
- [ ] User can register/login
- [ ] Non-admin cannot access /admin
- [ ] Start quiz -> answer -> see result with explanation
- [ ] Multi-select works (checkbox, partial credit? simple: must select all correct)
- [ ] Admin can add question with 4 options, mark correct
- [ ] Import markdown works (test with provided file)
- [ ] Docker builds and runs on 5000
- [ ] Data persists in postgres volume

## 12. Deployment
- For local: `docker-compose up --build`
- For prod: push image to Docker Hub / GHCR, deploy to Render / Railway / AWS ECS / Fly.io
- Set env vars in prod: SECRET_KEY, DATABASE_URL (managed postgres)
- Run migrations: `flask db upgrade`

## 13. Future Enhancements (Optional)
- Leaderboard
- Timer for exam simulation
- AI-generated explanation using Gemini API
- Spaced repetition for wrong answers

## 14. Instructions for Gemini CLI
When you (Gemini) read this file:
1. Generate the entire Flask project structure as above
2. Implement models.py, forms.py, routes
3. Create base.html with Bootstrap 5 CDN
4. Implement parser.py to handle the provided markdown format (### number, **Question:**, - options, **Correct Answer:**)
5. Create seed.py that imports the 65+ QAs
6. Make sure admin can manage everything
7. Provide Dockerfile + docker-compose.yml that works out-of-the-box
8. Output clear README with `docker-compose up` instructions

DO NOT skip admin features. DO NOT use overly complex frontend frameworks.

---
END OF GEMINI.md
