import re
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash

DATABASE = "affordable_eats.db"

app = Flask(__name__)
app.secret_key = "dev-key-change-later"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def valid_ku_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@(student\.ku\.dk|alumni\.ku\.dk)$"
    return re.match(pattern, email) is not None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/restaurants")
def restaurants():
    connection = get_db_connection()
    restaurants = connection.execute(
        "SELECT * FROM restaurants ORDER BY name"
    ).fetchall()
    connection.close()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/meals")
def meals():
    max_price = request.args.get("max_price", "")
    category = request.args.get("category", "")

    query = """
        SELECT meals.*, restaurants.name AS restaurant_name
        FROM meals
        JOIN restaurants ON meals.restaurant_id = restaurants.restaurant_id
        WHERE 1 = 1
    """
    params = []

    if max_price:
        query += " AND meals.price <= ?"
        params.append(max_price)

    if category:
        query += " AND meals.category LIKE ?"
        params.append(f"%{category}%")

    query += " ORDER BY meals.price ASC"

    connection = get_db_connection()
    meals = connection.execute(query, params).fetchall()
    connection.close()

    return render_template("meals.html", meals=meals, max_price=max_price, category=category)


@app.route("/order/<int:meal_id>", methods=["GET", "POST"])
def order(meal_id):
    connection = get_db_connection()
    meal = connection.execute(
        """
        SELECT meals.*, restaurants.name AS restaurant_name, restaurants.delivery_fee
        FROM meals
        JOIN restaurants ON meals.restaurant_id = restaurants.restaurant_id
        WHERE meals.meal_id = ?
        """,
        (meal_id,),
    ).fetchone()

    if meal is None:
        connection.close()
        flash("Meal not found.")
        return redirect(url_for("meals"))

    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        quantity = int(request.form["quantity"])

        if not valid_ku_email(email):
            connection.close()
            flash("Please use a KU email ending in @student.ku.dk or @alumni.ku.dk.")
            return render_template("order.html", meal=meal)

        student = connection.execute(
            "SELECT * FROM students WHERE email = ?", (email,)
        ).fetchone()

        if student is None:
            cursor = connection.execute(
                "INSERT INTO students (name, email) VALUES (?, ?)", (name, email)
            )
            student_id = cursor.lastrowid
        else:
            student_id = student["student_id"]

        total_price = (meal["price"] * quantity) + meal["delivery_fee"]

        cursor = connection.execute(
            """
            INSERT INTO orders (student_id, restaurant_id, total_price)
            VALUES (?, ?, ?)
            """,
            (student_id, meal["restaurant_id"], total_price),
        )
        order_id = cursor.lastrowid

        connection.execute(
            """
            INSERT INTO order_items (order_id, meal_id, quantity, item_price)
            VALUES (?, ?, ?, ?)
            """,
            (order_id, meal_id, quantity, meal["price"]),
        )

        connection.commit()
        connection.close()
        return redirect(url_for("order_success", order_id=order_id))

    connection.close()
    return render_template("order.html", meal=meal)


@app.route("/order-success/<int:order_id>")
def order_success(order_id):
    connection = get_db_connection()
    order = connection.execute(
        """
        SELECT orders.*, students.name AS student_name, students.email,
               restaurants.name AS restaurant_name
        FROM orders
        JOIN students ON orders.student_id = students.student_id
        JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id
        WHERE orders.order_id = ?
        """,
        (order_id,),
    ).fetchone()
    connection.close()
    return render_template("order_success.html", order=order)


@app.route("/admin")
def admin():
    connection = get_db_connection()
    orders = connection.execute(
        """
        SELECT orders.order_id, orders.order_time, orders.status, orders.total_price,
               students.name AS student_name,
               restaurants.name AS restaurant_name,
               meals.name AS meal_name,
               order_items.quantity
        FROM orders
        JOIN students ON orders.student_id = students.student_id
        JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id
        JOIN order_items ON orders.order_id = order_items.order_id
        JOIN meals ON order_items.meal_id = meals.meal_id
        ORDER BY orders.order_time DESC
        """
    ).fetchall()
    connection.close()
    return render_template("admin.html", orders=orders)


if __name__ == "__main__":
    app.run(debug=True)
