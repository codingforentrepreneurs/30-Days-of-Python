# Day 2 - Variables, Data Types and Operators
This tutorial is based on variables, data types and operators

## Variables
A variable holds a value in a memory location that is needed for the execution of your program.

### Using a variable
A memory location needs to be allocated for the variable value, before it can be used by the program.

**Declaring a variable** means stating what _data type_ will be used for the value. 
**Initialising a variable** means _setting the initial value_. Python doesn’t use variable declaration, only initialisation.

**Example**
```python
name = "Alex"
print(name)
```

## Data Types
There are five main data types namely;
- String (text) e.g "Alex", "Sofia"
- Integer (whole numbers) e.g. 3, 4, 5
- Boolean (True or False) e.g. True, False
- Real or floating point numbers (decimal numbers) e.g. 4.5, 7.54
- Char (single string characters) e.g. "a", "z", "b"

**N.B:** Incorrect data types can cause problems during the execution of your programs.

**Question**

Predict what might happen when this code is executed.

```python
print("Enter a number")
num1 = input()
print("Enter another number")
num2 = input()
print(num1+num2)
```
**Output**
```bash
Enter a number
1
Enter another number
2
12
>>>
```
The data type for an input is always string. When you add two pieces of string together, it will concatenate (join) them. 
Instead of adding the two numbers together to make 3, it has joined the corresponding strings together to make 12 (one,two). 
This code has produced a logic error because it hasn’t executed as expected.

If you want Python to use your value as an integer, then you need to tell it that by **casting the value**. 
You do this by placing `input()` inside the `int()` function.

```python
print("Enter a number")
num1 = int(input())
print("Enter another number")
num2 = int(input())
print(num1+num2)
```

```bash
Enter a number
1
Enter another number
2
3
```

Errors can still happen during execution, even when casting has been used.
 **Question**
 
What might happen if the user enters ‘four’ when this code is executed?

**Answer**

A runtime error occurs. This is a type of error that causes the program to crash during execution.

```python
print("Enter a number")
number = int(input())
print(number)
```

```bash
Enter a number
four
Traceback (most recent call last):
  File "c:\users\pi\mu_code\fsea.py", line 2, in <module>
    number = int(input())
ValueError: invalid literal for int() with base 10: 'four'
>>>
```

You can avoid this type of error by introducing validation checks. 
Here is an example check that you can use called try and except. 

```python
print("Enter a number")
try:
    number = int(input())
except ValueError:
    print("You must enter a number")
    number = int(input())
```
To convert values to different data types, you need to know the functions that are available to you. 
Here are the most common functions that you will need to know.

```python
# convert to string
str() 
# convert to integer
int()
# convert to real
float()
```

## Operators

Adding
```
10 + 10
```
Multiply
```
9 * 32
```
Divide

24 / 6

Exponent 

4 ** 2

Modulo (Remainder)

24 % 5

Greater Than

55 > 22

Less Than

132 < 123


