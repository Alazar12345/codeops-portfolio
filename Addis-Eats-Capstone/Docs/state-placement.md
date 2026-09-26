# Addis Eats State Placement Table


## State Management Strategy

The application uses different state locations depending on how widely the data is needed.

- Global state is used for data shared across multiple pages.
- Local component state is used for page-specific UI behavior.
- Form libraries manage form-related state and validation.


---

# State Placement Table


| State | Location | Management Method | Reason |
|---|---|---|---|
| User authentication | Global | Zustand authStore | User information is required across protected pages |
| Cart items | Global | Zustand cartStore | Cart data is shared between menu, dish details, and checkout |
| Order information | Global | Zustand orderStore | Required during checkout and order confirmation |
| Selected dish | URL parameter | React Router (`:id`) | Dish details are identified through route navigation |
| Search text | Menu Page | React useState | Only the menu page uses search functionality |
| Selected category | Menu Page | React useState | Only affects menu filtering |
| Quantity selection | Cart Item component | React useState | Controls one item's quantity |
| Login form data | Login Page | React Hook Form | Handles form state and validation |
| Checkout form data | Checkout Page | React Hook Form | Handles customer input and validation |
| Loading status | Component/Page level | React state | Controls loading UI |
| Error messages | Error Boundary | React Error Boundary | Handles application errors safely |


---

# Global State


## Auth Store

Contains:

- Current user
- Login status
- Logout function


Used by:

- Header
- Profile
- Checkout


---

## Cart Store

Contains:

- Cart items
- Add item function
- Remove item function
- Update quantity function
- Total calculation


Used by:

- Menu
- Dish Details
- Cart
- Checkout


---

## Order Store

Contains:

- Current order
- Order history
- Order submission status


Used by:

- Checkout
- Order confirmation


---

# Local Component State


## Menu Page

Owns:

- Search input
- Category filter
- Display options


Reason:

These values only affect menu browsing.


---

## Cart Item

Owns:

- Temporary quantity changes
- Item interaction state


Reason:

Each cart item manages its own UI behavior.


---

# Form State


## Login Form

Managed by:

React Hook Form + Zod


Handles:

- Email validation
- Password validation
- Submit errors


---

## Checkout Form

Managed by:

React Hook Form + Zod


Handles:

- Customer information
- Delivery address
- Order validation


---

# Data Flow Example


User selects a dish:
