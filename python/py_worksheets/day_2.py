
#Project 2: Build a tip calculator

# Welcome Header for the program
print("Welcome to the tip calculator!")

# Ask the user what their total bill amount was
total_bill = float(input("What was the total bill amount? $"))

# Use integer for user to input a value of 10, 12, or 15 percent tip
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15 "))

# Asking the user for integer input for the amount of people splitting the total amount

split_between = int(input("How many people to split the bill? "))

# Calculation using variables to find bill total + tip
total_with_tip = total_bill + (total_bill * tip_percentage / 100)

# Calculating total_with_tip divided by number of people and rounding value 2 decimal places

per_person = round(total_with_tip / split_between, 2)
# Final print statement of tip calculator

print(f"Each person should pay: ${per_person}")





