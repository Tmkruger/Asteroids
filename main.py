# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def main():
    BLACK = pygame.Color(0,0,0)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    asteroidfield = AsteroidField()
    player = Player(x,y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0
        screen.fill((0,0,0), rect=None)
        for thing in drawable:
            thing.draw(screen)
        for thing in updateable:
            thing.update(dt)
        for thing in asteroids:
            if player.collision(thing) == True:
                raise SystemExit("Game over!")
            for bullet in shots:
                if bullet.collision(thing):
                    thing.split()
                    bullet.kill()
        pygame.display.flip()

if __name__ == "__main__":
    main()
