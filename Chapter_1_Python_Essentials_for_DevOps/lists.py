# the constructor method list() can be used to create an empty list or a list based on another finite iterable object
list()  # []

list(range(10))  # [0,1,2,3,4,5,6,7,8,9]

# ['H', 'e', 'n', 'r', 'y', ' ', 'M', 'i', 'l', 'l', 'e', 'r']
list("Henry Miller")

# Lists are commonly created by directly using the square bracket form
empty = []

nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# They can contain mixed data types
mixed = [0, "a", nine, "WheelHoss"]

# You can append items easily to a list using the append() method
pies = ["cherry", "apple"]
pies.append("rhubarb")  # ['cherry', 'apple', 'rhubarb']

# You can also use insert(), it's less intuitive but you can specify the index where you want to insert the object
pies.insert(1, mixed)
# ['cherry', [0, 'a', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'WheelHoss'],'apple','rhubarb']

# The contents of a list can be appended to another list using the extend() method
letters = ["a", "b", "c"]
nine.extend(letters)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']

# You can use pop() to remove the last item from a list and return it
pies.pop()  # 'rhubarb'

pies.pop(1)
# [0, 'a', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c'], 'WheelHoss']

# There's also remove() which just removes the first occurrence of an item
pies.remove("apple")


# LIST COMPREHENSIONS

# You can use the functionality of a for loop in a single line, this works for lists and dicts

# for version
squares = []
for i in range(10):
    squared = i * i
    squares.append(squared)

print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# comprehension version
squares2 = [i * i for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
NOTE: The functionality of the inner block is put first, followed by the for statement.
Conditionals can also be added at the end
"""

squares_even = [i * i for i in range(10) if i % 2 == 0]
# [0, 4, 16, 36, 64]
