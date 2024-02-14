from functools import wraps

# * Decorator my_logger
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args: {args} and kwargs: {kwargs}'
        )
        return orig_func(*args, **kwargs)
    
    return wrapper

# * Decorator my_timer
def my_timer(orig_func):
    import time as t

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = t.time()
        result = orig_func(*args, **kwargs)
        t2 = t.time() - t1
        
        print(f'{orig_func.__name__} ran in {t2} sec')

        return result
    
    return wrapper

import time

@my_logger    
@my_timer
def display_info(name, age):
    time.sleep(1) # sleep 1 second
    print(f'display_info with {name} and {age}')

display_info('John', 25)
