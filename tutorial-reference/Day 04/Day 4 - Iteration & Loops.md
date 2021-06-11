# Day 4 - Iteration & Loops



### The `for` loop:
```
🕹 % python3
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> my_list = [1,2,3,4,5]
>>> my_list[0]
1
>>> my_list[1]
2
>>> my_list[2]
3
>>> my_list[3]
4
>>> my_list[4]
5
>>> for my_var in my_list:
...     print(my_var)
... 
1
2
3
4
5
>>> my_var
5
>>> for i in "abc":
... print(i)
  File "<stdin>", line 2
    print(i)
    ^
IndentationError: expected an indented block
>>> 
>>> for i in "abc":
...     print(i)
...    print(i)
  File "<stdin>", line 3
    print(i)
           ^
IndentationError: unindent does not match any outer indentation level
>>> for i in "abc":
...    print(i)
...    print(i)
... 
a
a
b
b
c
c
>>> "abc"[1]
'b'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for x in 10:
...     print(x)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> for x in "10":
...    print(x)
... 
1
0
>>> for x in range(0, 10):
...     print(x)
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
>>> user_1 = {'username': 'jmitchel3', 'id': 1}
>>> user_2 = {'username': 'abc', 'id': 2}
>>> my_users = [user_1, user_2]
>>> for user in my_users:
...     print(user)
... 
{'username': 'jmitchel3', 'id': 1}
{'username': 'abc', 'id': 2}
>>> for user in my_users:
...     print(user['username'])
... 
jmitchel3
abc
>>> for user in my_users:
...     print(user['email'])
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyError: 'email'
>>> user_2 = {'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}
>>> print(my_users)
[{'username': 'jmitchel3', 'id': 1}, {'username': 'abc', 'id': 2}]
>>> my_users = [user_1, user_2]
>>> print(my_users)
[{'username': 'jmitchel3', 'id': 1}, {'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}]
>>> for user in my_users:
...     print(user['email'])
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyError: 'email'
>>> for user in my_users:
...     if 'email' in user:
...         print(user['email'])
... 
abc@abc.abc
>>> selected_user = {}
>>> my_user_lookup = 2
>>> for user in my_users:
...     if 'id' in user:
...        if user['id'] == my_user_lookup:
...           selected_user = user
... 
>>> print(selected_user)
{'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}
>>> for x in range(0, 10):
...    print(x)
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
>>> for x in range(0, 10):
...    for user in my_users:
...        if user['id'] == x:
...           print(user)
... 
{'username': 'jmitchel3', 'id': 1}
{'username': 'abc', 'id': 2, 'email': 'abc@abc.abc'}
```
