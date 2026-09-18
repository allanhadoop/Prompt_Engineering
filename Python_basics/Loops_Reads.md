# Types of FOR loop - 
| Syntax                           | What it means in simple English                 | When to use                            |
| -------------------------------- | ----------------------------------------------- | -------------------------------------- |
| `for x in list`                  | Take each item from the list, one at a time     | You already have a list of things      |
| `for x in range(5)`              | Repeat 5 times, using numbers 0–4               | You need repetition/counting           |
| `for x in range(2, 5)`           | Take numbers 2, 3, 4                            | You need a specific number range       |
| `for x in range(2, 10, 2)`       | Take 2, 4, 6, 8                                 | You need a step/jump                   |
| `for i, x in enumerate(list)`    | Give me the item's position AND the item        | You need index + value                 |
| `for x in dictionary`            | Give me each dictionary key                     | You only need keys                     |
| `for x in dictionary.values()`   | Give me each dictionary value                   | You only need values                   |
| `for k, v in dictionary.items()` | Give me key AND value                           | You need both                          |
| `for a, b in zip(list1, list2)`  | Take one item from each list together           | You have matching lists                |
| `for x in reversed(list)`        | Start from the last item and go backwards       | You need reverse order                 |
| `for x in sorted(list)`          | Give items in sorted order                      | You need sorted order                  |
| `for _ in range(5)`              | Repeat 5 times; I don't need the counter        | You only want repetition               |
| Nested `for`                     | Run one loop inside another loop                | You need combinations / rows & columns |
| `continue`                       | Skip this item                                  | You want to ignore something           |
| `break`                          | Stop the loop completely                        | You found what you need                |
| `for ... else`                   | Run `else` if the loop finishes without `break` | Searching                              |
| List comprehension               | Short way to create a list using `for`          | Creating a new list                    |
| `async for`                      | Loop through asynchronous data                  | Advanced async programming             |

------------------------------------------------------------------------------------------------------------------------------
# How to read/access data —
| Data type                    | Example            | How to read     | Simple meaning               |
| ---------------------------- | ------------------ | --------------- | ---------------------------- |
| **Dictionary / JSON object** | `{"name": "Adam"}` | `data["name"]`  | Get value using key          |
| **List**                     | `["Adam", "John"]` | `data[0]`       | Get item using position      |
| **Tuple**                    | `("Adam", 20)`     | `data[0]`       | Get item using position      |
| **String**                   | `"Adam"`           | `data[0]`       | Get character using position |
| **Set**                      | `{"Adam", "John"}` | `for x in data` | Loop through values          |
| **Dictionary value**         | `{"age": 20}`      | `data.values()` | Get values                   |
| **Dictionary key**           | `{"age": 20}`      | `data.keys()`   | Get keys                     |
| **Dictionary key + value**   | `{"age": 20}`      | `data.items()`  | Get both                     |

-------------------------------------------------------------------------------------------------------------------------------
| Mechanism       | Simple meaning                     | Example                     |
| --------------- | ---------------------------------- | --------------------------- |
| Variable        | Give a value a name                | `name = "Adam"`             |
| Object          | A thing/value Python works with    | `"Adam"`, `[1,2]`, `person` |
| Attribute       | Information belonging to an object | `person.name`               |
| Method          | Function belonging to an object    | `name.upper()`              |
| Function        | Reusable piece of code             | `len(name)`                 |
| Parameter       | Input a function expects           | `def add(x, y)`             |
| Argument        | Actual value given to function     | `add(10, 20)`               |
| Return          | Send result back                   | `return result`             |
| Class           | Blueprint for objects              | `class Patient:`            |
| Instance        | Object created from class          | `patient1 = Patient()`      |
| Constructor     | Sets up a new object               | `__init__()`                |
| `self`          | Current object                     | `self.name`                 |
| Inheritance     | Child class gets parent features   | `class Dog(Animal)`         |
| Module          | Python file containing code        | `import math`               |
| Package         | Collection of modules              | `import numpy`              |
| Exception       | Error that can be handled          | `ValueError`                |
| `try/except`    | Handle an error                    | `try: ... except:`          |
| Lambda          | Small one-line function            | `lambda x: x * 2`           |
| `*args`         | Multiple positional inputs         | `def f(*args)`              |
| `**kwargs`      | Multiple named inputs              | `def f(**kwargs)`           |
| Generator       | Produces values one at a time      | `yield x`                   |
| Iterator        | Object that gives next item        | `next(iterator)`            |
| Decorator       | Modifies a function                | `@decorator`                |
| Context manager | Automatically manages resources    | `with open(...)`            |
| Async           | Work without blocking              | `async def` / `await`       |
