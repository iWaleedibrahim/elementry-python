

def hello_function(name='Bro'):
    '''
    DOCSTRING: Information about the function
    Input: name
    outPut: Hello + name
    '''
    return "HelloWorld!" + name


result = hello_function('Brother')

# print(result)


def add(n1, n2):
    return n1+n2


res = add(2, 4)

# print(res)


# find out if the word dog in a string


def searchForWord(word):
    return 'dog' in word.lower()


print(searchForWord('where is my dog'))
