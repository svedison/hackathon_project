import pygame
from settings import *




class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)    
        self.image = pygame.image.load('stonewall.png').convert_alpha()
        self.image = pygame.transform.smoothscale((self.image), (64, 64)) 
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        