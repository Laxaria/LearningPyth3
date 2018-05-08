import random

known = random.randint(0,100)
def main():
    known = random.randint(0,100)
    guess = input()
    counter = 0
    while int(guess) != known:
        if int(guess) < known:
            print("Your guess," , str(guess), "is too low")
            counter +=1
            print('Try again')
            guess = input()
        elif int(guess)> known:
            print("Your guess," , str(guess), "is too high")
            counter +=1
            print('Try again')
            guess = input()
    print('Your guess is correct', str(known), str(counter), "tries")
        
main()
        
