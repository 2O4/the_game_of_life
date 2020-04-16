#
# Conway's Game of Life
# https://en.wikipedia.org/wiki/Conway's_Game_of_Life
# Python integration by 2O4
#

import time
import os


WIDTH = 20
HEIGHT = 10

grid = [[False] * WIDTH for x in range(HEIGHT)]


def game_of_life(grid):
    """
    grid: 2D list countaining boolean values
            True represent a live cell
            False represent a dead cell
    return: grid after 1 tick
    """
    temp = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):

            # Get every neighbors without leaving the grid
            neighbors = [
                grid[m][n] 
                for n in range(
                    max(x-1, 0),
                    min(x+2, len(grid[y]))
                ) 
                for m in range(
                    max(y-1, 0),
                    min(y+2, len(grid))
                )
            ]

            # Count alive neighbors
            neighbors_count = neighbors.count(True) - (1 if grid[y][x] else 0)

            # Apply Conway's Game of Life rules to determine births and deaths
            if grid[y][x] and neighbors_count < 2 or neighbors_count > 3:
                # Any live cell with fewer than two live neighbours or 
                # with more than three live neighbours dies.
                temp.append([y, x, False])
            elif not grid[y][x] and neighbors_count == 3:
                # Any dead cell with exactly three live neighbours becomes a live cell.
                temp.append([y, x, True])
    
    # Apply transformations to the grid so that births and deaths occur simultaneously
    for cell in temp:
        grid[cell[0]][cell[1]] = cell[2]

    return grid


def print_grid(grid):
    for x in grid:
        for y in x:
            if y:
                print(end='O ')
            else:
                print(end='. ')
        print()


x = 1

if x == 0:
    # Blinker
    grid[1][2] = True
    grid[1][3] = True
    grid[1][4] = True
elif x == 1:
    # Glider
    grid[1][2] = True
    grid[2][3] = True
    grid[3][1] = True
    grid[3][2] = True
    grid[3][3] = True


while True:
    print_grid(grid)
    grid = game_of_life(grid)
    time.sleep(0.2)
    os.system('cls')
