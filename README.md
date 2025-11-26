# Inventory-Management-System
A simple Python-based inventory management system that supports adding items, updating stock, checking availability, and processing sales reports with automatic revenue calculations.

# Global Inventory Dictionary

Stores all items using the format:

inventory = {
    "ItemName": {
        "price": float,
        "stock": int
    }
}

# Add Items

Prevents duplicates and adds new inventory items with price and stock.

# Update Stock

Safely increases or decreases stock levels, preventing negative stock.

# Check Availability

Returns current stock or an error message if the item does not exist.

# Sales Report

Processes a dictionary of items sold and:

Validates item existence

Checks if enough stock is available

Deducts stock after successful sale

Calculates total revenue

Returns formatted revenue output

Also prints descriptive error messages when needed.
