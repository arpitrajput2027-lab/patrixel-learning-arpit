# Python Revision Notes — 18 November 2026

Short revision notes based on today's Python practice and discussion.

## 1. Python Basics and Data Types
- Python uses indentation to define blocks.
- Common types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, `dict`.
- `type(value)` checks a value's type; `int("5")` converts a numeric string to an integer.

```python
name = "Arpit"
age = 21
print(type(age))  # <class 'int'>
```

## 2. Loops and Functions
- `for` iterates over a sequence; `while` repeats while a condition is true.
- Use `def` for reusable functions and `return` to produce a result.
- Local variables are scoped to a function; global variables are defined at module level.
- Lambda is a short anonymous function; `map()` transforms and `filter()` selects elements.

```python
def add(a, b):
    return a + b

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

## 3. File Handling
- `r`: read, `w`: write (creates/truncates), `a`: append; `t`: text mode.
- `with open(...)` automatically closes the file when exiting its block.
- `FileNotFoundError` is raised when reading a missing file.
- A write-only file cannot be read: `io.UnsupportedOperation`.

```python
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
```

## 4. OOP Quick Revision
- A class defines a blueprint; an object is an instance.
- `__init__()` initializes an object's attributes; `self` refers to the instance.

```python
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Arpit")
print(student.name)
```

## 5. Modules, Packages, Aliases and pip
- **Module:** a Python file, such as `math_utils.py`.
- **Package:** a way to organize related modules, often a folder with `__init__.py`.
- **Alias:** alternative import name, such as `import math as m`.
- **Standard library:** includes `math`, `datetime`, `io`.
- `pip` installs third-party Python packages, e.g. `python -m pip install requests`.
- Normal `import` statements cannot reference module names starting with digits.

```python
from datetime import date as dt
print(dt(2008, 9, 1))  # year, month, day

from utils.math_utils import add  # package.module -> function
```

## 6. `__name__` and `__init__.py`
- A directly executed module has `__name__ == "__main__"`.
- An imported module usually has its module name as `__name__`.
- `__init__.py` initializes a regular package and can expose imports.

```python
if __name__ == "__main__":
    print("Run directly")
```

## 7. Exception Handling
- `try`: code that might fail.
- `except`: handle a specific exception.
- `else`: runs when `try` completes without an exception.
- `finally`: normally runs regardless of success/failure, useful for cleanup.
- Common exceptions practiced: `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `io.UnsupportedOperation`.
- `except ValueError as err` makes the exception available as `err`.

```python
try:
    result = int("10") / int("2")
except (ValueError, ZeroDivisionError) as err:
    print("Error:", err)
else:
    print("Result:", result)
finally:
    print("Finished")
```

