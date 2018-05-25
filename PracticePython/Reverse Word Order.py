# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def Reverse_Word(userInput):
    listString = list(userInput.split())
    print(" ".join(listString[::-1]))

Reverse_Word(input("Type in a string: "))