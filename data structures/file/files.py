
import os

# where currently we are in?
print(os.listdir('.'))
# change directory to the following path to see the folder we are working in
os.chdir('./data structures/file')
print(os.listdir('.'))

f = open('test.txt')

# return all content of the file as a string

print(f.read())

# file no longer there because cursor stopped in the end first time we read file
print(f.read())

# change cursor place to the begining of the file using cursor method
f.seek(0)

# map a file content into a list of lines
print(f.readlines())


# colse file to let other programs can use it.

with open('test2.txt', mode='r') as my_new_file:
    content = my_new_file.read()
    print(content)

# modes are w+ a r w
