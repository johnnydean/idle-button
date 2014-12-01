#!/usr/bin/env python

import sys, pygame, pygbutton
pygame.init()

size = width, height = 1300, 800
light_cyan = 224,255,255

screen = pygame.display.set_mode(size)
mainButtonObj = pygbutton.PygButton((500, 375, 300, 200), 'Click Me')
buttonObj1 = pygbutton.PygButton((150, 10, 100, 50), '+1 PPS')
buttonObj2 = pygbutton.PygButton((270, 10, 100, 50), '+3 PPS')
buttonObj3 = pygbutton.PygButton((390, 10, 100, 50), '+5 PPS')
buttonObj4 = pygbutton.PygButton((510, 10, 100, 50), '+10 PPS')
buttonObj5 = pygbutton.PygButton((630, 10, 100, 50), '+50 PPS')
buttonObj6 = pygbutton.PygButton((750, 10, 100, 50), '+100 PPS')
buttonObj7 = pygbutton.PygButton((870, 10, 100, 50), '+500 PPS')
buttonObj8 = pygbutton.PygButton((990, 10, 100, 50), '+1000 PPS')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if 'click' in mainButtonObj.handleEvent(event):
            print "main button clicked"
        if 'click' in buttonObj1.handleEvent(event):
            print "button 1 clicked"
        if 'click' in buttonObj2.handleEvent(event):
            print "button 2 clicked"
        if 'click' in buttonObj3.handleEvent(event):
            print "button 3 clicked"
        if 'click' in buttonObj4.handleEvent(event):
            print "button 4 clicked"
        if 'click' in buttonObj5.handleEvent(event):
            print "button 5 clicked"
        if 'click' in buttonObj6.handleEvent(event):
            print "button 6 clicked"
        if 'click' in buttonObj7.handleEvent(event):
            print "button 7 clicked"
        if 'click' in buttonObj8.handleEvent(event):
            print "button 8 clicked"
            
    screen.fill(light_cyan)
    mainButtonObj.draw(screen)
    buttonObj1.draw(screen)
    buttonObj2.draw(screen)
    buttonObj3.draw(screen)
    buttonObj4.draw(screen)
    buttonObj5.draw(screen)
    buttonObj6.draw(screen)
    buttonObj7.draw(screen)
    buttonObj8.draw(screen)
    pygame.display.flip()
        
