# Learn Error Handling

https://www.youtube.com/watch?v=NIWwJbo-9_8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

## Try / Except Blocks template

```py
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
```

## Testing Errors

```py
f = open('notfound.txt')
```

**Error received**:

```bash
Traceback (most recent call last):
  File "path\to\main.py", line 1, in <module>
    f = open('notfound.txt')
        ^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'notfound.txt'
```

## Wrap with Try / Except block

```py
try:
    f = open('notfound.txt')
except Exception: # General exception
    print('Sorry. This file does not exist')
```

**Output received**

```bash
Sorry. This file does not exist
```

## Specifying exception

```py
try:
    f = open('found.txt') # the file now exist
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
```

But even if we have the `except` block, we're still getting an unhandled exception, since it's a new exception which is `NameError`:

```bash
Traceback (most recent call last):
  File "path\to\main.py", line 3, in <module>
    var = bad_var
          ^^^^^^^
NameError: name 'bad_var' is not define
```

## Add another `except` block

```py
try:
    f = open('found.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except NameError:
    print('You have bad variable')
```

## Unexpected error

Almost all the time, you may not know exactly the error is:

```py
try:
    f = open('found.txt')
    var = bad_var
except FileNotFoundError as e:
    print('Sorry. This file does not exist', e)
except Exception as e: # Other exceptions
    print(e) # => name 'bad_var' is not defined
```

## `else` block

```py
try:
    f = open('found.txt')
except Exception as e: # Other exceptions
    print(e) # => name 'bad_var' is not defined
else:
    # Executes ONLY when `try` block did NOT throw any error
    print(f.read())
    f.close()
```

## `finally` block

```py
try:
    f = open('not-found.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    # Executes regardless `try` block threw an error or not
    print('Closing')
```

## Manually raise an exception

You can manually throw an exception

```py
try:
    f = open('found.txt')
    raise Exception('Custom error')
except Exception as e:
    print(e) # => Custom error
```
