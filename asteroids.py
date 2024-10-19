from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255), (self.position.x,self.position.y), radius=self.radius,width=2)
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            angle = random.uniform(20,50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            self.kill()
            asteroid_1 = Asteroid(self.position.x,self.position.y, new_rad)
            asteroid_2 = Asteroid(self.position.x,self.position.y, new_rad)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2
            
            
            
