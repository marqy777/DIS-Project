# E/R Diagram

This is our database model for **Affordable Eats**. It matches the tables created in `schema.sql`.

```mermaid
erDiagram
    STUDENTS {
        int student_id PK
        string name
        string email UK
    }

    RESTAURANTS {
        int restaurant_id PK
        string name
        string address
        string cuisine_type
        float delivery_fee
    }

    MEALS {
        int meal_id PK
        int restaurant_id FK
        string name
        string description
        float price
        string category
        int is_student_discount
    }

    ORDERS {
        int order_id PK
        int student_id FK
        int restaurant_id FK
        string order_time
        string status
        float total_price
    }

    ORDER_ITEMS {
        int order_item_id PK
        int order_id FK
        int meal_id FK
        int quantity
        float item_price
    }

    RESTAURANTS ||--o{ MEALS : offers
    STUDENTS ||--o{ ORDERS : places
    RESTAURANTS ||--o{ ORDERS : receives
    ORDERS ||--|{ ORDER_ITEMS : contains
    MEALS ||--o{ ORDER_ITEMS : included_in
```

## Relationships

- One restaurant can offer many meals.
- One student can place many orders.
- One restaurant can receive many orders.
- One order contains one or more order items.
- Each order item refers to one meal.

## Tables and SQL files

- The tables are defined in `schema.sql`.
- The sample data is inserted from `seed.sql`.
- The database is initialized by running `python init_db.py`.
