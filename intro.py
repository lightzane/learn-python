# File Objects

# * Recommended to use "Context Manager" - `with`
with open('test.txt', 'r') as f:
    # 'r' = readonly

    # print(f.name)
    # print(f.mode)

    # f_contents = f.readline()
    # print(f_contents, end='')

    # f_contents = f.readline()
    # print(f_contents, end='')

    # for line in f:
    #     print(line, end='')

    # f_contents = f.read(100)
    # print(f_contents, end='')

    f.seek(10) # sets the position to start reading

    size_to_read = 100

    print(f.tell()) # tells the current position

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read) # will return empty string at the last part, thus, 0 length

print(f.closed) # => True

# * Writing to a File
# Creates a new file if it doesn't exist
# ! Else it will OVERRIDE the existing file
# with open('test2.txt', 'w') as f:
#     # w = writable
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# * Read and Write to a text file
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# * Read and Write to a binary file
with open('assets/qr-code-cbr.svg', 'rb') as rf:
    with open('qr_copy.svg', 'wb') as wf:
        for line in rf:
            wf.write(line)

# More example
with open('assets/qr-code-cbr.svg', 'rb') as rf:
    with open('qr_copy2.svg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

# ! Not Recommended (without context manager `with`)
# f = open('test.txt', 'r') # 'r' - read

# print(f.name) # => test.txt
# print(f.mode) # => r

# f.close() # ! Never forget to close the file