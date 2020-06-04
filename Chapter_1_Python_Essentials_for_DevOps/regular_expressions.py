# The "re" module offers regular expression operations
import re

# Let's say we have an email cc list and we want to query email addressess in the list
cc_list = """Itachi Uchiha <iuchiha@konoha.com>,
Naruto Uzumaki <nuzumaki@konoha.com>,
Kakashi Hatake <khatake@konoha.com>,
Neji Hyuga <nhyuga@konoha.com>,
Hidan <hidan@akatsuki.com>"""

# We can use the built in "in" operator for this
"Itachi" in cc_list  # True

# We can also use the re.search() method for similar behavior
# NOTE: The default re.search() behavior returns the first match

re.search(r"Kakashi", cc_list)
# <re.Match object; span=(74, 81), match='Kakashi'>
# NOTE: Raw strings are recommended for regex operations, otherwise known as r strings

# What if we want to find an entry, but we don't remember if the name was Naruto or Maruta?
# We can use comma separated values
re.search(r"[N,M]arut[o,a]", cc_list)
# <re.Match object; span=(36, 42), match='Naruto'>

# Or ranges
re.search(r"Itac[a-z][a-z]", cc_list)
# <re.Match object; span=(0, 6), match='Itachi'>

# The "+" after a regex item matches one or more of that item
re.search(r"[A-Za-z]+", cc_list)
#  <re.Match object; span=(0, 6), match='Itachi'>

# A number in curly braces matches that exact number of characters
re.search(r"H[a-z]{5}", cc_list)
# <re.Match object; span=(82, 88), match='Hatake'>

# Let's construct a regex combination that matches a generic email address
re.search(r"[A-Za-z0-9]+@[a-z]+\.[a-z]+", cc_list)
# <re.Match object; span=(15, 33), match='iuchiha@konoha.com'>

# NOTE: the "." is a wildcard that matches any character,
# if you want to search for an actual ".", you have to escape it with a backslash

r""" "re" offers character classes, which are premade character sets,
such as "\w" which represents [a-zA-Z0-9_] and "\d" which represents [0-9]"""

re.search(r"\w+", cc_list)
# <re.Match object; span=(0, 6), match='Itachi'>

re.search(r"\w+\@\w+\.\w+", cc_list)
# <re.Match object; span=(15, 33), match='iuchiha@konoha.com'>

# You can use parentheses to define groups in a match, they can then be accessed from the match object
# The 0 group represents the whole match, the rest are numbered in order

email = re.search(r"(\w+)(\@\w+)(\.\w+)", cc_list)
# <re.Match object; span=(15, 33), match='iuchiha@konoha.com'>

email.group(0)  # 'iuchiha@konoha.com'
email.group(1)  # 'iuchiha'
email.group(2)  # '@konoha'
email.group(3)  # '.com'

# You can also give names to the groups by adding ?P<name> in the group definition

email_2 = re.search(r"(?P<username>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
# <re.Match object; span=(15, 33), match='iuchiha@konoha.com'>

print(
    f"""Username: {email_2.group('username')}
Secondary Level Domain: {email_2.group('SLD')}
Top Level Domain: {email_2.group('TLD')}"""
)
# Username: iuchiha
# Secondary Level Domain: konoha
# Top Level Domain: com

# we can use findall() to return a list of all matches
email_addresses = re.findall(r"(?P<username>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
# [('iuchiha', 'konoha', 'com'),
#  ('nuzumaki', 'konoha', 'com'),
#  ('khatake', 'konoha', 'com'),
#  ('nhyuga', 'konoha', 'com'),
#  ('hidan', 'akatsuki', 'com')]

usernames = [address[0] for address in email_addresses]
# ['iuchiha', 'nuzumaki', 'khatake', 'nhyuga', 'hidan']

# finditer() returns an iterator object, which processes text until it finds a match and then stops
# this object can be passed to the next() function in order to return the current match and then search for the next match

one_at_a_time = re.finditer(r"(?P<username>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)

next(one_at_a_time)  # <re.Match object; span=(15, 33), match='iuchiha@konoha.com'>
next(one_at_a_time)  # <re.Match object; span=(52, 71), match='nuzumaki@konoha.com'>
next(one_at_a_time)  # <re.Match object; span=(90, 108), match='khatake@konoha.com'>

# You can also iterate through the object in a for loop
for email in one_at_a_time:
    print(email.groupdict())
# {'username': 'nhyuga', 'SLD': 'konoha', 'TLD': 'com'}
# {'username': 'hidan', 'SLD': 'akatsuki', 'TLD': 'com'}

# NOTE: the for loop started where next() left off, because next already iterated through the first 3 matches

# You can substitute values for matches using re.sub()
re.sub(r"\d", "#", "The password you entered was 9381716")
# 'The password you entered was #######'

reverse_emails = re.sub(
    r"(?P<username>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)",
    r"\g<TLD>.\g<SLD>@\g<username>",
    cc_list,
)
# 'Itachi Uchiha <com.konoha@iuchiha>,
# Naruto Uzumaki <com.konoha@nuzumaki>,
# Kakashi Hatake <com.konoha@khatake>,
# Neji Hyuga <com.konoha@nhyuga>,
# Hidan <com.akatsuki@hidan>'

# If we're going to need a regex pattern multiple times throughout our code,
# we can compile the regex pattern into an object and then call that object each time we need it

email_regex_pattern = re.compile(r"(?P<username>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)")

email_regex_pattern.search(cc_list)
# <re.Match object; span=(15, 33), match='iuchiha@konoha.com'>
