# list support indexing and slicing, and it works just like strings

myList = [1, 2, 3]
myList2 = ['String', 100, 20.33, True]
myList3 = ['one', 'two', 'three']

# print lengeth of a list

print(len(myList))
print(len(myList2))


# concatante two lists

print(myList + myList2)

# difference from string that we can mutate a list
myList3[0] = 'OneAllCaps'
print(myList3)

# add element to the end of a list
myList3.append("Four")
print(myList3)

# remove item from a list using pop method, it returns removed item

print(myList.pop())

# remove item from a list using pop method in specific index
# by default it has paramater of -1 that is the last element

print(myList.pop(1))

# sort list using sort method in place
# it changes the original list, doesn't return a new list.
# None is the returned value of a function that doesn't return anything.


myList5 = ['a', 'b', 'x', 'c', 'd', 'u']
print(myList5.sort())
print(myList5)

# reverse a list using reverse method

myList5.reverse()
print(myList5)
