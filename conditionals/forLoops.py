
# all objects in python are iteratable, list, dicts, Strings ..

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_string = "HelloWorld!"
my_list_of_tuples = [(1, 2), (3, 4), (5, 6)]
my_list_of_triples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
d = {'k1': 1, 'k2': 2, 'k3': 3}


list_sum = 0
for number in my_list:
    list_sum = list_sum + number
print(list_sum + 120 + 30 + 20)


for char in my_string:
    print(char)

for item in (1, 2, 3):
    print(item)

print(len(my_list_of_tuples))

for tup in my_list_of_tuples:
    print(tup)


# tuple and packing
for x, y in my_list_of_tuples:
    print(x)
    print(y)

# in triples
for x, y, z in my_list_of_triples:
    print(x)
    print(y)
    print(z)


for item in d.items():
    print(item)

for key, value in d:
    print(key)
    print(value)


# nested loops


for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        [].append(x*y)

print(my_list)
