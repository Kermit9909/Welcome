# 100 Days of Python
Date: 2026:03:27
Day: 1

## String Manipulation

print ("Hello World!")
> Run

print("Hello World")

**Option 1 - Multiple print statements:**

print("1. Mix stuff")
print("2. Knead dough")
print("3. Let it rise")
```

**Option 2 - One print with \n (newline character):**

print("1. Mix stuff\n2. Knead dough\n3. Let it rise")
```

**Option 3 - Triple quotes (cleanest for long recipes):**

print("""
1. Mix stuff
2. Knead dough
3. Let it rise
""")

## Concatenate

print("Hello" + "Sean")
HelloSean
print ("Hello " + "Sean")
Hello Sean
print("Hello" + " " + "Sean")
Hello Sean

**Spaces are important in Python!!!**
    - Indentation Errors

## Input Function (User Interation)

Def:
input("A prompt for the user")

Ex:
print("Hello " + input("What is your name?"))

**Installed Thonny for learning**
**'#'** for comments (good practice)
**Use ctrl + / to comment a whole line of code in python**

## Variables

 Step 1 = create the input
 Step 2 = use length function and wrap around input
 Step 3 = use a print statement to print input>lenth calculation
 print(len(input("What is your name?")))

## The real way!  The power of Variables
username = input("What is your name?")
lenth = len(username)
print(lenth)

