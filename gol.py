#
# Conway's Game of Life
# https://en.wikipedia.org/wiki/Conway's_Game_of_Life
# Python integration by 2O4
#

import pygame


def game_of_life(grid):
    """
    Conway's Game of Life Python algortihm

    grid: 2D list countaining boolean values
            True represent a live cell
            False represent a dead cell
    return: grid after 1 tick
    """
    temp = []

    width = len(grid[0])
    height = len(grid)

    for y in range(height):
        for x in range(width):

            # Get every neighbors
            neighbors = [
                grid[m][n] 
                for n in [x-1, x, (x+1)%width]
                for m in [y-1, y, (y+1)%height]
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


class GameOfLifeGUI():
    def __init__(self, width=60, height=18):
        # ALGORITHM
        self.width = width
        self.height = height
        self.grid = [
            [False for x in range(self.width)]
            for x in range(self.height)
        ]

        self.physicsUpdateFrameRate = 3

        # GUI/PYGAME
        self.tileSize = 6
        self.windowWidth = self.width * self.tileSize
        self.windowHeight = self.height * self.tileSize
        self.windowSize = (self.windowWidth, self.windowHeight)
        self.window = pygame.display.set_mode(self.windowSize, 0, 32)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Conway's Game of Life")
        # GUI COLORS
        self.liveTileColor = (15, 15, 15)
        self.deadTileColor = (250, 250, 250)

    def gui_loop(self):
        pygame.init()
        currentPhysicFrame = 0
        pause = False
        while True:
            pygame.display.update()
            self.clock.tick(30)
            if currentPhysicFrame == 0 and not pause:
                game_of_life(self.grid)
                self.display_tiles()
            currentPhysicFrame = (currentPhysicFrame + 1) % self.physicsUpdateFrameRate
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.onClick(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = not pause

    def onClick(self, pos):
        x = int(pos[0] / self.tileSize)
        y = int(pos[1] / self.tileSize)
        self.grid[y][x] = not self.grid[y][x]
        self.display_one_tile(x, y)

    def load_glider(self):
        self.grid[1][2] = True
        self.grid[2][3] = True
        self.grid[3][1] = True
        self.grid[3][2] = True
        self.grid[3][3] = True

    def load_pulsar(self):
        from saves import pulsar
        self.load_from_grid(pulsar.DATA)

    def load_gospers_glider_gun(self):
        from saves import gospers_glider_gun 
        self.load_from_grid(gospers_glider_gun.DATA)

    def load_from_grid(self, grid_to_load):
        h = len(grid_to_load)
        l = len(grid_to_load[0])
        for x in range(h):
            for y in range(l):
                self.grid[x][y] = grid_to_load[x][y]

    def tile_position(self, x, y):
        """
        convert a grid position into gui position of a tile
        """
        gui_x = self.tileSize * x
        gui_y = self.tileSize * y
        return gui_x, gui_y

    def display_tiles(self):
        """
        Update the display of every tiles on the grid
        """
        for x in range(self.width):
            for y in range(self.height):
                self.display_one_tile(x, y)

    def display_one_tile(self, x, y):
        """
        Update the display of a single tile on the grid
        """
        self.window.fill(
            [self.liveTileColor if self.grid[y][x] else self.deadTileColor][0],
            pygame.Rect((
                self.tile_position(x, y),
                (self.tileSize, self.tileSize)
            ))
        )


if __name__ == "__main__":
    gui_gol = GameOfLifeGUI(width=120, height=30)
    #gui_gol.load_gospers_glider_gun()
    gui_gol.gui_loop()
