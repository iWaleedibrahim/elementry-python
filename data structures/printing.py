

# .format replace what in curly braces with given variable

print("this is a string {}".format("INSERTED"))

# replace many vaibles in order

print("The {} {} {}".format('fox', "brown", "quick"))

# replace based on varibles index in .format

print("The {2} {1} {0}".format('fox', "brown", "quick"))

# replace with repeating

print("The {1} {1} {1}".format('fox', "brown", "quick"))

# replace with keywords

print("The {adjuctive} {color} {animal}".format(
    animal='fox', color="brown", adjuctive="quick"))
