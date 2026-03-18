# bonjour a tous je suis J et mon ami koustubh

print("Hello World")


import sys 
import pygame 

class Tetris:
  # this is an overall class to manage game assests and behaviour 

  def __init__(self):
    #initalize game and create resources
    pygame.init()
    self.screen = pygame.display.set_mode((1920,1080)
    pygame.display.set_caption("TETRIS")


    # for now i have added a main class thats tertris and a def that has screen resolution and when th game opens its shows tetris on its above an drecent apps
