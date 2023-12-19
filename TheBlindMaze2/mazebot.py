from pygame.locals import *
import pygame
import sys
from fsm import FSM

class MazeBot(pygame.sprite.Sprite):
    SOUTH, EAST, NORTH, WEST, BSOUTH, BEAST, BNORTH, BWEST, GAMEOVER = 0, 1, 2, 3, 4, 5, 6, 7, 8

    def __init__(self, game, x=50, y=50):
        super().__init__()

        self.game = game

        # Load initial image
        self.image = pygame.image.load("assets/images/bot.png")
        self.rect = self.image.get_rect()

        # Set rectangle
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.centerx = x
        self.rect.centery = y

        # The map of the maze
        self.maze = self.game.txt_grid

        # The route the bot will take to get to the $
        self.path = []

        # TODO: Create the Bot's finite state machine (self.fsm) with initial state
        self.fsm = FSM(self.SOUTH)
        self.init_fsm()
    
    def init_fsm(self):
        # TODO: Add the state transitions
        moves = [self.move_south, self.move_east, self.move_north, self.move_west]
        # states = ["SOUTH", "EAST", "NORTH", "WEST", "BSOUTH", "BEAST", "BNORTH", "BWEST"]
        # this is just to visualize for input states: 0, 1, 2... 7
        for i in range(4):
            self.fsm.add_transition(" ", i, moves[i], i)
            self.fsm.add_transition(" ", i+4, moves[i], i+4)


            # self.fsm.add_transition("#", i, moves[(i+1)%4], (i+1)%4)
            # self.fsm.add_transition("#", i+4, moves[((i+1)%4)], ((i+1)%4)+4)

            self.fsm.add_transition("#", i, None, (i+1)%4)
            self.fsm.add_transition("#", i+4, None, ((i+1)%4)+4)
            

            self.fsm.add_transition("$", i, moves[i], 8)
            self.fsm.add_transition("$", i+4, moves[i], 8)

        for i in range(7):
            if i < 4:
                self.fsm.add_transition("B", i, moves[i], i+4)
                self.fsm.add_transition("X", i, None, (i+1)%4)

            if i >= 4:
                self.fsm.add_transition("B", i, moves[i-4], i-4)
                self.fsm.add_transition("X", i, moves[i-4], i)

            
    
    def get_state(self):
        # TODO: Return the maze bot's current state
        return self.fsm.current_state
    
    def move_south(self):
        """
        Changes the bot's location 1 spot South
        and records the movement in self.path
        """
        self.rect.centery += self.game.SPACING
        self.path.append("SOUTH")

    def move_east(self):
        """
        Changes the bot's location 1 spot East
        and records the movement in self.path
        """
        self.rect.centerx += self.game.SPACING
        self.path.append("EAST")

    def move_north(self):
        """
        Changes the bot's location 1 spot North
        and records the movement in self.path
        """
        self.rect.centery -= self.game.SPACING
        self.path.append("NORTH")

    def move_west(self):
        """
        Changes the bot's location 1 spot West
        and records the movement in self.path
        """
        self.rect.centerx -= self.game.SPACING
        self.path.append("WEST")
    
    def get_next_space(self):
        """
        Uses the bot's current state to determine the next 
        space in the maze the bot would go to. The next 
        space is returned as a String from self.maze.

        Ex. If the bot is facing South, you should get 
        the character one row down from you.

        Returns:
            String: The next character in the maze the bot could go to
        """

        # This is the current x and y indices of the bot in the maze
        grid_x = self.rect.centerx // self.game.SPACING
        grid_y = self.rect.centery // self.game.SPACING

        # TODO: Use the bot's current state to determine
        # what the next maze location value is
        state = self.get_state() #this returns int between 0-7. This method denotes what these nums mean
        
        # #South
        # if state==0 or state-4 == 0:
        #     return self.maze[grid_y+1][grid_x]
        
        # #East
        # if state==1 or state-4 == 1:
        #     return self.maze[grid_y][grid_x+1]
        
        # #North
        # if state==2 or state-4 == 2:
        #     return self.maze[grid_y-1][grid_x]
        
        # #West
        # if state==3 or state-4 == 3:
        #     return self.maze[grid_y][grid_x-1]
        
        # if state == 8:
        #     return self.maze[grid_y][grid_x]

        # Attempted user inputs function, to check what the user is pressing to correspond to that motion on the screen
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #South
                if evenement.type == KEYDOWN and evenement.key == K_DOWN:
                    return self.maze[grid_y+1][grid_x]
            
            #East
                if evenement.type == KEYDOWN and evenement.key == K_RIGHT:
                    return self.maze[grid_y][grid_x+1]
                
                #North
                if evenement.type == KEYDOWN and evenement.key == K_UP:
                    return self.maze[grid_y-1][grid_x]
                
                #West
                if evenement.type == KEYDOWN and evenement.key == K_LEFT:
                    return self.maze[grid_y][grid_x-1]
            
    
    # Getters for where the bot is on the maze
    def get_grid_x(self):
        grid_x = self.rect.centerx // self.game.SPACING
        return grid_x
    
    def get_grid_y(self):
        grid_y = self.rect.centerx // self.game.SPACING
        return grid_y
    
    def update(self):
        # TODO: Use the finite state machine to process input
        self.fsm.process(self.get_next_space())

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))