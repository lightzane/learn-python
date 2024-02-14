
# * Passing function as an argument
# def square(x):
#     return x * x

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(square, [1, 2, 3, 4, 5])

# print(squares) # => [1, 4, 9, 16, 25]

# * Returning function from a function
# def logger(msg):

#     def log_message():
#         print('Log:', msg)

#     return log_message

# log_hi = logger('Hi!')
# log_hi() # => Log: Hi!

# Another example
def html_tag(tag):

    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test headline!') # => <h1>Test headline!</h1>
print_h1('Another Headline') # => <h1>Another Headline</h1>

print_p = html_tag('p')
print_p('Test Paragraph!') # => <p>Test Paragraph!</p>