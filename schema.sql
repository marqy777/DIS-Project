DROP VIEW IF EXISTS cheap_meals;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS meals;
DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    cuisine_type TEXT NOT NULL,
    delivery_fee REAL NOT NULL
);

CREATE TABLE meals (
    meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK (price >= 0),
    category TEXT NOT NULL,
    is_student_discount INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    order_time TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'placed',
    total_price REAL NOT NULL CHECK (total_price >= 0),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    meal_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    item_price REAL NOT NULL CHECK (item_price >= 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);

CREATE VIEW cheap_meals AS
SELECT
    meals.meal_id,
    meals.name AS meal_name,
    meals.price,
    meals.category,
    restaurants.name AS restaurant_name
FROM meals
JOIN restaurants ON meals.restaurant_id = restaurants.restaurant_id
WHERE meals.price <= 50;