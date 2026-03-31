# Day 2
2026:03:30


## Data Types | Type Casting | Mathmatical Operations | f-strings
---

### Strings ( "  " )
 Def: an immutable sequence of Unicode characters used to store and manipulate text

Term: Subscripting

Ex. print("Hello"[0])
    H
### Accessing elements
data = ["apple", "banana", "cherry"]
print(data[1])  
Output: banana

### Integers - write a positive/negative number without anything else...
print(12 + 12)
24

***123,456,654 can be writen as 123_456_654 (human readable)

### Floats
Ex  
print(31.54)
31.54

### Boolean
print(True) or bool=True
print(False) or bool=False

### the Type function
Ex. 
print(type(12345))
<class 'int'>

***TRICK:  SHIFT + ALT + DOWN - Copies line of code to line below :)

## Type Casting/Conversion
    Def: Converting one data type into another (as long as it makes sense)
EX:
print(int("12" + int("12")) = "" are strings > int function converts to integer
24
More Examples:
    - int()
    - float()
    - str()
    - bool()

### Problem:
### print("Number of letters in your name: " + len(input("Enter your name")))

### Error:
### TypeError: can only concatenate str (not "int") to str

### This is one way to solve the problem
### print("Number of letters in your name: " + str(len(input("Enter your name"))))

## However this is the skill:

name_of_user = input("Enter your name")
length_of_name = len(name_of_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name))

print("Number of letters in your name: " + str(length_of_name))

## Mathmatical Operations

print("My age" + "12")
My age is 12
print(123 + 456)
579
print(7-3)
4
print (8*8)
64
print (6/3)
2.0
print (type(6 //3))
<class 'int'>
print(6//3) *Careful - it wipes everything past the decimal
2
print(2**16)
65536

## print(3*3+3/3-3)

# PEMDAS
# ()
# **
# * or /
# + or -
# = 7.0

Exercise:
bmi = (84/(1.65 ** 2))

print(bmi)
30.8539944...
print(int(bmi))
30
print(round(bmi))
31
print(round(bmi, 2))
30.85

## Assignment Operator - 
score=0
score += 1
print(score)
1

Examples: 
x = 10
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3

## THE F-STRING - Combining different data types 

score = 15
time_played = 20.5
is_winning = True

print(f"Congrats! Your score is {score}, total game time played {time_played} \
, and your team is winning = {is_winning}")
OUTPUT: Congrats! Your score is 15, total game time played 20.5 , and your team is winning = True