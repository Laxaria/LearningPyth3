# The factorial function, n!n! is defined thus for nn a non-negative integer:
# We say that a divides b if there exists an integer k such that k⋅a=b.

# Input
# The input to your program consists of several lines, each containing two non-negative integers, 
# n and m, both less than 2**31

def factoviser(a, b):
    # Set a working integer as a, the number to be factorial'd
    n = a

    # If a == 0, a! = 1, and b is always divisible by 1
    if a == 0:
        print(b, "divides", str(a)+"!")

    else:
        # Calculate factorial recursively, using n * (n-1)
        # "For" Loop iterates through numbers of (n-1)
        for i in range(a-1, 1, -1):
            n = n * i
        if n % b == 0:
            print(b, "divides", str(a)+"!")
        else:
            print(b, "does not divide", str(a)+"!")

userInput = list(map(int, input("Type in 2 numbers: ").split(" ")))
if len(userInput) == 2:
    factoviser(userInput[0], userInput[1])
else:
    print("Error; expected only two integers")
        
    
