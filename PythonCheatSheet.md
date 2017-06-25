# 30 Days of Python: Cheat Sheet
A quick reference guide for using the Python Programming language.


## Strings
```python
text = "Some string, with some stuff."

text2 = "Yet, another string here."

text3 = "Concatenation combines strings like \"" + text + "\" and \"" + text2  + "\""
print(text3)

```

### Formating

**`\n`: New Line**
```python
text = 'Often\nYou need a new line'
print(text)
```

**`\t`: Tab**
```python
text = 'Often a \t tab is needed.'
print(text)
```

**`\'`: Escaped single quote**
```python
text = 'Sometimes it\'s your quote sometimes it isn\'t'
print(text)
```

**`\"`: Escaped double quote**
```python
text = "Sometimes it\'s a \"Quote from someone else\""
print(text)
```

**`\`: Escaped linebreak**
```python
text = "Sometimes you need to have \
a inline break that isn't a linebreak."
print(text)
```


**`.lower()`: Lowercase entire string**
```python
text = "Some string, with some stuff."
text.lower()
print(text)
"some string, with some stuff."
```

**`.upper()`: Uppercase entire string**
```python
text = "Some string, with some stuff."
text.upper()
print(text)
"SOME STRING, WITH SOME STUFF.
```

**`.lower()` and `.upper()` to Capitalize string**
```python
lower_cased = "this sentence needs to be capitalized."

cap_string = lower_cased[0].upper() + lower_cased[1:]
print(cap_string)
"This sentence needs to be capitalized."
```

**`.split()` to Break up string**
```python
text = "Some string, with some stuff."
print(text.split())
['Some', 'string,', 'with', 'some', 'stuff.']

print(text.split(","))
['Some string', ' with some stuff.']
```

**`len()` to Count String Length**
```python
text_length = len("Some string, with some stuff.")
print(text_length)
29

text = "Some other length"
text_length2 = len(text)
print(text_length2)
17
```

### Substitution
**Format with Keyword Arguments (Variables)**
```python
text = "This is {variable_a} formatted string".format(variable_a="variable based")
print(text)

text = "This is another {variable_a} formatted string with \
multiple variables like {a} {b} {c}.".format(
    variable_a="variable based", 
    a="some random", b="replacement", c="text")
print(text)

text = """So, {name}, the best part is formated strings you don't have to order it. 
And these keyword argument replacements, ({var_a}, {var_b}, {name}) can be reused over and over.
Seriously {name}, this is some fun formatting.""".format(
            name="Jerry", 
            var_a="Variable 1", 
            var_b="Variable 2")
print(text)
```

**Format with Arguments**
```python
text = "This is {0} formatted string".format("argument based")
print(text)

text = "This is another {0} formatted string \
with multiple variables like {1} {2} {3}.".format(
    "variable based", 
    "some random", 
    "replacement", 
    "text"
    )
print(text)

text = """So, {0}, the best part is formated strings you don't have to order it. 
And these argument replacements, ({1}, {2}, {0}) can be reused over and over.
Seriously {0}, this is some fun formatting.""".format(
            "Jerry", 
            "Variable 1", 
            "Variable 2")
print(text)
```

**`%s` Substitution**
```python
text = "This is %s formatted string" %("replacement")
print(text)

text = "The %%s format string is not as %s, but still very %s." %("robust", "useful")
print(text)
```

**`%f` Float Substitution**
```python
text = "0 decimal places: %.0f" %(20)
print(text)


text = "2 decimal places: %.2f" %(20)
print(text)

text = "10 decimal places: %.10f" %(20)
print(text)

text = "400 decimal places: %.400f" %(20)
print(text)
```

**Date Substitution** [Docs](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)
```python
import datetime
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

text = today.strftime('%m/%d/%y')
print(text)

now = datetime.datetime.utcnow() #utc time
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text)

now = datetime.datetime.now() #local time
date_text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
text = "Time is: %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%B %d, %Y %H:%M:%S.%f %p')
text = "Time is %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%x')
text = "Time is %s" %(date_text)
print(text)

```

## Working with Files

```
file_obj = open(file_name, "<mode>")
```

| Mode          | Description   |
| ------------- | ------------- |
| "r"           | Read only. Default mode. |
| "rb"          | Read only in binary format |
| "r+"          | Read and write |
| "rb+"         | Read and write in binary format |
| "w"           | Write only. Overwrites existing file or creates a new file. |
| "wb"          | Write only in binary format. Overwrites existing file or creates a new file. |
| "w+"          | Read and write. Overwrites existing file or creates a new file. |
| "wb+"         | Read and write in binary format. Overwrites existing file or creates a new file.  |
| "a"           | Append to existing file or creates new file. |
| "ab"          | Append to existing file or creates new file in binary format. |
| "a+"          | Read and append. Overwrites existing file or creates a new file. |
| "ab+"         | Read and append in binary format. Overwrites existing file or creates a new file. |




