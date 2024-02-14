# Learn Decorator with Arguments

https://www.youtube.com/watch?v=KlBPCzcQNU8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# Prerequisite

[Learn Decorators](https://github.com/lightzane/learn-python/tree/l-decorators?tab=readme-ov-file#learn-decorators)

# Decorators Review

```py
from functools import wraps

def decorator_function(orig_func):

    @wraps(orig_func)
    def wrapper_function(*args, **kwargs):
        print(f'Executing... {orig_func.__name__}')
        result = orig_func(*args, **kwargs)
        print(f'After executing {orig_func.__name__}()', '\n')

        return result

    return wrapper_function

@decorator_function
def display_info(name: str, age: int):
    print(f'display_info with arguments {name} and {age}')

display_info('John', 25)

# => Executing... display_info
# => display_info with arguments John and 25
# => After executing display_info()
```

# Decorator with Function

```diff
from functools import wraps

+def prefix_decorator(prefix: str):
    def decorator_function(orig_func):

        @wraps(orig_func)
        def wrapper_function(*args, **kwargs):
            print(prefix, f'Executing... {orig_func.__name__}')
            result = orig_func(*args, **kwargs)
            print(prefix, f'After executing {orig_func.__name__}()', '\n')

            return result

        return wrapper_function
+   return decorator_function

+@prefix_decorator('PREFIX:')
def display_info(name: str, age: int):
    print(f'display_info with arguments {name} and {age}')

display_info('John', 25)

# => PREFIX: Executing... display_info
# => display_info with arguments John and 25
# => PREFIX: After executing display_info()
```
