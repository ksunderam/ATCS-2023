"""
This module implements a Finite State Machine (FSM).

You define an FSM by building a dictionary of transitions. For a given input symbol,
the process() method uses the dictionary to decide what action to call and what
the next state will be. The FSM has a dictionary of transitions that associate the tuples:

        (input_symbol, current_state) --> (action, next_state)

Where "action" is a function you define. The symbols and states can be any
objects. You use the add_transition() method to add to the transition table.

@author: Ms. Namasivayam
@version: 2022
"""


class FSM:
    def __init__(self, initial_state):
        # Dictionary (input_symbol, current_state) --> (action, next_state).
        self.state_transitions = {}
        self.current_state = initial_state

    def add_transition(self, input_symbol, state, action=None, next_state=None):
        """
        Adds a transition to the instance variable state_transitions
        that associates:
            (input_symbol, current_state) --> (action, next_state)

        The action may be set to None in which case the process() method will
        ignore the action and only set the next_state.

        The next_state may be set to None in which case the current state will be unchanged.
        
        Args:
            input_symbol (anything): The input received
            state (anything): The current state
            action (function, optional): The action to take/function to run. Defaults to None.
            next_state (anything, optional): The next state to transition to. Defaults to None.
        """
        # TODO: implement add transition
        self.state_transitions[input_symbol, state] = action, next_state


        # if self.current_state == "r":
        #     next_state = "g"
        #     self.state_transitions[input_symbol]["r"] = action, next_state
        # if self.current_state == "g":
        #     next_state = "y"
        #     self.state_transitions[input_symbol]["g"] = action, next_state
        # if self.current_state == "y":
        #     next_state = "r"
        #     self.state_transitions[input_symbol]["y"] = action, next_state


    def get_transition(self, input_symbol, state):
        """
        Returns tuple (action, next state) given an input_symbol and state.
        Normally you do not call this method directly. It is called by
        process().

        Args:
            input_symbol (anything): The given input symbol
            state (anything): The current state

        Returns:
            tuple: Returns the tuple (action, next_state)
        """
        # TODO: Implement get transition
        return self.state_transitions[input_symbol, state]

    def process(self, input_symbol):
        """
        The main method that you call to process input. This may
        cause the FSM to change state and call an action. This method calls
        get_transition() to find the action and next_state associated with the
        input_symbol and current_state. If the action is None then the action
        is not called and only the current state is changed. This method
        processes one complete input symbol.
        Args:
            input_symbol (anything): The input to process
        """
        # TODO: Implement process
        old_state = self.current_state
        x, self.current_state = self.get_transition(input_symbol, self.current_state)
        if self.current_state == None:
            self.current_state = old_state
        if x != None:
            x()







# import pygame
# import random

# # Constants
# WIDTH, HEIGHT = 640, 480
# ROWS, COLS = 20, 20
# CELL_SIZE = WIDTH // COLS, HEIGHT // ROWS
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)

# # Maze class to generate and display the maze
# class Maze:
#     def __init__(self):
#         self.grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]
#         self.visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
#         self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

#     def generate_maze(self, row, col):
#         self.visited[row][col] = True
#         directions = random.sample(self.directions, len(self.directions))

#         for dr, dc in directions:
#             new_row, new_col = row + 2 * dr, col + 2 * dc

#             if 0 <= new_row < ROWS and 0 <= new_col < COLS:
#                 if not self.visited[new_row][new_col]:
#                     self.grid[new_row][new_col] = 0  # passage
#                     self.grid[row + dr][col + dc] = 0  # passage
#                     self.generate_maze(new_row, new_col)

#     def draw(self, screen):
#         for row in range(ROWS):
#             for col in range(COLS):
#                 if self.grid[row][col] == 1:
#                     pygame.draw.rect(screen, BLACK, (col * CELL_SIZE[0], row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))
#                 elif self.grid[row][col] == 0:
#                     pygame.draw.rect(screen, WHITE, (col * CELL_SIZE[0], row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))

# # Player class to handle player movements
# class Player:
#     def __init__(self, maze):
#         self.maze = maze
#         self.row, self.col = 1, 1

#     def draw(self, screen):
#         pygame.draw.rect(screen, RED, (self.col * CELL_SIZE[0], self.row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))

#     def move(self, dx, dy):
#         if self.maze.grid[self.row + dy][self.col + dx] != 1:
#             self.row += dy
#             self.col += dx

# # Main function to run the game
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption('Maze Game')

#     maze = Maze()
#     maze.generate_maze(1, 1)

#     player = Player(maze)

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     player.move(0, -1)
#                 elif event.key == pygame.K_DOWN:
#                     player.move(0, 1)
#                 elif event.key == pygame.K_LEFT:
#                     player.move(-1, 0)
#                 elif event.key == pygame.K_RIGHT:
#                     player.move(1, 0)

#         screen.fill(BLUE)
#         maze.draw(screen)
#         player.draw(screen)
#         pygame.display.flip()

#     pygame.quit()

# if __name__ == "__main__":
#     main()