# Docstrings act as inline documentation for your functions
# Using docstrings is a best practice


def my_function():
    """This is a docstring.
    It describes what my function does, what type of parameters it takes in,
    and what is expected to be returned.
    """
    pass


# Function arguments are specified inside the parantheses


def values1(a, b):
    """
    Uses positional arguments to print two values.
    """
    print(f"First: {a}")
    print(f"Second: {b}")


def values2(a=1, b=2):
    """
    Default values assigned.
    """
    print(f"First: {a}")
    print(f"Second: {b}")


# If we specify arguments in order, they will be used in that order:
values1(1, 3)
# First: 1
# Second: 3

values1(5, 2)
# First: 5
# Second: 2

# We can also use keywords and the order will not matter
values1(b=9, a=4)
# First: 4
# Second: 9

# If we specify default values during the function definition, those will be used if no values
# are given when calling the function
values2()
# First: 1
# Second: 2

# NOTE: When we define a keyword parameter, all parameters after that will have to be keyword

# All functions return a value, if not set in the function definition, then it will return None


def no_return():
    """Function with no return definition"""
    pass


print(no_return())  # None
print(values2())
# First: 1
# Second: 2
# None


def return_one():
    """Returns a 1"""
    return 1


print(return_one())  # 1

# Functions are objects and you can use them as such,
# for example: you can put them in a list and loop through the list to invoke them


def double(number):
    """returns the number doubled"""
    return number * 2


def triple(number):
    """returns the number tripled"""
    return number * 3


functions = [double, triple]

for function in functions:
    print(function(5))
# 10
# 15

# Lambda functions (anonymous functions)
# generic form:  lambda <param> : <return expression>

# In this example, we have a list of lists and we want to sort them by the second or third item
# the default sorted() algorithm sorts by the first item in every list

items = [[0, "a", 2], [5, "b", 0], [2, "c", 1]]

sorted(items, key=lambda item: item[1])
# [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]

sorted(items, key=lambda item: item[2])
# [[5, 'b', 0], [2, 'c', 1], [0, 'a', 2]]
