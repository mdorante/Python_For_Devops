# Sequences: list, range, tuple, string, and binary types

# You can use the "in" and "not in" operators to test if an an item exists in a sequence

2 in [1, 2, 3]  # True
"a" not in "cat"  # False
10 in range(12)  # True
10 not in range(2, 4)  # True

# You can reference the contents of a sequence by using its index number

my_sequence = "Florida man"
my_sequence[0]  # F
my_sequence[5]  # d

# Indexing can also be done backwards by using negative index numbers

my_sequence[-1]  # n
my_sequence[-7]  # i

# The "index" method returns the first occurrence of an item in a sequence, but options can be used to modify its behavior

my_sequence.index("m")  # 8
my_sequence.index("a")  # 6
my_sequence.index("a", 7, 10)  # 9

# You can produce a new sequence from an existing one using slicing

# slice = sequence[start:stop:step]

my_sequence = ["a", "b", "c", "d", "e", "f", "g"]
my_sequence[2:5]  # ['c', 'd', 'e']
my_sequence[:5]  # ['a', 'b', 'c', 'd', 'e']
my_sequence[3:]  # ['d', 'e', 'f', 'g']
my_sequence[-6:]  # ['b', 'c', 'd', 'e', 'f', 'g']
my_sequence[3:-1]  # ['d', 'e', 'f']

# some sequence methods

my_sequence = [0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]

len(my_sequence)  # 12
min(my_sequence)  # 0
max(my_sequence)  # 4
my_sequence.count(1)  # 3
