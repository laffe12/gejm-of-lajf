# Game Of Life
import pygame
import sys
import random

# Window dimensions
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1500
cell_size = 15

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)

class Cell:
    def __init__(self, x_pos, y_pos, state=False, size=cell_size):
        self.state = state # dead or alive
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = cell_size

    def draw(self, screen):
        color = WHITE if self.state else BLACK
        cell_rect = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)
        pygame.draw.rect(screen, color, cell_rect)
        pygame.draw.rect(screen, (50,50,50), cell_rect, 1) # grid lines

def create_grid(cols, rows, cell_size):
    grid = []
    for y in range(rows):
        row = []
        for x in range(cols):
            x_pos = x * cell_size
            y_pos = y * cell_size
            row.append(Cell(x_pos, y_pos, state=False))
        grid.append(row)
    return grid

def check_alive_neighbors(grid, x_pos, y_pos):
    height = len(grid)
    width = len(grid[0])
    neighbor_count = 0
    # Toroidal wrapping where grid wraps around the edges
    directions = [
        (-1,-1), (0,-1), (1,-1),
        (-1, 0),         (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    for dx, dy in directions:
        x_neighbor = (x_pos + dx + width) % width
        y_neighbor = (y_pos + dy + height) % height

        if grid[y_neighbor][x_neighbor].state:
            neighbor_count += 1
    return neighbor_count

def seed_glider(grid, x, y):
    if x + 2 >= len(grid[0]) or y + 2 >= len(grid): return # out of bounds check
    grid[y][x + 1].state = True
    grid[y + 1][x + 2].state = True
    grid[y + 2][x].state = True
    grid[y + 2][x + 1].state = True
    grid[y + 2][x + 2].state = True

def seed_blinker(grid, x, y):
    if x + 2 >= len(grid[0]) or y >= len(grid): return # out of bounds check
    grid[y][x].state = True
    grid[y][x + 1].state = True
    grid[y][x + 2].state = True

def seed_block(grid, x, y):
    if x + 1 >= len(grid[0]) or y + 1 >= len(grid): return # out of bounds check
    grid[y][x].state = True
    grid[y][x + 1].state = True
    grid[y + 1][x].state = True
    grid[y + 1][x + 1].state = True


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    # create grid
    cols = WINDOW_WIDTH // cell_size
    rows = WINDOW_HEIGHT // cell_size
    grid = create_grid(cols, rows, cell_size)
    
    # seeds
    seed_glider(grid, 40, 40)
    seed_blinker(grid, 10, 10)
    seed_block(grid, 60, 60)

    while True:
        SCREEN.fill(WHITE)

        # Step simulation
        future_states = [[False for _ in range(cols)] for _ in range(rows)] # temporary create a grid of Falses states
        for y in range(rows):
            for x in range(cols):
                cell = grid[y][x]
                alive_neighbors = check_alive_neighbors(grid, x, y)

                # Game rules
                if cell.state:
                    future_states[y][x] = (alive_neighbors in [2,3])
                else:
                    future_states[y][x] = (alive_neighbors == 3)

        # Update grid
        for y in range(rows):
            for x in range(cols):
                grid[y][x].state = future_states[y][x]
                grid[y][x].draw(SCREEN)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(10)

if __name__ == "__main__":
    main()