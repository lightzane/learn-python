from functools import wraps

def prefix_decorator(prefix: str):
    def decorator_function(orig_func):
        
        @wraps(orig_func)
        def wrapper_function(*args, **kwargs):
            print(prefix, f'Executing... {orig_func.__name__}')
            result = orig_func(*args, **kwargs)
            print(prefix, f'After executing {orig_func.__name__}()', '\n')

            return result
        
        return wrapper_function
    return decorator_function

@prefix_decorator('PREFIX:')
def display_info(name: str, age: int):
    print(f'display_info with arguments {name} and {age}')

display_info('John', 25)
display_info('IU', 25)
