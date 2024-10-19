# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import os
import math
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def main():
    #Starting App
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Global Variables
    score = 0
    score_increment = 10
    multiplier = 1
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    #Init Pygame variables and things
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
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

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Initalize variables every frame
        font = pygame.font.Font(None, 36)
        dt = clock.tick(60) / 1000.0
        screen.fill((0,0,0), rect=None)
        #Draw and update Game
        for thing in drawable:
            thing.draw(screen)
        for thing in updateable:
            thing.update(dt)
        #Update Score
        score += math.ceil((score_increment * dt) * 100) / 100
        score = math.ceil(score * 100) / 100

        #Render Score
        multiplier_text = font.render(f"Multiplier: {multiplier}", True, (255,255,255))
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(multiplier_text, (200,10))

        #Check For Collisions
        for thing in asteroids:
            if player.collision(thing) == True:
                pygame.display.flip()
                screen.fill((0,0,0), rect=None)
                end_screen(score_text,score)
                #raise SystemExit(f"Game over!-- Score: {score}")
            for bullet in shots:
                if bullet.collision(thing):
                    multiplier += .1
                    multiplier = math.ceil(multiplier * 100) / 100
                    thing.split()
                    bullet.kill()
        #Refresh Screen
        pygame.display.flip()

def end_screen(score_text, score):
    while True:
        pygame.display.flip()
        screen.fill((0,0,0), rect=None)
        screen.blit(score_text, ((SCREEN_WIDTH/2) - 50, (SCREEN_HEIGHT/2)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(f"Game over!-- Score: {score}")
            if event.type == pygame.KEYDOWN:
                raise SystemExit(f"Game over!-- Score: {score}")
                # [...]

        
if __name__ == "__main__":
    main()
