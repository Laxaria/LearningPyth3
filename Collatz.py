def collatz(a):
    print(a)
    while a != 1:
        if a % 2 == 0:
            a = a // 2
            yield(a)
        elif a % 2 != 0:
            a = 3 * a + 1
            yield(a)

b = int(input('Input a number: '))
print(list(collatz(b)))
