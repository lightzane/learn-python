# Decorators

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test('lemon', 'orange', one=1, two=2)
# args => ('lemon', 'orange')
# kwargs => {'one': 1, 'two': 2}

def outer_function(msg):

    def inner_function():
        print(msg)
    
    return inner_function

my_func = outer_function('Hello World') 
new_world = outer_function('A whole new world')

my_func() # => Hello World
new_world() # => A whole new world


def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print(f'Executing function: {original_function.__name__}')
        return original_function(*args, **kwargs)
    
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display() # => display function ran

@decorator_function # shorter syntax for: decorated_display = decorator_function(display)
def display_2():
    print('display v2 function ran')

display_2() 
# => Executing function: display_2
# => display v2 function ran

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('John', 25) # ! Will throw error when *args and **kwargs not defined in wrapper function of the decorator
# => Executing function: display_info
# => display_info ran with arguments (John, 25)

# * Decorator Class

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