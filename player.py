import pygame
import collision
import constants as c

class Player:
    def __init__(self, level):
        self.y = 64
        self.x = 32
        self.health = 3
        self.level = level
        self.spriteCount = 0
        self.default = c.playerdown[0]
        self.img = c.playerdown[0]
        self.facing = "down"

    def death(self):
        if self.health == 0:
            print("game over")
        else:
            print("alive")

    def movement(self,curRoom):

        keys = pygame.key.get_pressed()

        colList = collision.checkCollision((self.x,self.y),curRoom.obstacleList)

        if keys[pygame.K_w]:
            self.facing = "up"

            if keys[pygame.K_z]:
                pass

            self.spriteCount += 1

            if self.spriteCount == 6:
                self.spriteCount = 0

            self.img = c.playerup[self.spriteCount]
            self.default = c.playerup[0]

            if "up" not in colList:
                self.y -= 8

        if keys[pygame.K_s]:
            self.facing = "down"
            self.spriteCount += 1

            if self.spriteCount == 6:
                self.spriteCount = 0

            self.img = c.playerdown[self.spriteCount]
            self.default = c.playerdown[0]

            if "down" not in colList:
                self.y += 8

        if keys[pygame.K_a]:
            self.facing = "left"
            self.spriteCount += 1

            if self.spriteCount == 6:
                self.spriteCount = 0

            self.img = c.playerleft[self.spriteCount]
            self.default = c.playerleft[0]

            if "left" not in colList:
                self.x -= 8

        if keys[pygame.K_d]:
            self.facing = "right"
            self.spriteCount += 1

            if self.spriteCount == 6:
                self.spriteCount = 0

            self.img = c.playerright[self.spriteCount]
            self.default = c.playerright[0]

            if "right" not in colList:
                self.x += 8

        else:
            self.img = self.default

    def hurtSprite(self):
        self.img = self.img.set_alpha()

    def move(self,pos,facing):
        self.x = pos[0]
        self.y = pos[1]
        self.img = pygame.image.load("assets\\images\\"+ facing + "1.png")
        self.default = pygame.image.load("assets\\images\\"+ facing + "1.png")