# Game Of Life
import pygame
import sys

# Window, Background & Color
BLACK = (0,0,0)
WHITE = (255,255,255)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

class Cell:
    def __init__(self, x_pos, y_pos, state=False):
        self.state = state # dead or alive
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = 20

    def draw(self, screen):
        color = WHITE if self.state else BLACK
        cell_rect = pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)
        if self.state:
            pygame.draw.rect(screen, color, cell_rect, 0)
        else:
            pygame.draw.rect(screen, color, cell_rect, 0)

# create grid
def drawGrid():
    cell_size = 20
    for x in range(0, WINDOW_WIDTH, cell_size):
        for y in range(0, WINDOW_HEIGHT, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    new_cell = Cell(40,40) #create new cell
    
    while True:
        SCREEN.fill(WHITE)
        drawGrid()
        new_cell.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(30)

if __name__ == "__main__":
    main()