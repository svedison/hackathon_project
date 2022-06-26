import pygame
from settings import *




class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.smoothscale((self.image), (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-28, -15)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacles_sprites = obstacles_sprites


    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center 

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top   #up is negative and down is positive, shout out to mr.nemes!
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom


    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    def update(self):
        self.input()
        self.move(self.speed)

