# Learn Decorators

Alter the functionality of your **Functions**

https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# Contents

- [Review `*args` and `**kwargs`](#review-about-args-and-kwargs)
- [Getting Started](#getting-started)
- [Creating a decorator function](#decorator)
- [Define a Decorator Function](#using-the--symbol)
  - [Decorating a function that has arguments](#decorating-a-function-with-arguments)
- [Define a Decorator Class](#decorator-class)
- [More examples](#more-examples) (Decorator Function)
  - [Logger Decorator](#logger-example)
  - [Timer Decorator](#timer-example)
- [Stacked Decorators](#stacked-decorators)

# Review about `*args` and `**kwargs`

```py
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test('lemon', 'orange', one=1, two=2)
# args => ('lemon', 'orange')
# kwargs => {'one': 1, 'two': 2}
```

## Getting Started

Function as a closure

```py
def outer_function(msg):

    def inner_function():
        print(msg)

    return inner_function

my_func = outer_function('Hello World')
new_world = outer_function('A whole new world')

my_func() # => Hello World
new_world() # => A whole new world
```

# Decorator

- A function that takes another **function as an argument** and **returns another function** without altering the source code that we passed in.
- Executes a function that is passed in

```py
def decorator_function(original_function):

    def wrapper_function():
        # Put any side quests here...
        return original_function()

    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display() # => display function ran
```

## Using the `@` symbol

```py
def decorator_function(original_function):

    def wrapper_function():
        print(f'Executing function: {original_function.__name__}')
        return original_function()

    return wrapper_function

@decorator_function # shorter syntax for: decorated_display = decorator_function(display)
def display():
    print('display function ran')

display()
# => Executing function: display_2
# => display function ran
```

### Decorating a function with arguments

```py
@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

# ! Will throw error when *args and **kwargs not defined in wrapper function of the decorator
display_info('John', 25) # ! ERROR ! .wrapper_function() takes 0 positional arguments but 2 were given
```

This will throw an error since our `decorator` will call the `original_function()` without passing any arguments.

#### Solution is to add `*args` and `**kwargs` in your `wrapper_function()`

```py
def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print(f'Executing function: {original_function.__name__}')
        return original_function(*args, **kwargs)

    return wrapper_function

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('John', 25)
# => Executing function: display_info
# => display_info ran with arguments (John, 25)
```

# Decorator Class

```py
class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    # Calls self as a function
    def __call__(self, *args, **kwargs):
        print(f'__call__ method of Decorator Class executes: {self.original_function.__name__}()')
        return self.original_function(*args, **kwargs)

@DecoratorClass
def other_info(name, age):
    print(f'other_info is called with ({name}, {age})')

other_info('IU', 25)
# => __call__ method of Decorator Class executes: other_info()
# => other_info is called with (IU, 25)
```

# More Examples

## Logger Example

```py
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args: {args} and kwargs: {kwargs}'
        )
        return orig_func(*args, **kwargs)

    return wrapper
```

### Logger Usage

```py
@my_logger
def display_info(name, age):
    print(f'display_info with {name} and {age}')

display_info('John', 25)
display_info('John', 25, super=True)
```

Based on function name `display_info`, it will generate a file `display_info.log` with content:

```log
INFO:root:Ran with args: ('John', 25) and kwargs: {}
INFO:root:Ran with args: ('John', 25) and kwargs: {'super': True}
```

## Timer Example

```py
def my_timer(orig_func):
    import time as t

    def wrapper(*args, **kwargs):
        t1 = t.time()
        result = orig_func(*args, **kwargs)
        t2 = t.time() - t1

        print(f'{orig_func.__name__} ran in {t2} sec')

        return result

    return wrapper
```

### Timer Usage

```py
import time

@my_timer
def display_info(name, age):
    time.sleep(1) # sleep 1 second
    print(f'display_info with {name} and {age}')

display_info('John', 25)
# => display_info with John and 25
# => display_info ran in 1.001845359802246 sec
```

# Stacked Decorators

```py
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1) # sleep 1 second
    print(f'display_info with {name} and {age}')
```

If we stack two decorators, it will execute like this:

```py
decorated_display_info = my_logger(my_timer(display_info))
```

**PROBLEM**

In this approach, the `my_logger` will actually call the `wrapper` of `my_timer` and vice-versa when we switch the order of decorators.

## How to preserve the information of our `orig_func` for both decorators?

By using the `functools.wraps` from Python standard library.

```diff
+from functools import wraps

 def my_logger(orig_func):
     ...
+    @wraps(orig_func)
     def wrapper(*args, **kwargs):
         ...

 def my_timer(orig_func):
     ...
+    @wraps(orig_func)
     def wrapper(*args, **kwargs):
         ...
```
