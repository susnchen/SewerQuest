import pygame
import collision
import constants as c

class Player:
    def __init__(self):
        self.y = 64
        self.x = 32

        self.health = 3

        self.spriteCount = 0
        self.curSpriteSheet = c.playerSprites["idlel"]
        self.img = self.curSpriteSheet[0]

        self.facing = "down"

    def movement(self,curRoom):
        print(self.curSpriteSheet)
        if self.spriteCount == len(self.curSpriteSheet):
            self.spriteCount = 0

        keys = pygame.key.get_pressed()

        idle = True

        colList = collision.checkCollision((self.x,self.y),curRoom.obstacleList)
        colList += collision.checkCollision((self.x, self.y), curRoom.waterList)

        if keys[pygame.K_w]:
            idle = False
            self.curSpriteSheet = c.playerSprites["up"]
            self.facing = "up"

            if "up" not in colList:
                if "upleft" in colList and keys[pygame.K_a]:
                    colList += ["left"]

                elif "upright" in colList and keys[pygame.K_d]:
                    colList += ["right"]

                self.y -= 8

        if keys[pygame.K_s]:
            idle = False
            self.curSpriteSheet = c.playerSprites["down"]
            self.facing = "down"

            if "down" not in colList:
                if "downleft" in colList and keys[pygame.K_a]:
                    colList += ["left"]

                elif "downright" in colList and keys[pygame.K_d]:
                    colList += ["right"]

                self.y += 8

        if keys[pygame.K_a]:
            idle = False
            print("left")
            self.curSpriteSheet = c.playerSprites["left"]
            self.facing = "left"

            if "left" not in colList:
                self.x -= 8

        if keys[pygame.K_d]:
            idle = False
            self.curSpriteSheet = c.playerSprites["right"]
            self.facing = "right"

            if "right" not in colList:
                self.x += 8

        elif idle:
            if self.facing == "right" or self.facing == "up":
                print("else")
                self.curSpriteSheet = c.playerSprites["idler"]
            elif self.facing == "left" or self.facing == "down":
                print("else")
                self.curSpriteSheet = c.playerSprites["idlel"]

        self.img = self.curSpriteSheet[self.spriteCount]
        self.spriteCount += 1

    def move(self,pos):
        self.x = pos[0]
        self.y = pos[1]
