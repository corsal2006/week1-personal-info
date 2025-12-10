# --------------------------------------------------
# Author: Siddesh Naik
# Project: Personal Information Manager
# Description: Stores and displays personal info
# --------------------------------------------------

# -------------------------------
# Step 2: Static information
# -------------------------------

# Name of the user (string)
name = "Siddesh Naik"

# Age of the user (integer)
age = 18

# City where the user lives (string)
city = "Mumbai"

# Hobby or interest (string)
hobby = "Coding"

# -------------------------------
# Step 3: Get user input
# -------------------------------

print("👋 Welcome to the Personal Information Manager!")

# Ask user for their favorite food and color
favorite_food = input("Enter your favorite food: ").strip()
favorite_color = input("Enter your favorite color: ").strip()

# Basic input validation (check for empty string)
if not favorite_food:
    favorite_food = "Not provided"

if not favorite_color:
    favorite_color = "Not provided"

# -------------------------------
# Step 4 & Enhancements
# -------------------------------

# Calculate age in months
age_in_months = age * 12

# Display information using formatted output
print("\n============================")
print("📌 Personal Information Summary")
print("============================")

# Using f-strings for formatting
print(f"Name         : {name}")
print(f"Age          : {age} years ({age_in_months} months)")
print(f"City         : {city}")
print(f"Hobby        : {hobby}")
print(f"Food         : {favorite_food}")
print(f"Color        : {favorite_color}")

print("============================")
print("🎉 Thank you for using this program!")
print("============================")
