# Addis Eats Component Tree

## Application Structure


App

├── Layout

│
├── Header

│   ├── Logo

│   ├── Navigation

│   └── CartIndicator

│
└── Outlet


---

# Pages


## Home Page

Purpose:
Landing page and restaurant introduction.


Home

├── HeroSection

│   ├── RestaurantImage

│   ├── IntroductionText

│   └── ViewMenuButton

│
├── FeaturedDishes

│   └── DishCard

│
└── CategoryPreview


Component Ownership:

Home owns:
- Featured dish selection
- Homepage display data
- Hero content


---

## Menu Page

Purpose:
Display all available dishes.


Menu

├── SearchBar

├── CategoryFilter

└── DishGrid

    └── DishCard


Component Ownership:

Menu owns:
- Search query
- Selected category
- Filtered dish list


---

## Dish Details Page

Purpose:
Display complete information about one dish.


DishDetails

├── DishImage

├── DishInformation

│   ├── Name

│   ├── Description

│   ├── Ingredients

│   └── Price

│
└── AddToCartButton


Component Ownership:

DishDetails owns:
- Selected dish information
- Quantity selection


---

## Cart Page

Purpose:
Manage selected food items.


Cart

├── CartItem

│   ├── ItemImage

│   ├── ItemName

│   ├── QuantityControl

│   └── RemoveButton

│
└── CartSummary


Component Ownership:

Cart owns:
- Cart display
- Total calculation
- Quantity updates


---

## Login Page


Login

├── LoginForm

│   ├── EmailInput

│   ├── PasswordInput

│   └── SubmitButton


Component Ownership:

Login owns:
- Form validation
- Login submission


---

## Checkout Page


Checkout

├── CustomerForm

│   ├── NameInput

│   ├── PhoneInput

│   └── AddressInput

│
├── OrderSummary

└── SubmitOrderButton


Component Ownership:

Checkout owns:
- Customer information
- Order submission


---

# Shared Components


components

├── Header

├── Button

├── Card

├── DishCard

├── Input

├── LoadingSpinner

└── ErrorMessage


These components are reusable across multiple pages.