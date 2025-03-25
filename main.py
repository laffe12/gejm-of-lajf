# Game Of Life
import pygame
import sys
import random

# Window, Background & Color
BLACK = (0,0,0)
WHITE = (255,255,255)
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1500
cell_size = 15

class Cell:
    def __init__(self, x_pos, y_pos, state=False):
        self.state = state # dead or alive
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = 20

    def draw(self, screen):
        color = WHITE if self.state else BLACK
        cell_rect = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)
        pygame.draw.rect(screen, color, cell_rect)
        pygame.draw.rect(screen, (50,50,50), cell_rect, 1) # grid lines

def create_grid(cols, rows, cell_size):
    grid = []
    for x in range(cols):
        row = []
        for y in range(rows):
            x_pos = x * cell_size
            y_pos = y * cell_size
            row.append(Cell(x_pos, y_pos))
        grid.append(row)
    return grid

def check_alive_neighbors(grid, x_pos, y_pos):
    height = len(grid)
    width = len(grid[0])
    neight_count = 0
    # Toroidal wrapping where grid wraps around the edges
    directions = [
        (-1,-1), (0,-1), (1,-1),
        (-1, 0),         (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    for dx, dy in directions:
        x_neighbor = (x_pos + dx + width) % width
        y_neighbor = (y_pos + dy + height) % height
        if grid[x_neighbor, y_neighbor].state:
            neight_count += 1
    return neight_count

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

    while True:
        SCREEN.fill(WHITE)

        # draw grid
        for row in grid:
            for cell in row:
                cell.state = random.choice([True, False])
                cell.draw(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(10)

if __name__ == "__main__":
    main()