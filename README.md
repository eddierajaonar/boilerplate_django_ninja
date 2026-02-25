# Django Ninja Boilerplate

## Installation

git clone ...
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Routes

POST /api/register
POST /api/login
POST /api/refresh
GET /api/products
POST /api/products
PUT /api/products/{id}
DELETE /api/products/{id}

## USING DOCKER
docker compose up --build

http://localhost:8000/api/docs (for Ninja docs )

### create superuser
docker exec -it django_backend python manage.py createsuperuser
