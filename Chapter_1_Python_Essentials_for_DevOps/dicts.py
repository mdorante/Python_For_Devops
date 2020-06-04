# Like all the other data types, you can use the constructor method to create a dict
map = dict()

kv_list = [["key-1", "value-1"], ["key-2", "value-2"]]
dict(kv_list)  # {'key-1': 'value-1', 'key-2': 'value-2'}

# Or you can also just directly use curly braces and manually create the dict
map = {"key-1": "value-1", "key-2": "value-2"}

# You can access the values associated to keys
map["key-1"]  # 'value-1'
map["key-2"]  # 'value-2'

# You can use the same syntax to create a new value or modify an existing one
map["key-3"] = "value-3"
map["key-1"] = 15

# get() checks if you have a key defined in the dict, if not, it will return a default value
# If you don't define a default value and the key doesn't exist, it will return None

map.get("key-4", "not here bruh")  # 'not here bruh'

# Use del() to remove a key-value pair
del map["key-1"]

# methods that return a dict's contents

map.keys()  # dict_keys(['key-2', 'key-3'])
map.values()  # dict_values(['value-2', 'value-3'])
map.items()  # dict_items([('key-2', 'value-2'), ('key-3', 'value-3')])

# DICT COMPREHENSIONS
letters = "abcde"

# A dict that maps all letters to their uppercase representations
letters_upper = {i: i.upper() for i in letters}
# {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'}

letters_upper["b"]  # 'B'
