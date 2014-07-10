__author__ = 'Al Sweigart,Jason Crockett'

import pygame,sys
from pygame.locals import *

WIDGETORAPPNAME = "Activate Launcher"

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640,480))
pygame.display.set_caption(WIDGETORAPPNAME)

# Functions go here below:
def toggle_fullscreen():
    # source: www.pygame.org - Function credits:
    # Philhassey & Illume
    # Added two lines to preserve the cursor shape as well. - Duoas
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007

    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()

    pygame.display.quit()
    pygame.display.init()

    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(WIDGETORAPPNAME)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007

    return screen #which is a pygame display


while True: # put game logic and functions in this loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            sys.exit()
        if event.type == KEYDOWN and event.key == K_F11: # The Keypress Boilerplate line! The Powah!
            toggle_fullscreen() # problem lines

        #add extra events above.

    #the leave the below lines alone
    screen = pygame.display.get_surface() # problem lines
    pygame.display.update()
    #pygame.display.flip() # possible extra needed.

