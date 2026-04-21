

# Ask user for weight in kilograms
# Ask user for height in meters
# Calculate BMI and round to nearest interger

print("Welcome to the BMI Index Calculator\n")
weight = float(input("What is your weight in kilograms?\n"))
height = float(input("What is your height in meters?\n"))
bmi = (weight / height ** 2)
print(f"Your BMI is {round(bmi, 1)}")
      
