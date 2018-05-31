import random
# WORD CHOOSER
def word_picker():
    try:
        with open('hangmanlist.txt') as hangmanlist:
            listOfWords = list(hangmanlist)
            return listOfWords[random.randint(0,len(listOfWords)-1)]
    except IOError:
        print("Creating hangmanlist.txt")
        listOfWords = []
        with open("google-10000-english-usa.txt", "r") as f:
            for line in f:
                if len(line) >= 11:
                    with open("hangmanlist.txt", "a+") as h:
                        h.write(line)
        return False

# WORD CHECKER
def word_checker(a, c):
    savedWord = list(c)
    wordCheck = [i for i, x in enumerate(savedWord) if x == a]
    if not wordCheck:
        print("No find")
        return False
    else:
        return wordCheck

# Track User Input
def user_input_validator(a, b):
    if (len(a) == 1) and (a.isdigit() == False) and (a not in b):
        return a
    else:
        return False

# GAME
def game(b):
    i = 0
    blankWord = list("_" * (len(b)-1))
    trackUserInput = []
    while i < 7:
        print("Letters you have tried: " + " ".join(sorted(trackUserInput)) + "\n")
        userInput = input("Input a letter: ")
        userInputState = user_input_validator(userInput, trackUserInput)
        if userInputState == False:
            print("There is an error with your input. \nPlease make sure your input is a single letter that has not been used yet.\n")
            continue
        else:
            userInput = userInputState
            trackUserInput.append(userInput)
        gameState = word_checker(userInput, b)
        if gameState == False:
            i += 1
            print("You have {} tries remaining.".format(7-i),"\n","".join(blankWord),"\n")
            continue
        else:
            for j in gameState:
                blankWord[j] = userInput
            print("\n"+"".join(blankWord))
            if "".join(blankWord) == b[0:-1]:
                return print("You have won!")
            continue
    print("The word was {}".format(b))
    print("You have lost")
            

# MAIN

def main():
    chosenWord = word_picker()
    if chosenWord == False:
        chosenWord = word_picker()
    print("\nWe have chosen a word for you. This word is {} characters long".format(len(chosenWord)),"\n")
    game(chosenWord)

main()