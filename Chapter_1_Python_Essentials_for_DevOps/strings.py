# You can use the constructor method str() to make strings from other objects
my_list = list()
str(my_list)

multi_line_string = """This is a
multi line
string
"""

# strip() is useful if you want to remove extra whitespace at the beginning and end of a string

input = "    I like pizza         "

input.strip()  # 'I like pizza'
input.rstrip()  # '    I like pizza'
input.lstrip()  # 'I like pizza         '

# ljust() and rjust() can add padding to the sides of a string

output = "Barry"

output.ljust(10)  # 'Barry     '
output.rjust(10, "*")  # '*****Barry'

# split() breaks a string into a list of strings

text = "Mary had a little lamb"
text.split()  # ['Mary', 'had', 'a', 'little', 'lamb']

url = "gt.motomomo.io/v2/api/asset/143"
url.split("/")  # ['gt.motomomo.io', 'v2', 'api', 'asset', '143']

# join() creates a string from a list and inserts a separator between each item

food = "pasta", "barbecue", "soup"
" and ".join(food)  # 'pasta and barbecue and soup'

# You can also change the case used in strings

name = "itachi uchiha"

name.capitalize()  # 'Itachi uchiha'
name.title()  # 'Itachi Uchiha'
name.swapcase()  # 'ITACHI UCHIHA'

name = name.upper()  # 'ITACHI UCHIHA'
name.lower()  # 'itachi uchiha'

# Always try to use f-strings as they're easier to write and read than other string formatting methods
a = 1
b = 2
f_string = f"a is {a}, b is {2}, a+b is {a+b}"  # 'a is 1, b is 2, a+b is 3'


# You can also do some nice things with the format() method
# Here we're using a dict to insert the values for our replacement fields
values = {"first": "Spider", "last": "Man"}

"Peter Parker by day, {first} {last} by night".format(**values)
# 'Peter Parker by day, Spider Man by night'

# You can also use the format specification mini-language
text = "{0:>15} - {1:<25}"
text.format("Beer", "Wine")  # '           Beer - Wine                     '

text2 = "{0:$>20} | {1:%<15} | {2:#>20}"
text2.format("Winter", "Summer", "Spring")
# '$$$$$$$$$$$$$$Winter | Summer%%%%%%%%% | ##############Spring'

# Format specification can also be done with f-strings
number = 100
f"some stuff {number:@<15}"  # 'some stuff 100@@@@@@@@@@@@'

padding = 20
f"some other stuff {number:{padding}}"
# 'some other stuff                  100'

# NOTE: It is highly recommended to use f-strings
