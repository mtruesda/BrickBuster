# imports
import pygame

def main():
    # initialize the module
    pygame.init()
    # set window caption
    pygame.set_caption("blockbuster")
    # set window icon
    # pygame.set_icon("file")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))
    # main loop controller
    running = true

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

main()

