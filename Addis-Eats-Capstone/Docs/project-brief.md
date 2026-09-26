# Addis Eats Capstone

## Project Overview

Addis Eats is a digital restaurant ordering platform that allows customers to discover Ethiopian dishes, explore menu items, view food details, and place orders through a simple and user-friendly interface.

The goal of this project is to create a modern restaurant experience that connects customers with Ethiopian cuisine through an organized online ordering system.

---

## Problem

Many local restaurants in Ethiopia still depend on traditional ordering methods. Customers often have difficulty viewing menus, comparing dishes, understanding prices, and placing orders conveniently.

Restaurants also need a better way to present their food offerings digitally and improve the customer ordering experience.

---

## Target Users

### Customers

People who want to:

- Discover Ethiopian dishes
- View restaurant menus online
- Learn about ingredients and prices
- Add meals to a cart
- Place food orders easily

### Restaurant Owners

Businesses that want to:

- Display their menu digitally
- Showcase popular dishes
- Improve customer experience

---

## Solution

Addis Eats provides a digital restaurant platform where users can browse Ethiopian dishes, search and filter menu items, view detailed dish information, manage their cart, and complete checkout.

The application focuses on a clean user interface, reusable components, and modern React development practices.

---

## Main Screens

### 1. Home Screen

Purpose:
Introduce the restaurant and display available dishes.

Data:
- Featured dishes
- Categories
- Search keywords
- Restaurant information

---

### 2. Menu Screen

Purpose:
Allow users to browse all available food items.

Data:
- Dish name
- Image
- Description
- Price
- Category

---

### 3. Dish Details Screen

Purpose:
Show complete information about a selected dish.

Data:
- Dish image
- Name
- Description
- Price
- Ingredients
- Quantity options

---

### 4. Cart Screen

Purpose:
Allow users to review selected dishes before checkout.

Data:
- Selected dishes
- Quantity
- Item prices
- Total price

---

### 5. Login and Checkout Screen

Purpose:
Authenticate users and collect order information.

Data:
- User information
- Email
- Password
- Delivery address
- Payment method

---

## Application Data

### Dish

- id
- name
- image
- description
- price
- category

### User

- id
- name
- email

### Cart Item

- dishId
- quantity

### Order

- userId
- items
- total
- delivery information