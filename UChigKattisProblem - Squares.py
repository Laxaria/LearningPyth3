# https://uchicago.kattis.com/problems/uchicago.mpcs.square

def recursive_exp(x, n):
    if n == 0:
        print("1")
    elif n == 1:
        print(x)
    elif n % 2 == 0:
        while n > 1:
            x = x * x
            n = n/2
        print(x)
    elif n % 2 > 0:
        z = x
        while n > 1:
            x = x * x
            n = (n-1)/2
        print(x * z)

inputNumbers = list(map(int, input("Input 2 numbers: ").split(" ")))
recursive_exp(inputNumbers[0], inputNumbers[1])