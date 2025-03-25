# Game Of Life
import pygame
import sys

# Window, Background & Color
BLACK = (0,0,0)
WHITE = (200,200,200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800


class Cell:
    def __init__(self, x_pos, y_pos, state):
        self.state = state # state 0 or 1 (dead or alive)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = 20

# create grid
def drawGrid():
    cell_size = 20
    for x in range(0, WINDOW_WIDTH, cell_size):
        for y in range(0, WINDOW_HEIGHT, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

# create cell
def drawCell(cell):
    cell_rect = pygame.Rect(cell.x_pos, cell.y_pos, cell.size, cell.size)
    if cell.state == 0:
        pygame.draw.rect(SCREEN, BLACK, cell_rect, 0)
    else:
        pygame.draw.rect(SCREEN, WHITE, cell_rect, 0)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    new_cell = Cell(121, 400, 0) #create new cell

    while True:
        SCREEN.fill(WHITE)
        drawGrid()
        drawCell(new_cell)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(30)

if __name__ == "__main__":
    main()