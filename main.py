# bonjour a tous je suis J et mon ami koustubh

import sys 
import pygame
import constants

# what i have done currently: (i will remove this comment on my next updation)
# 1. added three buttons (not working currently) but with a hover feature.

class Tetris:
    # this is an overall class to manage game assests and behaviour 

    def __init__(self):
        #initalize game and create resources
        pygame.init()
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("TETRIS")
        self.font = pygame.font.Font('freesansbold.ttf',20) # fonts added


        # for now i have added a main class thats tertris and a def that has screen resolution and when th game opens its shows tetris on its above an drecent apps

class Buttons:
    def __init__(self,name,pos_x,pos_y,width,height):
        self.name = name
        self.x = pos_x
        self.y = pos_y
        self.w = width
        self.h = height
        self.hover = 0
        self.state = 0

        self.button_rect = pygame.rect.Rect((self.x,self.y),(self.w,self.h))

    def draw_buttons(self):
        pygame.draw.rect(window.screen, constants.YELLOW, (self.x - 10,self.y - 10,self.w + 20,self.h + 20)) # border
        pygame.draw.rect(window.screen, constants.WHITE, (self.x,self.y,self.w,self.h))

        if self.hover == 1:
            pygame.draw.rect(window.screen, constants.GREEN, (self.x,self.y,self.w,self.h))

        button_text = window.font.render(self.name,True,constants.BLACK)
        window.screen.blit(button_text,(self.x, self.y))

    

window = Tetris()
running = True


new_game = Buttons('NEW GAME',100,100,200,60)
records = Buttons('RECORDS',100,200,200,60)
settings = Buttons('SETTINGS',100,300,200,60)

while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_pos = pygame.mouse.get_pos()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            # (temporary) draws white squares on the position of mouse click of size 50,50
            x,y = mouse_pos[0],mouse_pos[1]
            pygame.draw.rect(window.screen,(255,255,255),(x,y,50,50))
            pass
        
        if mouse_pos and new_game.button_rect.collidepoint(mouse_pos):
            new_game.hover = 1
        else:
            new_game.hover = 0
        
        if mouse_pos and records.button_rect.collidepoint(mouse_pos):
            records.hover = 1
        else:
            records.hover = 0
        
        if mouse_pos and settings.button_rect.collidepoint(mouse_pos):
            settings.hover = 1
        else:
            settings.hover = 0
        

        
    
    new_game.draw_buttons()
    records.draw_buttons()
    settings.draw_buttons()
    pygame.display.update()

pygame.quit()
sys.exit()
    


