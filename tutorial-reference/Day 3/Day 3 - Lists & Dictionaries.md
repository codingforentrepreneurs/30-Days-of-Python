Mastering lists and dictionaries in Python involves understanding their functionalities, properties, and common operations. Here's a comprehensive breakdown to get you started:

**Lists:**

* **Definition:** An ordered collection of items enclosed in square brackets `[]`. Elements can be of any data type, including other lists and dictionaries.
* **Creation:**
```python
my_list = [1, "hello", 3.14, [True, False]]
```
* **Accessing elements:** Use zero-based indexing starting from `[0]`. Negative indices access from the end (`[-1]` is the last element).
```python
first_element = my_list[0]  # first_element will be 1
last_element = my_list[-1]  # last_element will be [True, False]
```
* **Slicing:** Extract a sublist using colon (`:`) notation. `[start:end:step]`:
  * `start` (inclusive): index of the first element to include (defaults to 0).
  * `end` (exclusive): index of the element after the last element to include (defaults to the end of the list).
  * `step`: the difference between consecutive elements to include (defaults to 1).
```python
sublist = my_list[1:3]  # sublist will be ["hello", 3.14]
```
* **Common operations:**
  * `append(element)`: Add an element to the end of the list.
  * `insert(index, element)`: Insert an element at a specific index.
  * `remove(element)`: Remove the first occurrence of an element.
  * `pop(index)`: Remove and return the element at a specific index (or the last element by default).
  * `len(list)`: Get the length of the list (number of elements).
  * `sort()`: Sort the list in ascending order (modifies the original list).
  * `reversed()`: Return a reversed iterator for the list (doesn't modify the original list).

**Dictionaries:**

* **Definition:** An unordered collection of key-value pairs enclosed in curly braces `{}`. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be any data type.
* **Creation:**
```python
my_dict = {"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]}
```
* **Accessing elements:** Use the key enclosed in square brackets `[]` to access the corresponding value.
```python
name = my_dict["name"]  # name will be "Alice"
```
* **Common operations:**
  * `get(key, default)`: Get the value for a key, returning `default` if the key is not found.
  * `keys()`: Return a view of all keys in the dictionary.
  * `values()`: Return a view of all values in the dictionary.
  * `items()`: Return a view of all key-value pairs as tuples.
  * `in`: Check if a key exists in the dictionary.
  * `update(dict2)`: Update the dictionary with key-value pairs from another dictionary (`dict2`).
  * `pop(key, default)`: Remove the key-value pair and return the value, or `default` if the key is not found.
