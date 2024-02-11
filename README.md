# File Objects

https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

- [Read](#reading-a-file)
- [Write](#writing-to-a-file)

# Reading a file

```py
with open('test.txt', 'r') as f:
    # 'r' = readonly
    print(f.name)
    print(f.mode)

    f_contents = f.read()
    print(f_contents) # => prints out the content with the same formatting

print(f.closed) # => True
```

The `with` is the **Context Manager** that will automatically close the file.

## readline

```py
with open('test.txt', 'r') as f:
    # 'r' = readonly
    print(f.name)
    print(f.mode)

    f_contents = f.readline()
    print(f_contents)

    f_contents = f.readline()
    print(f_contents)

print(f.closed) # => True
```

**OUTPUT**

```bash
test.txt
r
1) This is a test file!

2) With multiple lines of data

True
```

```py
with open('test.txt', 'r') as f:
    # 'r' = read
    print(f.name)
    print(f.mode)

    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

print(f.closed) # => True
```

**OUTPUT**

```bash
test.txt
r
1) This is a test file!
2) With multiple lines of data
True
```

## for loop

```py
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
```

**Outputs the entire content**

## read

```py
with open('test.txt', 'r') as f:

    # f_contents = f.read() # => reads the entire content
    f_contents = f.read(100) # => specify size to read
    f_contents = f.read(100) # => will continue to read where it left of
    print(f_contents, end='')
```

## while loop using read

```py
with open('test.txt', 'r') as f:
    f.seek(10) # sets the position to start reading
    print(f.tell()) # tells the current position

    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read) # will return empty string at the last part, thus, 0 length
```

# Writing to a file

Creating a file

```py
with open('test2.txt', 'w') as f:
    pass
```

```py
# Creates a new file if it doesn't exist
# Else it will OVERRIDE the existing file
with open('test2.txt', 'w') as f:
    # w = writable
    f.write('Test')
    f.seek(0)
    f.write('R')
```

This will create OR override the `test2.txt` file with the following content:

```txt
Rest
```

## Read and Write to a file

### Copying a txt file

```py
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
```

### Copying an image file

Use `rb`/`wb` to read as **binary** file instead of reading as `utf-8` (text)

```py
with open('test.png', 'rb') as rf:
    with open('test_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
```

#### More example

```py
with open('assets/qr-code-cbr.svg', 'rb') as rf:
    with open('qr_copy2.svg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
```
