#Write a program, in any language (incl pseudocode) that iterates the numbers from 1 to 100.
#For any value divisible by 4, the program should print "Go".
#For any value divisible by 5, the program should print "Figure".
#For any value divisible by 4 and 5, the program should print "GoFigure".

for a in range(0, 100, 1):
    if a % 4 == 0 and a % 5 == 0:
        print("Go Figure")
    elif a % 5 == 0:
        print("Figure")
    elif a % 4 == 0:
        print("Go")