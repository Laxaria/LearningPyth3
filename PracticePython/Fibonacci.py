# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number 
# of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
# the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def Fib_Generator(userInput):
    fibList = [0, 1,1]
    userInput = int(userInput)
    if userInput == 0:
        print(fibList[0])
    elif userInput == 1:
        print(fibList[0:2])
    elif userInput == 2:
        print(fibList[0:3])
    else:
        for _i in range(userInput-3):
            fibList.append(fibList[-1] + fibList[-2])
        print(fibList)

Fib_Generator(input("How many Fibonnaci numbers do you want to generate? Input: "))
