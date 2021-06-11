# Day 5 - Conditions & Control Flow

__Reference__
```
>>> True
>>> False

>>> True == False

>>> True != False

>>> 10 > 31

>>> 94 < 123

>>> 133 >= 133

>>> 133 <= 201

>>> "abc" == "ABC".lower()

>>> "XyZ".upper() == "XYZ"

>>> str(True).lower() == "true":

>>> 1 > 10

>>> (3123 / 30) == 32

>>> 24 % 5 == 3

```


__Conditions & Conditional Statements__
```
>>> True
True
>>> False
False
>>> if True:
...    print("hi there")
... 
hi there
>>> if False:
...    print("nothing")
... 
>>> if not False:
...    print("whats up")
... 
whats up
>>> True == False
False
>>> var_ = "this"
>>> True = False
  File "<stdin>", line 1
SyntaxError: cannot assign to True
>>> for = True
  File "<stdin>", line 1
    for = True
        ^
SyntaxError: invalid syntax
>>> 10 > 32
False
>>> 424 < 323433
True
>>> 10 > 32 or 10 < 32
True
>>> not 10 > 32
True
>>> not (10 > 32)
True
>>> 200 > 200
False
>>> 200 >= 200
True
>>> 200 > 200 or 200 == 200
True
>>> true, false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> str(True).lower() == "true"
True
>>> str("true").title() == "True"
True
>>> str("true")
'true'
>>> "abc".title()
'Abc'
>>> bool(str("true").title())
True
>>> abc = [1,2,3,4,5]
>>> abc_sq = []
>>> for num in abc:
...     new_number = num ** 2
...     abc_sq.append(new_number)
... 
>>> abc_sq
[1, 4, 9, 16, 25]
>>> is_even = []
>>> is_odd = []
>>> for num in abc_sq:
...     if num % 2 == 0:
...        print("this is even") 
...        is_even.append(num)
...     else:
...        is_odd.append(num)
... 
this is even
this is even
>>> print(is_even, is_odd)
[4, 16] [1, 9, 25]
>>> is_factor_of_3 = []
>>> for num in abc_sq:
...    if num % 3 == 0:
...       is_factor_of_3.append(num)
...    elif num % 2 == 0:
...       is_even.append(num)
...    else:
...       is_odd.append(num)
... 
>>> print(is_factor_of_3)
[9]
>>> print(is_even, is_odd)
[4, 16, 4, 16] [1, 9, 25, 1, 25]
>>> is_even = []
>>> is_odd = []
>>> is_factor_of_3 = []
>>> for num in abc_sq:
...     if num % 3 == 0: 
...        is_factor_of_3.append(num)
...     else:
...        if num % 2 == 0:
...           is_even.append(num)
...        else:
...           is_odd.append(num)
... 
>>> print(is_even, is_odd)
[4, 16] [1, 25]
>>> print(is_factor_of_3)
[9]
>>> for num in abc_sq:
...     if num % 3 == 0:
...        is_factor_of_3.append(num)
...     if num % 2 == 0:
...        is_even.append(num)
...     is_odd.append(num)
... 
>>> print(is_even, is_odd)
[4, 16, 4, 16] [1, 25, 1, 4, 9, 16, 25]
```


__While Loops & Control Flow__
```
🕹 % python3 
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 10
>>> i = 0
>>> while i < x:
...     print(i)
...     i = i + 1
... 
0
1
2
3
4
5
6
7
8
9
>>> while i < x:
...    print(i)
... 
>>> i = 0
>>> while i < x:
...     print(i)
... 
0
0

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> x = 10
>>> i = 0 
>>> z = 12
>>> while i < x:
...    z = z * 2
...    if z > 342900:
...       break
...    print(z, i)
...    i = i + .00000000001
... 
24 0
48 1e-11
96 2e-11
192 3e-11
384 4e-11
768 4.9999999999999995e-11
1536 6e-11
3072 7e-11
6144 8.000000000000001e-11
12288 9.000000000000001e-11
24576 1.0000000000000002e-10
49152 1.1000000000000002e-10
98304 1.2000000000000003e-10
196608 1.3000000000000002e-10
>>> x = 10
>>> i = 0
>>> while i < x:
...    if i % 2 == 0:
...       print("even")
...    else:
...       continue
...    i += 1
... 
even
^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> while i < x:
...    print(i)
...    if i % 2 == 0:
...      print("even")
...    else:
...      continue
...    i = i + 1
... 
1
1
1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> x = 10
>>> i = 0
>>> while i < x:
...    if i % 2 == 0:
...       continue
...    else:
...       print('odd')
...    i += 1
... 
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> while i < x:
...     i += 1
...     if i % 2 == 0:
...       continue
...     print(i)
... 
1
3
5
7
9
>>> 

```
