import pygame
import random

# Constants
WIDTH, HEIGHT = 640, 480
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS, HEIGHT // ROWS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Maze class to generate and display the maze
class Maze:
    def __init__(self):
        self.grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]
        self.visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def generate_maze(self, row, col):
        self.visited[row][col] = True
        directions = random.sample(self.directions, len(self.directions))

        for dr, dc in directions:
            new_row, new_col = row + 2 * dr, col + 2 * dc

            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                if not self.visited[new_row][new_col]:
                    self.grid[new_row][new_col] = 0  # passage
                    self.grid[row + dr][col + dc] = 0  # passage
                    self.generate_maze(new_row, new_col)

    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(screen, BLACK, (col * CELL_SIZE[0], row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))
                elif self.grid[row][col] == 0:
                    pygame.draw.rect(screen, WHITE, (col * CELL_SIZE[0], row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))

# Player class to handle player movements
class Player:
    def __init__(self, maze):
        self.maze = maze
        self.row, self.col = 1, 1

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.col * CELL_SIZE[0], self.row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))

    def move(self, dx, dy):
        if self.maze.grid[self.row + dy][self.col + dx] != 1:
            self.row += dy
            self.col += dx

# Main function to run the game
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Maze Game')

    maze = Maze()
    maze.generate_maze(1, 1)

    player = Player(maze)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    player.move(0, 1)
                elif event.key == pygame.K_LEFT:
                    player.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    player.move(1, 0)

        screen.fill(BLUE)
        maze.draw(screen)
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()