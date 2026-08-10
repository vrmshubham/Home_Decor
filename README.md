# Home Decor Store

Monorepo for an Indian home-furnishing catalogue and commerce platform serving Bhavnagar and online customers across India.

## Stack

- React, TypeScript and Vite
- Django REST Framework
- PostgreSQL
- Docker Compose for local infrastructure

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/development.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API runs at `http://localhost:8000/api/` and Django Admin at `http://localhost:8000/admin/`.

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

The storefront runs at `http://localhost:5173/`.

## First milestone

- Product category and product models
- Variant-level pricing and stock
- Django Admin catalogue management
- Public catalogue API
- Responsive storefront homepage

Brand name, address and WhatsApp details currently use placeholders.
