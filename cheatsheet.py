# Cheat Sheet

-------------------------------------

#Printing

() = '()'
print()

#Examples:

hw = 'Hello World!'
print(hw)

hay = 'How Are You?'
print(hay)

-------------------------------------

#Mathematical Operations

lineBreak = "#################### \n"

addition = 6 + 9
print("the value of 6 + 9 is: ")
print(addition)
print(lineBreak)

subtraction = 6 - 9
print("the value of 6 - 9 is: ")
print(subtraction)
print(lineBreak)

multiplication = 6 * 9
print("the value of 6 * 9 is: ")
print(multiplication)
print(lineBreak)

division = 6 / 9
print("the value of 6 / 9 is: ")
print(division)
print(lineBreak)

floorDivision = 6 // 9
print("the value of 6 // 9 is: ")
print(floorDivision)
print("lineBreak")

modulo/mod/remainder = 6 % 9
print("the value of 6 % 9 is: ")
print(modulus)
print(lineBreak")

-------------------------------------

#All below operators are for strings:

str.find(sub[, start[, end]])
      ('Py' in Python)
      True
      
str.format
      "The sum of 1 + 2 is {0}".format(1+2)
      'The sum of 1 + 2 is 3'
      
str.format_map(mapping)
      class Default(dict):
          def __missing__(self, key):
              return key

    '{name} was born in {country}'.format_map(Default(name='Guido'))
'Guido was born in country'

str.index()

str.isalnum()

str.isalpha()

str.isdecimal()

str.isdigit()

str.isindentifier

str.islower()

str.isnumeric()

str.isprintable()

str.isspace

str.istitle

str.isupper

str.join(iterable)

str.ljust(width[, fillchar])

str.lower()

str.lstrip
    '   spacious'.lstrip()
'spacious   '
    'www.example.com'.lstrip('cmowz.')
'example.com'

#static:
str.maketrans(x[, y[, z]])

str.partition(sep)

str.replace(old, new[, count])

str.rfind(sub[, start[, end]])

str.rindex(sub[, start[, end]])

str.rjust(width[, fillchar])

str.rpartition(sep)

str.rsplit(sep=None, maxsplit=-1)

str.rstrip([chars])
    '   spacious   '.rstrip()
    '   spacious'
    'mississippi'.rstrip('ipz')
'mississ'

str.split
'1,2,3'.split(',')
['1', '2', '3']
>>> '1,2,3'.split(',', maxsplit=1)
['1', '2,3']
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']

'1 2 3'.split()
['1', '2', '3']
>>> '1 2 3'.split(maxsplit=1)
['1', '2 3']
>>> '   1   2   3   '.split()
['1', '2', '3']

str.splitlines([keepends])

      #All below is a chart of representations and descriptions:

      \n   Line Feed
      \r   Carriage Return
      \r\n   Carriage Return + Line Feed
      \v or \x0b   Line Tabulation
      \f or \x0c   Form Feed
      \x1c   File Separator
      \x1d   Group Separator
      \x1e   Record Separator
      \x85   Next Line (C1 Control Code)
      \u2028   Line Separator
      \u2029   Paragraph Separator

      #Examples:

'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']

"".splitlines()
[]
>>> "One line\n".splitlines()
['One line']

#For comparison, split('\n') gives:

''.split('\n')
['']
>>> 'Two lines\n'.split('\n')
['Two lines', '']

str.startswith(prefix[, start[, end]])

str.strip([chars])

'   spacious   '.strip()
'spacious'

'www.example.com'.strip('cmowz.')
'example'

comment_string = '#....... Section 3.2.1 Issue #32 .......'

comment_string.strip('.#! ')
'Section 3.2.1 Issue #32'

str.swapcase()

str.title()

'Hello world'.title()
'Hello World'

"they're bill's friends from the UK"
"They'Re Bill'S Friends From The Uk"

import re
def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
      titlecase("they're bill's friends.")
"They're Bill's Friends."

str.translate(table)

str.upper()

str.zfill(width)
    "42.zfill(5)
'00042
      "-42".zfill(5)
'-0042'

print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.

#Below is a chart with flags and their meanings:

      '#'   The value conversion will use the "alternate form" (where defined below)
      '0'   The conversion will be zero padded for numeric values
      '_'   The converted value is left adjusted (overrides the '0' conversion if both are given).
      ' '   (a space) A blank should be left before a positive number (or empty string) produced by a sign conversion   
      '+'   A sign character ('+' or '_') will precede the conversion (overrides a "space" flag).
#The conversion types for these flags are below with their meanings:

      'd'   Signed integer decimal
      'i'   Signed integer decimal
      'o'   Signed octal value
      'u'   Obsolete type - it is identical to 'd'
      'x'   Signed hexadecimal (lowercase)
      'X'   Signed hexadecimal (uppercase)
      'e'
      'E'
      'f'
      'F'
      'g'
      'G'
      'c'
      'r'
      's'
      'a'
      '%'
      #Search for last MEANING typed to find where left off
