Day 3 - Lists & Dictionaiers

Code https://github.com/codingforentrepreneurs/30-days-of-python
github: cfe.sh/github

## Reference
_Coming soon_

__Declare__
```
my_list = []
```
or
```
my_list = [1, 2, 3, 4, 5]
```


### Lists
```python
>>> my_cart = [12.99, 312, 32, 142]
>>> sum(my_cart)
498.99
>>> my_cart.append(39.99)
>>> print(my_cart)
[12.99, 312, 32, 142, 39.99]
>>> len(my_cart)
5
>>> my_cart
[12.99, 312, 32, 142, 39.99]
>>> my_cart[3]
142
>>> my_cart[2]
32
>>> my_cart[2] * 120
3840
>>> my_string = "hello world"
>>> len(my_string)
11
>>> my_string[4]
'o'

>>> my_cart
[12.99, 312, 32, 142, 39.99]
>>> my_items = ["mouse", "laptop", "mic", "screen", "snack"]
>>> my_items
['mouse', 'laptop', 'mic', 'screen', 'snack']
>>> my_cart[1]
312
>>> my_items[1]
'laptop'
>>> my_products = [my_items, my_cart]
>>> my_products
[['mouse', 'laptop', 'mic', 'screen', 'snack'], [12.99, 312, 32, 142, 39.99]]
>>> 
```

### Dictionaries
```python
>>> my_list = [1,2,3,4,5]
>>> my_data = {"name": "Justin Mitchel"}
>>> my_data["name"]
'Justin Mitchel'
>>> my_data = {"name": "Justin Mitchel", "location": "California"}
>>> my_data[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> my_data.keys()
dict_keys(['name', 'location'])
>>> list(my_data.keys())
['name', 'location']
>>> list(my_data.keys())[0]
'name'
>>> my_data.append({"occ": "coder"})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'append'
>>> my_data["occ"] = "Coder"
>>> my_data
{'name': 'Justin Mitchel', 'location': 'California', 'occ': 'Coder'}
>>> user_1 = {"name": "James bond"}
>>> user_2 = {"name": "Ned Stark"}
>>> my_users = [user_1, user_2]
>>> my_users
[{'name': 'James bond'}, {'name': 'Ned Stark'}]
```
