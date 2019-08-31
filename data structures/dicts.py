
# dictionaries has no indeces rather you can use keys

myDict = {"key1": "Value1", "key2": "Value2"}

print(myDict)

# grab a value from dictoanry based on key

print(myDict["key1"])

# usecase of dictionaries is prices list for set of items

prices = {"apple": "2000$", "samsung": "1700$", "Lenovo": "1200$"}

print(prices["samsung"])

# dictionray can hold any dataTypes

complexDictionary = {"String": "WaleedHassan", "bool": True,
                     "integer": 100, "float": 2.4,
                     "dict": {"key": "value"},
                     "list": [1, True, 2]}
print(complexDictionary)

print(complexDictionary["list"])
print(complexDictionary["dict"]["key"])
print(complexDictionary["list"][1])

# add to dictionary

myDict["key3"] = "Value3"
print(myDict)

# dict.keys() method returns all dict keys as a list

print(myDict.keys())

# dict.values() method returns all dict values as a list

print(myDict.values())

# dict.items() method returns all dict keys and values as a list of tuples

print(myDict.items())
