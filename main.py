'''
LEGB
Local, Enclosing, Global, Built-in
'''
# import builtins
# print(dir(builtins))

# def min():
#     pass

# m = min([5, 1, 3])
# print(m) # => 1

x = 'global x'

def test():
    global x
    x = 'local x'
    print(x) # => local x

test()
print(x) # => local x

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x) # => inner x
    
    inner()
    print(x) # => outer x

outer()

def outer_non_local():
    x = 'outer non local x'

    def inner():
        nonlocal x
        x = 'inner non local x'
        print(x) # => inner non local x
    
    inner()
    print(x) # => inner non local x

outer_non_local()