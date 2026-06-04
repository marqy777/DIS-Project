INSERT INTO students (name, email)
VALUES
('Test Student', 'test@student.ku.dk');

INSERT INTO restaurants (name, address, cuisine_type, delivery_fee)
VALUES
('Budget Bites', 'Nørrebrogade 10', 'Fast food', 15),
('Campus Curry', 'Universitetsparken 2', 'Indian', 20),
('Pasta Point', 'Amagerbrogade 50', 'Italian', 10);

INSERT INTO meals (restaurant_id, name, description, price, category, is_student_discount)
VALUES
(1, 'Student Burger', 'Simple burger with fries', 45, 'burger', 1),
(1, 'Cheap Wrap', 'Chicken wrap', 39, 'wrap', 1),
(1, 'Fries Box', 'Large fries with dip', 29, 'snack', 1),
(2, 'Lentil Curry', 'Vegetarian curry with rice', 49, 'curry', 1),
(2, 'Chicken Curry', 'Chicken curry with rice', 65, 'curry', 0),
(3, 'Tomato Pasta', 'Pasta with tomato sauce', 42, 'pasta', 1),
(3, 'Carbonara', 'Classic carbonara', 68, 'pasta', 0),
(3, 'Garlic Bread', 'Small garlic bread', 25, 'snack', 1);