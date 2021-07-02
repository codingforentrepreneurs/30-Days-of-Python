# Day 6 - String Formatting & F-Strings
Python has ways to make writing text a bit more programmic and helps systematically remove repeating youself.

Also, check out:
- [pyformat](https://pyformat.info/)
- [strftime.org](https://strftime.org/)

### String Formatting

Basic formatting:

`#`: Write a comment `# this is a comment`

`\n`: New Line

`\t`: Tab

`\\` or `//`: Allowed Slash

`\'`: Allowed Single Quote

`\"`: Allowed Double quote

`{{` or `}}`: Allowed single curly bracket in formatted strings

`"your single-line text"`: Wrap a single quote (`'`) or double quote (`"`) around text / numbers to make it a string.

`\`: A `slash` in front of a `return`/`enter` will escape that. Allowing for multi-line strings without the triple quotes. Such as:
```python
"this is my string example\
when I close it here"
```


`""" your multi-line text"""`: Wrap 3x single quotes (```) or 3x double quotes (`"`) around a lot of text to allow for multi-line strings. Such as:
```python
"""this is my string example
when I close it here"""
```



#### The `.format()` method

_Empty_
```python
"{} {}".format("Hello", "World")
```

_Positional_
```python
"{0} {1} {0}".format("Hello", "World")
```

_Keyword_
```python
"{first} {second} {first}".format(first="Hello", second="World")
```

_Positional & Keyword_
```python
"{0} {second} {0}".format("Hello", second="World")

"{0} {1} {2['hello']}".format("Hello", "World", {'hello': 'sup'})
```

_Unpacking a Dictionary_
```python
data = {'name': 'Hodor', 'email': 'holdthe@door.com'}
txt = 'Name: {name}\nEmail: {email}'.format(**data)
print(txt)
```

_Numbers, Floats & Decimals_

Number / Integer
```python
"{:d}".format(32)
```
or
```python
"{}".format(32)
```



Float / Decimal
```python
"{:f}".format(32)
```

```python
pi = 3.14159265359
"{:f}".format(pi)
```

Limit to `n` decimal places. Replace `4` below with the number of decimal places to round to.
```python
pi = 3.14159265359
"{:.4f}".format(pi)
```



#### The `%` method

_Positional - Strings or Numbers_
```python
"%s %s %s %s" % ("Hello", 12, 131.312, {'hello': 'sup'})
```

_Keyword / Dictionary_
```python
"%(first)s %(second)s" % {"first":"Hello", "second":"World"}
```

_Keywords_ (Also known as named placeholders)
```python
data = {'name': 'Hodor', 'email': 'holdthe@door.com'}
txt = 'Name: %(name)s\nEmail: %(email)s' % data
print(txt)
```

_Numbers, Floats & Decimals_

Number
```python
"%d" % (32)
```
or
```python
"%s" % (32)
```

Float
```python
"%f" % (32)
```

```python
pi = 3.14159265359
"%f" % (pi)
```

Limit to `n` decimal places. Replace `2` below with the number of decimal places to round to.
```python
pi = 3.14159265359
"%.2f" % (pi)
```

#### `f` Strings (aka `f-string`)

_Strings or Number variables_
```python
first = "Hello"
second = "World"
third = 32.3122
fourth = "{:.2f}".format(third)
f"{first} {second} {first.upper()} {third} {fourth}"
```

_Dictionary_
```python
data = {'name': 'Hodor', 'email': 'holdthe@door.com'}
txt = f'Name: {data["name"]}\nEmail: {data["email"]}'
print(txt)
```

_Inline Math_
```python
hours = 21
seconds = 32
f"{hours} {seconds * 10} {seconds}"
```

_Inline Formatting_


```python
pi = 3.14159265359
f"{format(pi, '.2f')}"
```




#### Lesson Reference
```
>>> "hello justin, this is cool"
'hello justin, this is cool'
>>> f"hello {name}, this is cool"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> print(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> name = "Justin"
>>> f"hello {name}, this is cool"
'hello Justin, this is cool'
>>> names = ["J", "A", "E"]
>>> for name in names:
...     print(f"Hello {name}")
... 
Hello J
Hello A
Hello E
>>> msg = "hi there" + " this is cool " + "the end."
>>> msg
'hi there this is cool the end.'
>>> msg = "" 
>>> for i in names:
...    msg += f"name: {i}"
... 
>>> print(msg)
name: Jname: Aname: E
>>> template = """Hello there,
... {name} this is an amazing way to do
... subbing my cool items."""
>>> print(template)
Hello there,
{name} this is an amazing way to do
subbing my cool items.
>>> template.format(name='J')
'Hello there,\nJ this is an amazing way to do\nsubbing my cool items.'
>>> print('hello world\nagain''hello world\nagain'
... 
... )
hello world
againhello world
again
>>> print(template.format(name='J'))
Hello there,
J this is an amazing way to do
subbing my cool items.
>>> "\n"
'\n'
>>> print("\n")


>>> """hello
... another"""
'hello\nanother'
>>> "hello\nanother".replace("\n", "")
'helloanother'
>>> "hello\nanother".replace("\n", " ")
'hello another'
>>> "hello\nanother".replace("\n", "<br/>")
'hello<br/>another'
>>> "Hello \
... this is another line or is it?"
'Hello this is another line or is it?'
>>> "hello 
  File "<stdin>", line 1
    "hello 
          ^
SyntaxError: EOL while scanning string literal
>>> "hello \
... abc
  File "<stdin>", line 2
    abc
      ^
SyntaxError: EOL while scanning string literal
>>> "http:\\thisisaweomse"
'http:\\thisisaweomse'
>>> print("http:\\thisisaweomse"
... )
http:\thisisaweomse
>>> print("http:\\\\thisisaweomse")
http:\\thisisaweomse
>>> `\\`
  File "<stdin>", line 1
    `\\`
    ^
SyntaxError: invalid syntax
>>> "http://www.helloworld.com"
'http://www.helloworld.com'
>>> "http:\\www.helloworld.com"
'http:\\www.helloworld.com'
>>> template = "{name} is cool but I want to include {}".format(name='Justin")
  File "<stdin>", line 1
    template = "{name} is cool but I want to include {}".format(name='Justin")
                                                                             ^
SyntaxError: EOL while scanning string literal
>>> template = "{name} is cool but I want to include {}".format(name='Justin')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 0 out of range for positional args tuple
>>> template = "{name} is cool but I want to include {}".format('abc', name='Justin')
>>> template
'Justin is cool but I want to include abc'
>>> template = "{name} is cool but I want to include {{}}".format(name='Justin')
>>> template
'Justin is cool but I want to include {}'
>>> f"{name} just "
'E just '
>>> 3.14523423
3.14523423
>>> pi = 3.14523423
>>> f"{pi}"
'3.14523423'
>>> "{}".format(pi)
'3.14523423'
>>> "{:f}".format(pi)
'3.145234'
>>> "{:f}".format(23)
'23.000000'
>>> "{:.2f}".format(pi)
'3.15'
>>> "{:.4f}".format(pi)
'3.1452'
>>> 
>>> 
>>> format()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: format expected at least 1 argument, got 0
>>> format(pi)
'3.14523423'
>>> format(pi, ".2f")
'3.15'
>>> pi
3.14523423
>>> pi * 313223
985159.70122329
>>> format(pi, ".2f") * 3
'3.153.153.15'
>>> f"{pi}"
'3.14523423'
>>> f"{format(pi, '.2f')}"
'3.15'
```
