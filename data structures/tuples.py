
# tuples are immutable

t = (1, 2, 3)
myList = [1, 2, 3]

print(type(t))
print(type(myList))

t2 = ('one', 2)

# count method returns how many times a value in tuple

t3 = ('a', 'b', 'c', 'a')

print(t3.count('a'))

# index method returns place of a value

print(t3.index('b'))
