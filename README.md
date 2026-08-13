
# AWS Quiz App - Flask

See GEMINI.md for full blueprint.

## Quick Start with Docker (Recommended)

1. cp .env.example .env
2. docker-compose up --build
3. Open http://localhost:5000
   - Login with admin / Admin@123 (from .env)
   - Dashboard -> Start Quiz

## Local Dev without Docker

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db init
flask db migrate -m "init"
flask db upgrade
python seed/seed.py
flask run
```

## Features Implemented
- Auth (register/login)
- Role admin/user
- Dashboard, Start Quiz random/exam
- Question with single/multi
- Result page
- Admin: Users toggle/delete, Questions CRUD, Import markdown
- Docker + postgres
