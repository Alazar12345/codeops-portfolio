# Addis Eats Route Map

## Application Navigation Structure


/
│
├── /menu
│
├── /dish/:id
│
├── /cart
│
├── /login
│
└── /checkout


---

# Route Description


## Home Route

Path:

/
Purpose:

Landing page for the restaurant.

Contains:

- Hero section
- Featured dishes
- Restaurant information
- Navigation to menu


---

## Menu Route

Path:

/menu


Purpose:

Display all available Ethiopian dishes.

Contains:

- Search functionality
- Category filtering
- Dish cards


Data Required:

- Dish list
- Categories


---

## Dish Details Route

Path:

/dish/:id


Purpose:

Display detailed information about a selected dish.

Contains:

- Dish image
- Description
- Ingredients
- Price
- Add to cart option


Dynamic Parameter:

/dish/1



---

## Cart Route

Path:

/cart


Purpose:

Allow users to review selected items before checkout.

Contains:

- Cart items
- Quantity controls
- Remove item option
- Total calculation


---

## Login Route

Path:

/login


Purpose:

Allow users to authenticate.


Contains:

- Email input
- Password input
- Validation messages


---

## Checkout Route

Path:

/checkout


Purpose:

Collect customer order information.


Contains:

- Customer name
- Phone number
- Delivery address
- Order summary
- Submit order


---

# Route Flow
