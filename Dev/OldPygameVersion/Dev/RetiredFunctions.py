__author__ = 'Jason Crockett'
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

    return screen # which is a pygame display

def get_background_images(): #old version
    UserHome = str(expanduser("~")) # get user home folder
    # ^ works on windows and mac too. prints with no "/" on the end

    try: #try and make a Pictures folder location string.
        assert(isinstance(UserHome,str))
        PicturesFolder = UserHome + "/Pictures" #is a string
    except AssertionError:
        print("Userhome is not a string!")

    PicturesFullPathList = []

    try: # try to load images in the pictures folder string.
        for file in os.listdir(PicturesFolder):
            assert(file is type(str())) #file hopefully is a string
            PicturesFullPath = PicturesFolder + file
            PicturesFullPathList.append(PicturesFullPath)
    except TypeError:
        print("a filename in os.listdir is not a string, is it the actual file? ") # oh *uck it isnt.
    """
    #warning.. this code is ram hungry insanity mode
    PygamePictureBinarys = []

    for file in PicturesFullPathList:
        PictureBinary = pygame.image.load(file)
        PygamePictureBinarys.append(PictureBinary)

    return
    """
    return PicturesFullPathList