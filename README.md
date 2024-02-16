# Learn Python Typing

Type Hints & Annotations

https://www.youtube.com/watch?v=QORvB-_mbZ0

Python documentation: https://docs.python.org/3/library/typing.html <br>
_New in version 3.5_

## Installation

```bash
pip install mypy
```

Add type annotations to your Python programs, and use mypy to type check them. Mypy is essentially a Python linter. (https://pypi.org/project/mypy/)

**Notice that mypy is already included in [.gitignore](./.gitignore)**

```properties
# mypy
.mypy_cache/
.dmypy.json
dmypy.json
```

## Usage

```py
# main.py

x: str = 1 # Line 1
```

Run command `mypy` in terminal

```bash
mypy main.py
```

```bash
main.py:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```

### More examples

```py
def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c

add_numbers('1', '2', '3') # Line 6
```

```bash
main.py:6: error: Argument 1 to "add_numbers" has incompatible type "str"; expected "int"  [arg-type]
main.py:6: error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"  [arg-type]
main.py:6: error: Argument 3 to "add_numbers" has incompatible type "str"; expected "int"  [arg-type]
Found 3 errors in 1 file (checked 1 source file)
```

```py
# Correct
from typing import Optional

def foo(output: Optional[bool]=False):
    pass

def bar(output: bool=False):
    pass

# Correct
z: tuple[int, int, int] = (1, 2, 3)
```

```py
# Incorrect

def fu(x: int, y: int) -> int:
    return x + y

def kung(func: Callable[[], int]) -> None:
    func(1, 2) # Line 25

kung(fu('fighting')) # Line 27
```

```bash
main.py:25: error: Too many arguments  [call-arg]
main.py:27: error: Missing positional argument "y" in call to "fu"  [call-arg]
main.py:27: error: Argument 1 to "kung" has incompatible type "int"; expected "Callable[[], int]"  [arg-type]
main.py:27: error: Argument 1 to "fu" has incompatible type "str"; expected "int"  [arg-type]
Found 4 errors in 1 file (checked 1 source file)
```

What is this `main.py:25: error: Too many arguments  [call-arg]`?

**Line 25**: We are passing 2 arguments (`1`, `2`) but the `Callable[[], int]` is not accepting any argument.

#### Fix Line 25

```py
def fu(x: int, y: int) -> int:
    return x + y

def kung(func: Callable[[int, int], int]) -> None:
    func(1, 2)

kung(fu('fighting')) # Line 27 still incorrect
```

`Callable[[int, int], int]` = `func(int, int) -> int`

- `Callable` first argument - defines the number of arguments in the function
- `Callable` second argument - defines the return type of the function

**Remaining errors**

```bash
main.py:27: error: Missing positional argument "y" in call to "fu"  [call-arg]
main.py:27: error: Argument 1 to "kung" has incompatible type "int"; expected "Callable[[int, int], int]"  [arg-type]
main.py:27: error: Argument 1 to "fu" has incompatible type "str"; expected "int"  [arg-type]
Found 3 errors in 1 file (checked 1 source file)
```

- We have Line 27: `kung(fu('fighting'))`

```bash
main.py:27: error: Missing positional argument "y" in call to "fu"  [call-arg]
```

`fu(x: int, y: int) -> int` - accepts 2 arguments, but we only passed `x` argument which is `'figthing'`

```bash
main.py:27: error: Argument 1 to "kung" has incompatible type "int"; expected "Callable[[int, int], int]"  [arg-type]
```

`fu(...) -> int` - returns an `int`, therefore, imagine passing a number like so: `kung(5)`

But `kung`'s argument is expecting a function `Callable[[int, int], int]` that accepts 2 `int` arguments that returns an `int` type value

```bash
main.py:27: error: Argument 1 to "fu" has incompatible type "str"; expected "int"  [arg-type]
Found 3 errors in 1 file (checked 1 source file)
```

We have passed a `str` argument to `fu('fighting')` but we defined `fu(x: int, y: int)` to accept 2 `int` arguments.

```py
# Correct

def fu(x: int, y: int) -> int:
    return x + y

def kung(func: Callable[[int, int], int]) -> None:
    func(1, 2)

kung(fu)
```

### Generics

```py
# Correct

from typing import TypeVar

T = TypeVar('T')

def get_items(arr_list: list[T], index: int) -> T:
    return arr_list[index]

lemon = get_items(['lemon', 'orange'], 0)
print(lemon)

mixed = get_items(['lemon', 1, True], 2)
print(mixed)
```
