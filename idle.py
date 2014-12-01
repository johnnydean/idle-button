#!/usr/bin/env python

import sys, pygame, pygbutton
pygame.init()

size = width, height = 1300, 800
light_cyan = 224, 255, 255
black = 0, 0, 0
money = 0
PPS = 0

screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 60)
mainButtonObj = pygbutton.PygButton((500, 375, 300, 200), 'Click Me')
buttonObj1 = pygbutton.PygButton((150, 10, 100, 50), '+1 PPS')
buttonObj2 = pygbutton.PygButton((270, 10, 100, 50), '+3 PPS')
buttonObj3 = pygbutton.PygButton((390, 10, 100, 50), '+5 PPS')
buttonObj4 = pygbutton.PygButton((510, 10, 100, 50), '+10 PPS')
buttonObj5 = pygbutton.PygButton((630, 10, 100, 50), '+50 PPS')
buttonObj6 = pygbutton.PygButton((750, 10, 100, 50), '+100 PPS')
buttonObj7 = pygbutton.PygButton((870, 10, 100, 50), '+500 PPS')
buttonObj8 = pygbutton.PygButton((990, 10, 100, 50), '+1000 PPS')

PPSEVENT = pygame.USEREVENT+1
one_second = 1000
pygame.time.set_timer(PPSEVENT, one_second)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == PPSEVENT:
            money = money + PPS
        if 'click' in mainButtonObj.handleEvent(event):
            money = money + 1
        if 'click' in buttonObj1.handleEvent(event):
            if money >= 19:
                PPS = PPS + 1
                money = money - 19
        if 'click' in buttonObj2.handleEvent(event):
            if money >= 57:
                PPS = PPS + 3
                money = money - 57
        if 'click' in buttonObj3.handleEvent(event):
            if money >= 95:
                PPS = PPS + 5
                money = money - 95
        if 'click' in buttonObj4.handleEvent(event):
            if money >= 190:
                PPS = PPS + 10
                money = money - 190
        if 'click' in buttonObj5.handleEvent(event):
            if money >= 950:
                PPS = PPS + 50
                money = money - 950
        if 'click' in buttonObj6.handleEvent(event):
            if money >= 1900:
                PPS = PPS + 100
                money = money - 1900
        if 'click' in buttonObj7.handleEvent(event):
            if money >= 9500:
                PPS = PPS + 500
                money = money - 9500
        if 'click' in buttonObj8.handleEvent(event):
            if money >= 19000:
                PPS = PPS + 1000
                money = money - 19000

    screen.fill(light_cyan)
    text = font.render("Money: " + str(money) , True, black)
    text2 = font.render("PPS: " + str(PPS) , True, black)
    screen.blit(text, (500, 200))
    screen.blit(text2, (500, 150))
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
        
