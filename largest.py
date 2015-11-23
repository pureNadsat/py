#!/usr/local/bin/python3

# import operating system and reg expression modules
import os
import re

# create a string object of the philosophical book 'Urantia'
# and removes character seperators
with open('/users/abrick/resources/urantia') as urantia:
  urantia = urantia.read().replace('\n', '').replace(' ', '').replace(',', '')

# finds all the Unicode decimal digits within the string
# and converts them into integers
urantiaInts = list(map(int, re.findall('\d+', urantia)))

# print largest single digit within 'Urantia'
print(max(urantiaInts))


