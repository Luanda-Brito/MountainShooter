#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import self

from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self, ):
    print('Setup Start')

    print('Setup End')
    print('Loop Start')
    while True:
        menu = Menu(self.window)
        menu.run()
        pass
    # Check for all events
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit() #Close Window
                #quit() #End PyGame