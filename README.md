# CheapEats

CheapEats is a small Flask + SQLite course project for a database systems class.
The goal is to keep the implementation simple and explainable, using direct SQL
queries instead of an ORM.

## Setup

Create and activate a virtual environment, then install Flask:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Recreate the Database

Run:

```powershell
python init_db.py
```

This creates `cheap_eats.db` from `schema.sql` and loads sample data from
`seed.sql`.

## Run the App

Run:

```powershell
python app.py
```

Then open the local Flask URL shown in the terminal.

## SQL Usage

The project should use direct SQLite queries with `?` placeholders. The schema
includes the required tables: `students`, `restaurants`, `meals`, `orders`, and
`order_items`. It also includes a `cheap_meals` view for browsing low-cost
meals.

## Regex Usage

Before placing an order, the app should use Python regular expressions to
validate KU student emails ending in `@student.ku.dk` or `@alumni.ku.dk`.

## AI Declaration

See `AI_DECLARATION.md` for the required course declaration about AI assistance.
