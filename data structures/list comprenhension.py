

my_string = "HelloWorld"

# construct list like this
mylist = [char for char in my_string]

print(mylist)

my_num_list = [num**2 for num in range(0, 10)]

print(my_num_list)


# this formula replaces the .append method of lists
# we can do as much complex math inside list.

celecius = [0, 10.6, 23, 37.2, 40.3]

fehrenhiet = [((9/5)*temp+32) for temp in celecius]

print(fehrenhiet)


# also including conditionals like

degress = [51, 30, 70, 92, 60, 42, 67, 94, 83, 76, 23, 85, 0]

sucessful = [degree for degree in degress if degree > 60]
failure = [degree for degree in degress if degree < 60]

print("passing are: {}".format(sucessful))
print("fails are: {}".format(failure))
