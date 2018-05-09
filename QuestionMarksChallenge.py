# Using the Python language, have the function QuestionsMarks(str) 
# take the str string parameter, which will contain single digit 
# numbers, letters, and question marks, and check if there are 
# exactly 3 question marks between every pair of two numbers that 
# add up to 10. If so, then your program should return the string 
# true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, 
# then your program should return false as well. 

# For example: if str is "arrb6???4xxbl5???eee5" then your program 
# should return true because there are exactly 3 question marks 
# between 6 and 4, and 3 question marks between 5 and 5 at the end 
# of the string. 

import re
def stringcheck(a):
    a.lower()
    pattern = re.compile(r'(?=([0-9]\?{3}[0-9]))')
    reformat = re.compile(r'[a-z]*')
    test = reformat.sub('',a)
    for groups in pattern.findall(test):
        if int(groups[0]) + int(groups[-1]) == 10:
            return True
        else:
            continue
    return False
input = input('Input a random string of stuff: ')
print(stringcheck(input))