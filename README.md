# Affordable Eats

Affordable Eats is a simple Flask + SQLite web-app for a database systems project.
It uses direct SQL queries and includes a regex validation for KU student emails.

## Mac setup

```bash
cd DIS-Project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py
python app.py
```

Open the URL shown in the terminal, normally:

```text
http://127.0.0.1:5000
```

## What the app contains

- restaurants page
- meals page with search/filter
- order form
- admin/order overview
- SQLite database initialized from `schema.sql` and `seed.sql`
- regex validation for KU emails

## Reset database

```bash
python init_db.py
```

## AI Declaration

See `AI_DECLARATION.md`.
