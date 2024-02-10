# Lists, Tuples and Sets

https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

[`Lists`](#lists) and [`Tuples`](#tuples)

- ordered list (sequential data)
- allows duplicates

[`Sets`](#sets)

- unordered list
- NOT allowed duplicates

## Lists

[**Mutable**](#lists-are-mutable) and sequential list

```py
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses) # => ['History', 'Math', 'Physics', 'CompSci']
print(len(courses)) # => 4
print(courses[0]) # => History
print(courses[-1]) # => CompSci
print(courses[-2]) # => Physics
print(courses[0:2]) # => ['History', 'Math'] // slicing
print(courses[2:]) # => ['Physics', 'CompSci'] // slicing
print(courses.index('CompSci')) # => 3
print(courses.index('Art')) # ERROR
print('Art' in courses) # => False
print('Math' in courses) # => True
```

### List.append()

`print(help(list.append))`:

- `append(self, object, /)` Append object to the end of the list.

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.append('Art')
print(courses) # => ['History', 'Math', 'Physics', 'CompSci', 'Art']
```

### List.insert()

`print(help(list.insert))`:

- `insert(self, index, object, /)` - Insert object before index.

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0, 'Art')
print(courses) # => ['Art', 'History', 'Math', 'Physics', 'CompSci']
```

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses) # => [['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci']
print(courses[0]) # => ['Art', 'Education']
```

### List.extend()

`print(help(list.extend))`:

- `extend(self, iterable, /)` - Extend list by appending elements from the iterable.

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses) # => ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']
print(courses[0]) # => History
```

### List.remove()

Remove first occurrence of value.

Raises ValueError if the value is not present.

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses) # => ['History', 'Physics', 'CompSci']
```

### List.pop()

Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
popped = courses.pop()
print(popped) # => CompSci
print(courses) # => ['History', 'Math', 'Physics']
```

### List.reverse()

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()

print(courses) # => ['CompSci', 'Physics', 'Math', 'History']
```

### List.sort()

`print(help(list.sort))`:

- `sort(self, /, *, key=None, reverse=False)`

Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them,
ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()
print(courses) # => ['CompSci', 'History', 'Math', 'Physics']
```

#### Sort Ascending

```py
nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums) # => [1, 2, 3, 4, 5]
```

#### Sort Descending

```py
nums = [1, 5, 2, 4, 3]
nums.sort(reverse=True)
print(nums) # => [5, 4, 3, 2, 1]

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort(reverse=True)
print(courses) # => ['Physics', 'Math', 'History', 'CompSci']
```

#### sorted()

`print(help(sorted))`:

- `sorted(iterable, /, *, key=None, reverse=False)`

Return a **NEW** list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
ascending = sorted(courses)
descending = sorted(courses, reverse=True)

print(courses) # => ['History', 'Math', 'Physics', 'CompSci']
print(ascending) # => ['CompSci', 'History', 'Math', 'Physics']
print(descending) # => ['Physics', 'Math', 'History', 'CompSci']
```

#### min(), max() and sum()

```py
nums = [1, 5, 2, 4, 3]
print(min(nums)) # => 1
print(max(nums)) # => 5
print(sum(nums)) # => 15
```

### Looping in List

```py
courses = ['History', 'Math', 'Physics', 'CompSci']

for item in courses:
    print(item)

# => History
# => Math
# => Physics
# => CompSci
```

```py
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, item in enumerate(courses):
    print(index, item)
# => 0 History
# => 1 Math
# => 2 Physics
# => 3 CompSci
```

```py
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, item in enumerate(courses, start=1):
    print(index, item)
# => 1 History
# => 2 Math
# => 3 Physics
# => 4 CompSci
```

### join() and split()

`join()` - joining list into strings
`split()` - spliting strings to list

```py
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ', '.join(courses)

print(courses_str) # => History, Math, Physics, CompSci

courses_str = ' -- '.join(courses)
print(courses_str) # => History -- Math -- Physics -- CompSci

new_list = courses_str.split(' -- ')
print(new_list) # => ['History', 'Math', 'Physics', 'CompSci']
```

### Lists are mutable

```py
# * Mutable (uses square brackets)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1) # => ['History', 'Math', 'Physics', 'CompSci']
print(list_2) # => ['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Art'

print(list_1) # => ['Art', 'Math', 'Physics', 'CompSci']
print(list_2) # => ['Art', 'Math', 'Physics', 'CompSci']
```

## Tuples

**IMMUTABLE** and **non**-sequential list

Similar to [lists](#lists) but we **CANNOT MODIFY** tuples

```py
# * Immutable (uses parenthesis)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1) # => ('History', 'Math', 'Physics', 'CompSci')
print(tuple_2) # => ('History', 'Math', 'Physics', 'CompSci')

tuple_1[0] = 'Art' # ! ERROR -- TypeError: 'tuple' object does not support item assignment
```

## Sets

**Unordered** and **has NO duplicates**

Sets do **membership tests** and **comparison** more efficiently than lists and tuples.

```py
courses_set = {'History', 'Math', 'Physics', 'CompSci'}
# Order will always change for each run since **SETS** are unordered
print(courses_set) # => {'Math', 'Physics', 'History', 'CompSci'}

courses_set = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# Sets removes duplicates
print(courses_set) # => {'Math', 'History', 'Physics', 'CompSci'}
```

### Membership Test

```py
print('Math' in courses_set) # => True
print('Art' in courses_set) # => False
```

### Set comparison

```py
set_com = {'History', 'Math', 'Physics', 'CompSci'}
set_art = {'History', 'Math', 'Art', 'Design'}

print(set_com.intersection(set_art)) # => {'Math', 'History'}
print(set_com.difference(set_art)) # => {'Physics', 'CompSci'}
print(set_com.union(set_art)) # => {'Design', 'CompSci', 'Art', 'Physics', 'History', 'Math'}
```

# Empty List, Tuple and Set

```py
# Empty Lists
empty_list = []
empty_list = list()


# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()


# Empty Sets
empty_set = {} # INCORRECT.. It's an empty **DICTIONARY**
empty_set = set()
```

See [05/dictionaries](https://github.com/lightzane/learn-python/tree/05/dictionaries)
