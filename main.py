# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def main():
    BLACK = pygame.Color(0,0,0)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None)
        pygame.display.flip()

if __name__ == "__main__":
    main()