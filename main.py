try:
    f = open('found.txt')
    raise Exception('Custom error')
    # var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e: # Other exceptions
    print(e) # => name 'bad_var' is not defined
else:
    # Executes ONLY when `try` block did NOT throw any error
    print(f.read())
    f.close()
finally:
    # Executes regardless `try` block threw an error or not
    print('Closing')

