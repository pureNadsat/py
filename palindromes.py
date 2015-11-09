# program that finds palindromes of words greater than 7 characters in the english language

# import operating system module
import os

# open file object and convert to a list of strings
with open('/users/abrick/resources/american-english-insane') as dictionary:
    listWords = [line.rstrip('\n') for line in dictionary]

# loop that extracts palindromes from a list of words greater than 7 characters
palindromesSeven = []
for word in listWords:
    if word == word[::-1] and len(word) > 7:
        palindromesSeven.append(word)

# prints a list of palindromes greater than 7 characters
print(palindromesSeven)

