# bonjour a tous je suis J et mon ami koustubh

import sys 
import pygame

# what i have done currently: (i will remove this comment on my next updation)
# 1. made a window object of the class Tetris
# 2. applied a while loop to display the screen and 
#    just checked using draw rect function that is the loop working or not.

# Waiting for the list of buttons from sarvesh which i will add in the homescreen

class Tetris:
    # this is an overall class to manage game assests and behaviour 

    def __init__(self):
        #initalize game and create resources
        pygame.init()
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("TETRIS")


        # for now i have added a main class thats tertris and a def that has screen resolution and when th game opens its shows tetris on its above an drecent apps



window = Tetris()
running = True

list_of_buttons = [0,1,2,3,4,5] #sarvesh has to name them

while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            # (temporary) draws white squares on the position of mouse click of size 50,50
            x,y = pygame.mouse.get_pos()
            pygame.draw.rect(window.screen,(255,255,255),(x,y,50,50))
            pass

        if list_of_buttons == 1:
            # move to gamepage
            pass
    
    pygame.display.update()

pygame.quit()
sys.exit()
    


