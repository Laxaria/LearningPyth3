# After its successful rainfall measurement campaign, the University of Chicago Weather Service is ready to undertake a new challenge: 
# measuring snowfall. More specifically, each day a volunteer will take measurements of how deep the snow is at various points around campus. 
# Each measurement is a non-negative integer. Given this information, we would like to 
# compute the difference between the biggest and smallest depth observed.

# Input
# The input is composed of two lines. The first line contains a single positive integer nn (1≤n≤1001≤n≤100) that 
# specifies the number of measurements. The second line contains the measurements, each separated by a single space.

def weather_measure():
    input1 = input("Input number of measurements: ")
    input2 = input("Input a list of measurements: ")
    listMeasures = list(map(int, input2.split(" ")))
    if len(listMeasures) != int(input1):
        print("Error; number of measurements does not match count of measurements")
    else:
        smallestMeasure = listMeasures[0]
        largestMeasure = 0
        for i in listMeasures:
            if i > largestMeasure:
                largestMeasure = i
            elif i < smallestMeasure:
                smallestMeasure = i
    print(largestMeasure - smallestMeasure)

weather_measure()