# If the name has an even number of letter, each pair of letters in the name is flipped. 
# For example, the name apax would become paxa

# If the name had an odd number of letters, the last letter of the name remains the same, and the rest of the name is treated according to rule 1
# For example, the name alexi would become laxei

def flip_names():
    apaxiaNameList = list(input("Input a name: "))
    new_name = []
    if len(apaxiaNameList) % 2 == 0:
        for i in range(0,len(apaxiaNameList),2):
            new_name.append(apaxiaNameList[i+1])
            new_name.append(apaxiaNameList[i])
    else:
        for i in range(0,len(apaxiaNameList)-1,2):
            new_name.append(apaxiaNameList[i+1])
            new_name.append(apaxiaNameList[i])
        new_name.append(apaxiaNameList[-1])
    print("".join(new_name))

flip_names()        