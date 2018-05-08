import numpy as np
import pprint
import copy


# Define board size and initiate board 
side = 10
currentBoard= np.random.randint(2,size=(side, side))
pprint.pprint(currentBoard)

# Conway Game of Life Function
def gameoflife(a):
    # Make a true copy of board state to ensure only new board gets changed
    newBoard = copy.copy(currentBoard)

    # Iteration for doing calculations
    for x in range(side):
        for y in range(side):
            # Topoidal wrapping. Eg, for 0,0, the cell above is 0,-1, which is out of boundary.
            # -1%side returns the y-coordinate for the wrap-around
            # -1%10 returns 9, making the cell above 0,0 as 0,9
            num_neighbours = currentBoard[(x-1)%side, (y-1)%side] + \
                             currentBoard[(x)%side, (y-1)%side] + \
                             currentBoard[(x+1)%side, (y-1)%side] + \
                             currentBoard[(x-1)%side, (y)%side] + \
                             currentBoard[(x+1)%side, (y)%side] + \
                             currentBoard[(x-1)%side, (y+1)%side] + \
                             currentBoard[(x)%side, (y+1)%side] + \
                             currentBoard[(x+1)%side, (y+1)%side]
            # If-statements to execute conditionals in Game of Life
            # Statements take the original board state, calculates neighbours, 
            # then writes changes to a new board state
            if currentBoard[x,y] == 0:
                if num_neighbours == 3:
                    newBoard[x,y] = 1
            elif currentBoard[x,y] == 1:
                if num_neighbours <= 1:
                    newBoard[x,y] = 0
                elif num_neighbours == 2|3:
                    newBoard[x,y] = 1
                elif num_neighbours >= 4:
                    newBoard[x,y] = 0
    return newBoard

for i in range(10):
    print('\n')
    pprint.pprint(gameoflife(currentBoard))
    currentBoard = gameoflife(currentBoard)
