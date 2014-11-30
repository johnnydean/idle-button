#!/usr/bin/env python

import sys, pygame
pygame.init()

size = width, height = 1300, 800
light_cyan = 224,255,255

screen = pygame.display.set_mode(size)

while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    screen.fill(light_cyan)
    pygame.display.flip()
        
