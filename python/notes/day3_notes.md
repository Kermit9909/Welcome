# Day 3 Notes:

## Conditional Statements:

### if-else statement

Def: Fundamental programming construct used for decision-making. It allows a program to execute different blocks of code based on whether a specified condition evaluates to true or false.

### nested if-else statement

Def: A nested if-else statement is a control structure where one if-else statement is placed inside the body of another if or else block. This allows for hierarchical decision-making, where a secondary condition is only evaluated based on the result of a primary condition

### elif statement

Def: The if-elif statement is a shortcut for chaining multiple if-else conditions. While using if-elif statement at the end else block is added which is performed if none of the above if-elif statement is true.

### Useful Comparison Operators

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

### Example Code:
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print("Have fun!")
else:
    print("Sorry you must grow to greater heights.")
```

### Modulo Operator %
```
10 / 2 = 5 (remainder 0)

10 / 3 = 3.33333333 ( with 1 remaining)

10 % 3 = 1

10 % 2 = 0
```

### Example Usage:
```
print("Welcome to the Odds or Evens Game\n")
number = int(input("Please enter any number\n"))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Nested if / else

Example code:

```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Have fun!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you must grow to greater heights.")
```

## elif statement

Example Code:
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Have fun!")
    age = int(input("What is your age? "))
    if age > 18:
        print("Please pay $12.")
    elif age >= 12 or age <= 18:
        print("Please pay $7.")
    elif age > 12:
        print("Please pay $5.")
else:
    print("Sorry you must grow to greater heights.")

```
## Logical Operators
```
A and B
C or D
 not E
```






## Roller Coaster Project
```
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0


if height >= 120:
    print("Then you may ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18:
        bill = 18
        print("Adult tickets are $18.")
    elif age >= 12 or age <= 18:
        bill = 12
        print("Teenage tickets are $12.")
    elif age < 12:
        bill = 7
        print("Child tickets are $7.")

    wants_photo = input("Do you want a photo taken? Type y for Yes and n for No\n")
    if wants_photo == "y":
# In python += is a shorthand way of saying variable 'bill + 3'
        bill += 3
    
    print (f"Your final bill is ${bill}")
  
else:
    print("Sorry you must grow to greater heights.")
```

## Pizza Project:
```
# todo: work out how much they need to pay based on size
# s = $15 m = $20 l = $25
# todo: work out how much they need to add to bill based on pepperoni choice
# $2 (small), $3 (M/L)
# todo: work out their final amount based on whether they want extra cheese.
# $1
# A final print statement " Your final bill is: $ "


print("Welcome to Python Pizza Deliveries!")

bill = 0

size = input("What size pizza do you want? S, M, L: ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")
```