# Variable Scope

https://www.youtube.com/watch?v=QVdf0LgmICw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# LEGB

This is the order that Python determines what a variable is assigned to.

1. **Local** - defined within a function
2. **Enclosing** - variables within nested functions
3. **Global** - defined at top level of module or explicitly declared with the `global` keyword
4. **Built-in** - pre-assigned in Python

```py
x = 'global x'

def test():
    y = 'local y'
    print(y) # => local y

test()
print(x) # => global x
print(y) # ! ERROR !
```

## local variable within function with same variable name at global

```py
x = 'global x'

def test():
    x = 'local x'
    print(x) # => local x

test()
print(x) # => global x
```

## `global` keyword within a function

```py
x = 'global x'

def test():
    global x
    x = 'local x'
    print(x) # => local x

test()
print(x) # => local x
```

## Built-in variables

```py
import builtins

print(dir(builtins)) # => ... min ...

m = min([5, 1, 3])
print(m) # => 1
```

```py
import builtins

print(dir(builtins)) # => ... min ...

m = min([5, 1, 3])
print(m) # => 1
```

## Creating a function with same name with any built-in

```py
def min():
    pass

m = min([5, 1, 3]) # ! ERROR !
print(m)
```

## Nested function

```py
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x) # => inner x

    inner()
    print(x) # => outer x

outer()
```

## Enclosing Scope

```py
def outer():
    x = 'outer x'

    def inner():
        print(x) # => outer x

    inner()
    print(x) # => outer x

outer()
```

## `nonlocal` keyword

```py
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x) # => inner x

    inner()
    print(x) # => inner x

outer()
```
