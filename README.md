# django-project-template

A project template for Django 2.0 based on the django-two-scoops project template.

## Usage

```
npm install
python3 -m venv .env
source .env/bin/activate
pip install -r requirements/local.txt
python radius_2fa/manage.py migrate
python radius_2fa/manage.py collectstatic
python radius_2fa/manage.py runserver
```
