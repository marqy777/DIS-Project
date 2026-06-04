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
    STAKEHOLDER {
        int StakeholderID PK
        string Email
        string Name
        string Phone
    }
    ADDRESS {
        int AddressID PK
        string Street
        string City
        string PostalCode
    }
    CUSTOMER {
        int StakeholderID PK
        string Password
    }
    COURIER {
        int StakeholderID PK
        string VehicleType
    }
    RESTAURANT {
        int StakeholderID PK
    }
    UNITED_ORDERS {
        int UnitedOrderID PK
        datetime CreatedTime
    }
    ORDER {
        int OrderID PK
        datetime OrderTime
        string Status
        decimal TotalPrice
    }
    ORDER_ITEM {
        int Quantity
        decimal Price
        decimal Subtotal
    }
    DISH {
        int DishID PK
        string Name
        decimal Price
    }
    CUISINE {
        int CuisineID PK
        string Name
    }
    COURIER_RATING {
        int Rating
        datetime TimeOfRating
        string Comment
    }
    RESTAURANT_RATING {
        int Rating
        datetime TimeOfRating
        string Comment
    }

    STAKEHOLDER }o--|| ADDRESS : "Has base location"
    STAKEHOLDER ||--|| CUSTOMER : "Is-a"
    STAKEHOLDER ||--|| COURIER : "Is-a"
    STAKEHOLDER ||--|| RESTAURANT : "Is-a"
    CUSTOMER ||--o{ UNITED_ORDERS : "Places"
    UNITED_ORDERS ||--|{ ORDER : "Includes"
    ORDER ||--|{ ORDER_ITEM : "Contains"
    ORDER_ITEM }|--|| DISH : "Refers to"
    RESTAURANT ||--|{ DISH : "Offers"
    DISH }|--|| CUISINE : "Specializes in"
    COURIER }o--o{ RESTAURANT : "Tag Favorite"
    CUSTOMER ||--o{ COURIER_RATING : "rates"
    COURIER ||--o{ COURIER_RATING : "rated by"
    CUSTOMER ||--o{ RESTAURANT_RATING : "rates"
    RESTAURANT ||--o{ RESTAURANT_RATING : "rated by"
```
