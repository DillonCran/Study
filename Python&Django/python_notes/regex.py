import re

# returns a match object if there is a match anywhere in the string
# returns None if there is no match
# this does not return a boolean value, returns a Match object.
re.search(pattern,text)

# This is the same thing as using .split() on a string
re.split(pattern,text)

# This returns a list of all matches in a string
re.findall(pattern,text)

def multi_re_find(patterns,phrase):
    # Takes in a list of regex patterns and prints a list of all matches from phrase
    for pat in patterns:
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sdddd'

test_pattern = ['sd*'] 
# ['sd*'] finds s followed by zero or more d's
# ['sd+'] finds s followed by one or more d's
# ['sd?'] finds s followed by zero or one d's
# ['sd{3}'] finds s followed by three d's
# ['sd{1,3}'] finds s followed by one to three d's
# ['s[sd]+'] finds s followed by one or more s or d
# ['[^!.?]+'] finds characters that are not !, ., or ?
# ['[a-z]+'] finds lowercase letters
# ['[A-Z]+'] finds uppercase letters
# ['[a-zA-Z]+'] finds lowercase or uppercase letters
# ['[0-9]+'] finds any numbers
# ['[^a-zA-Z0-9]+'] finds any non-alphanumeric characters
# [r'\d'] finds digits
# [r'\D'] finds non-digits
# [r'\s'] finds whitespace
# [r'\S'] finds non-whitespace
# [r'\w'] finds alphanumeric
# [r'\W'] finds non-alphanumeric


