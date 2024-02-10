courses = ['History', 'Math', 'Physics', 'CompSci']

# print(courses) # => ['History', 'Math', 'Physics', 'CompSci']
# print(len(courses)) # => 4
# print(courses[0]) # => History
# print(courses[-1]) # => CompSci
# print(courses[-2]) # => Physics
# print(courses[0:2]) # => ['History', 'Math'] // slicing
# print(courses[2:]) # => ['Physics', 'CompSci'] // slicing
# print(courses.index('CompSci')) # => 3
# print(courses.index('Art')) # ERROR
# print('Art' in courses) # => False

# courses.append('Art')
# print(courses) # => ['History', 'Math', 'Physics', 'CompSci', 'Art']

# courses.insert(0, 'Art')
# print(courses) # => ['Art', 'History', 'Math', 'Physics', 'CompSci']

# courses_2 = ['Art', 'Education']
# courses.insert(0, courses_2)
# print(courses) # => [['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci']
# print(courses[0]) # => ['Art', 'Education']

# courses_2 = ['Art', 'Education']
# courses.extend(courses_2)
# print(courses) # => ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']
# print(courses[0]) # => History

# courses.remove('Math')
# print(courses) # => ['History', 'Physics', 'CompSci']

# popped = courses.pop()
# print(popped) # => CompSci
# print(courses) # => ['History', 'Math', 'Physics']

# courses.reverse()
# print(courses) # => ['CompSci', 'Physics', 'Math', 'History']

# courses.sort()
# print(courses) # => ['CompSci', 'History', 'Math', 'Physics']

# * Sort Ascending
nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums) # => [1, 2, 3, 4, 5]

# * Sort Descending
# courses.sort(reverse=True)
nums.sort(reverse=True)
print(nums) # => [5, 4, 3, 2, 1]
# print(courses) # => ['Physics', 'Math', 'History', 'CompSci']

ascending = sorted(courses)
descending = sorted(courses, reverse=True)
print(courses) # => ['History', 'Math', 'Physics', 'CompSci']
print(ascending) # => ['CompSci', 'History', 'Math', 'Physics']
print(descending) # => ['Physics', 'Math', 'History', 'CompSci']

print(min(nums)) # => 1
print(max(nums)) # => 5
print(sum(nums)) # => 15

for item in courses:
    print(item)
# => History
# => Math
# => Physics
# => CompSci

for index, item in enumerate(courses):
    print(index, item)
# => 0 History
# => 1 Math
# => 2 Physics
# => 3 CompSci

for index, item in enumerate(courses, start=1):
    print(index, item)
# => 1 History
# => 2 Math
# => 3 Physics
# => 4 CompSci

courses_str = ', '.join(courses)
print(courses_str) # => History, Math, Physics, CompSci

courses_str = ' -- '.join(courses)
print(courses_str) # => History -- Math -- Physics -- CompSci

new_list = courses_str.split(' -- ')
print(new_list) # => ['History', 'Math', 'Physics', 'CompSci']

# * Mutable (uses square brackets)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1) # => ['History', 'Math', 'Physics', 'CompSci']
print(list_2) # => ['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Art'

print(list_1) # => ['Art', 'Math', 'Physics', 'CompSci']
print(list_2) # => ['Art', 'Math', 'Physics', 'CompSci']

# * Immutable (uses parenthesis)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1) # => ('History', 'Math', 'Physics', 'CompSci')
print(tuple_2) # => ('History', 'Math', 'Physics', 'CompSci')

# tuple_1[0] = 'Art' # ! ERROR -- TypeError: 'tuple' object does not support item assignment

# * Sets

courses_set = {'History', 'Math', 'Physics', 'CompSci'}
# Order will always change for each run since **SETS** are unordered
print(courses_set) # => {'Math', 'Physics', 'History', 'CompSci'}

courses_set = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# Sets removes duplicates
print(courses_set) # => {'Math', 'History', 'Physics', 'CompSci'}

print('Math' in courses_set) # => True
print('Art' in courses_set) # => False

# * Set Comparison

set_com = {'History', 'Math', 'Physics', 'CompSci'}
set_art = {'History', 'Math', 'Art', 'Design'}

print(set_com.intersection(set_art)) # => {'Math', 'History'}
print(set_com.difference(set_art)) # => {'Physics', 'CompSci'}
print(set_com.union(set_art)) # => {'Design', 'CompSci', 'Art', 'Physics', 'History', 'Math'}


# Empty Lists
empty_list = []
empty_list = list()


# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()


# Empty Sets
empty_set = {} # INCORRECT.. It's an empty **DICTIONARY**
empty_set = set()
