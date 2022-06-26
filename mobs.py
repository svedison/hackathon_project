import pygame
import math
from settings import *
from player import Player


class Mob(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        self.image = pygame.image.load('mob1.png').convert_alpha()
        self.image = pygame.transform.smoothscale((self.image), (64, 64))
        self.rect = self.image.get_rect(topleft = (0, 0))
        
     
  

    def update(self):
        self.rect.x += 1

    def aggro(self, x, y):
        range = None
        coor = [self.rect.x, self.rect.y]
        ecoor = [x, y]
        if(math.dist(coor, ecoor) > range):
            return True
# still working on attack
    def attack(self, xs, ys):
        range = None
        coor = [self.rect.x, self.rect.y]
        ecoor = [xs, ys]
        if(math.dist(coor, ecoor) > range):
            return True
        return False

    
    
    def damage(self, x):
        self.hp -= x
        if(self.hp <= 0):

            self.kill()
            self.score+=1
            return True
        return False

    #make the mob move towards the player
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        if(self.rect.x < 0):
            self.rect.x = 0
        if(self.rect.y < 0):
            self.rect.y = 0
        if(self.rect.x > WIDTH):
            self.rect.x = WIDTH
        if(self.rect.y > HEIGHT):
            self.rect.y = HEIGHT
