__author__ = 'Al Sweigart,Jason Crockett'

import pygame,sys
from pygame.locals import *

WIDGETORAPPNAME = "Activate Launcher"
#global FULLSCREENSTATE

#FULLSCREENSTATE = False
pygame.init()
DISPLAYSURF = pygame.display.set_mode((640,480))
pygame.display.set_caption(WIDGETORAPPNAME)

# Functions go here below:
def toggle_fullDISPLAYSURF():
    # source: www.pygame.org - Function credits:
    # Philhassey & Illume
    # Added two lines to preserve the cursor shape as well. - Duoas

    #DISPLAYSURF = DISPLAYSURF
    DISPLAYSURF = pygame.display.get_surface()
    tmp = DISPLAYSURF.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007

    w,h = DISPLAYSURF.get_width(),DISPLAYSURF.get_height()
    flags = DISPLAYSURF.get_flags()
    bits = DISPLAYSURF.get_bitsize()

    pygame.display.quit()
    pygame.display.init()
    
    #if event.type == KEYDOWN and event.key == K_F11:
    DISPLAYSURF = pygame.display.set_mode((w,h),flags^FULLDISPLAYSURF,bits)
    DISPLAYSURF.blit(tmp,(0,0))
    pygame.display.set_caption(WIDGETORAPPNAME)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007

    return DISPLAYSURF #which is a pygame display

def load_image():
    Image = pygame.image.load("/home/jason/PycharmProjects/ActivateLauncher/Resources/Default/Background.png")
    Image.convert()
    #DISPLAYSURF.blit(Image,(0,0)) #put image onscreen
    #pygame.display.flip() # possibly needed.
    return Image

while True: # put game logic and functions in this loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_F11: # The Keypress Boilerplate line! The Powah!
            screen = toggle_fullscreen() # problem lines

        #add extra events above.

    #the leave the below lines alone
    #screen = pygame.display.get_surface() # safe line

    DISPLAYSURF.blit(DISPLAYSURF.convert)
    #load_image()
    pygame.display.update()
    pygame.display.flip() # possible extra needed.

