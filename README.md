# Strings

https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

```py
# Print Welcome Message
print('Hello World')

message1 = 'Hello "John"'
message2 = "Hello 'John'"

print(message1) # => Hello "John"
print(message2) # => Hello 'John'
```

Can use `single` or `double` quotes to wrap strings.

```py
# Print Welcome Message
message = 'Hello World'
print(len(message)) # => 11
print(message[0]) # => H
print(message[10]) # => d
print(message[0:5]) # => Hello
print(message[:5]) # => Hello
print(message[6:]) # => World
print(message.upper()) # => HELLO WORLD
print(message.count('l')) # => 3 // total of 3 "l" letters
print(message.find('World')) # => 6 // starts at 6th index
print(message.find('Universe')) # => -1

new_message = message.replace('World', 'Universe')
print(new_message) # => Hello Universe
```

## String concatenation

```py
greeting = 'Hello'
name = 'John'

message = greeting + ', ' + name + '. Welcome'
print(message) # => Hello, John. Welcome
```

## Formatted string

`>= Python 3.6`

```py
greeting = 'Hello'
name = 'John'

message = f'{greeting}, {name}. Welcome' # for Python >= 3.6
print(message) # => Hello, John. Welcome
```

`<= Python 3.5`

```py
greeting = 'Hello'
name = 'John'

message = '{}, {}. Welcome'.format(greeting, name) # for Python <= 3.5
print(message) # => Hello, John. Welcome
```

# dir() and Help documentations

You can check all the available properties or methods

```py
name = 'John'
print(dir(name)) # => ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

```py
print(help(str)) # => Help on class str in module builtins:
# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.
```

```py
print(help(str.lower)) # => Help on method_descriptor:
# lower(self, /)
#     Return a copy of the string converted to lowercase.
```
