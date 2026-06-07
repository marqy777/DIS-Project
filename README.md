# Affordable Eats

Affordable Eats is a simple Flask + SQLite web-app for our database systems project. The app interacts with the SQLite database `affordable_eats.db`, which is created from `schema.sql` and filled with sample data from `seed.sql`. The database contains students, restaurants, meals, orders and order items. The web-app uses direct SQL queries in `app.py`, including `SELECT` statements for browsing meals/restaurants/orders and `INSERT` statements when a student places an order. It also includes regular expression matching to validate KU student emails before an order can be submitted.

Public repository URL: <https://github.com/marqy777/DIS-Project.git>

We developed and tested the project on Mac.

## How to clone the repository

### Mac

```bash
git clone https://github.com/marqy777/DIS-Project.git
cd DIS-Project
```

### Windows

```bash
git clone https://github.com/marqy777/DIS-Project.git
cd DIS-Project
```

## How to compile / set up the web-app from source

The project is a Python Flask app, so there is no separate compilation step. The setup step is to install the dependencies and initialize the SQLite database.

### Mac setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py
```

### Windows setup

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python init_db.py
```

## How to run the web-app

### Mac

```bash
source venv/bin/activate
python app.py
```

### Windows

```bash
venv\Scripts\activate
python app.py
```

Then open the URL shown in the terminal, normally:

```text
http://127.0.0.1:5000
```

## How to interact with the app

- Open the front page: `http://127.0.0.1:5000/`
- Click **Meals** to browse affordable meals.
- Use the filters to search by maximum price or category.
- Click **Order** on a meal and enter a name, KU email and quantity.
- The email must match the regex validation for `@student.ku.dk` or `@alumni.ku.dk`.
- After placing an order, the app inserts data into the database.
- Click **Orders** to see the stored order overview.

## Project deliverables checklist

- Git repository: this project is stored in a public GitHub repository.
- Documentation: this README explains setup, database initialization, running and interaction.
- E/R diagram: see `docs/er-diagram.md`.
- SQL database interaction: `app.py` uses direct SQLite SQL statements such as `SELECT` and `INSERT`.
- Regex requirement: `valid_ku_email()` in `app.py` uses a regular expression to validate KU emails.
- AI declaration: see `AI_DECLARATION.md`.
- Bonus: `schema.sql` includes the SQL view `cheap_meals`.

## Reset the database

Run this command to recreate the database from `schema.sql` and `seed.sql`:

```bash
python init_db.py
```
