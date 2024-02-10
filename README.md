# Loops and Iterations

https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

- [For loop](#for-loop)
- [While loop](#while-loop)

## For loop

```py
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
```

### break

```py
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

# => 1
# => 2
# => Found
```

### continue

```py
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

# => 1
# => 2
# => Found
# => 4
# => 5
```

## Nested For Loop

```py
for num in nums:
    for letter in 'abc':
        print(num, letter)

# => 1 a
# => 1 b
# => 1 c
# => 2 a
# => 2 b
# => 2 c
# => 3 a
# => 3 b
# => 3 c
# => 4 a
# => 4 b
# => 4 c
# => 5 a
# => 5 b
# => 5 c
```

### range

```py
for i in range(10):
    print(i) # Prints 0 - 9

for i in range(1, 11):
    print(i) # Prints 1 - 10
```

## While loop

```py
x = 0

while x < 10:
    print(x) # prints 0 - 9
    x += 1
```

### break

```py
x = 0

while x < 10:
    if x == 5:
        break
    print(x) # prints 0 - 4
    x += 1
```

# Infinite loop

In most system, press `Ctrl + C` in your terminal
