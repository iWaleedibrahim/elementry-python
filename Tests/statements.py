
#
# 1st problem

st = "Sam Print Only the words that starts with s in this sentence"

for word in st.split(" "):
    if word[0].lower() == 's':
        print(word)

# okay I will come for that later

# 2nd problem

even_numbers = [even for even in range(0, 10) if even % 2 == 0]

print(even_numbers)

# OR

print(range(0, 10, 2))

three_multiples = [num for num in range(1, 50) if num % 3 == 0]

print(three_multiples)

# 3rd problem

if len(st.split(" ")) % 2 == 0:
    print("even list")
else:
    print("Odd list")

for i in range(0, 100):
    if i % 5 == 0:
        print("Fizz")
        if i % 3 == 0:
            print("FizzBuzz")
    elif i % 3 == 0:
        print("buzz")
    else:
        print(i)
