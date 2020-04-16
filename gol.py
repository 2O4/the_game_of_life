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
    temp = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            neighbor = [
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
            neighbor_count = neighbor.count(True) - (1 if grid[y][x] else 0)

            if grid[y][x] and neighbor_count < 2 or neighbor_count > 3:
                # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                # Any live cell with more than three live neighbours dies, as if by overpopulation.
                temp.append([y, x, False])
            elif not grid[y][x] and neighbor_count == 3:
                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                temp.append([y, x, True])

    for cell in temp:
        print( cell[0], cell[1], grid[cell[0]][cell[1]], cell[2])
    
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
    time.sleep(110.2)
    os.system('cls')
