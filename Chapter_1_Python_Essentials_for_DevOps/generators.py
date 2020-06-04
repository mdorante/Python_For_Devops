# Generators perform some operation on data in chunks, pausing their state between calls
# they use the 'yield' keyword instead of 'return' in order to return the current state and pause until the next call

# Let's write a simple function that counts and yields each number


def count():
    n = 0
    while True:
        n += 1
        yield n


counter = count()

next(counter)  # 1
next(counter)  # 2
next(counter)  # 3
next(counter)  # 4

# Let's use this mechanism to create a Fibonacci generator


def fib():
    first = 0
    last = 1
    while True:
        first, last = last, first + last
        yield first


f = fib()

next(f)  # 1
next(f)  # 1
next(f)  # 2
next(f)  # 3
next(f)  # 5
next(f)  # 8
next(f)  # 13
next(f)  # 21

# We can also iterate using the generator in a for loop

f2 = fib()
for x in f2:
    print(x)
    if x > 21:
        break
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# GENERATOR COMPREHENSIONS
# similar syntax to list and dict comprehensions, but in this case we use parentheses

num_gen = (x for x in range(100))
next(num_gen)  # 0
next(num_gen)  # 1
next(num_gen)  # 2
next(num_gen)  # 3
next(num_gen)  # 4
