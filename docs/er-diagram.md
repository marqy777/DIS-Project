# E/R Diagram Placeholder

Add the final E/R diagram here when the database design is complete.

Current planned entities:

- `students`
- `restaurants`
- `meals`
- `orders`
- `order_items`

Current planned relationships:

- One restaurant has many meals.
- One student can place many orders.
- One order belongs to one restaurant.
- One order contains one or more order items.
- Each order item refers to one meal.

```mermaid
erDiagram
    USER {
        int UserID PK
        string Email
        string PhoneNumber
        string Name
    }
    ORDER {
        int OrderID PK
        string Status
        decimal TotalPrice
        datetime Time
    }
    ORDER_ITEM {
        int OrderID PK
        int FoodID PK
        int Quantity
        decimal Price
    }
    FOOD_ITEMS {
        int FoodID PK
        string Name
        decimal Price
    }
    COURIER {
        int CourierID PK
        string Name
        string Location
        int AddressID FK
        string City
    }
    ADDRESS {
        int AddressID PK
        string Street
        string PostalCode
    }
    RESTAURANT {
        int RestaurantID PK
        string Name
        string Location
        float Rating
    }
    OFFER {
        int OfferID PK
        decimal Discount
        date ValidUntil
    }

    USER ||--o{ ORDER : "Places"
    ORDER ||--|{ ORDER_ITEM : "Contains"
    ORDER_ITEM }|--|| FOOD_ITEMS : "Places"
    ORDER }o--|| COURIER : "Has"
    COURIER }|--|| ADDRESS : "From"
    FOOD_ITEMS }|--|| RESTAURANT : "Belongs to"
    RESTAURANT ||--o{ OFFER : "Has"
```