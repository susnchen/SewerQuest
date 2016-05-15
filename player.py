# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# player.py
# contains a Player class that has the player health, position, and sprites and are able to update these variables

# input: room numbers as int and position as tuple
# output: updates player image as a pygame surface, health as an int, and position as a tuple

import pygame
import collision
import constants as c

class Player:
    def __init__(self):
        #intial variables such as position health and sprite of the player
        self.y = 64
        self.x = 32

        self.health = 3

        # the curSpriteSheet gets a list of all images of this state from the dictionary
        self.spriteCount = 0
        self.curSpriteSheet = c.playerSprites["idlel"]
        self.img = self.curSpriteSheet[0]

        #timeBetweenSprite variable will be use to so sprites do not loop too fast
        self.timeBetweenSprite = 0

        self.facing = "down"

    def movement(self,curRoom):
        keys = pygame.key.get_pressed()

        #idle will remain true if no movement keys are pressed
        idle = True

        #gets a list of collisions from the waterList and obstacleList using the checkCollision function
        colList = collision.checkCollision((self.x,self.y),curRoom.obstacleList)
        colList += collision.checkCollision((self.x, self.y), curRoom.waterList)

        #if up keys is pressed
        if keys[pygame.K_w]:
            #idle is no longer True
            idle = False

            #update the state of the sprite sheet
            self.curSpriteSheet = c.playerSprites["right"]
            self.facing = "up"

            #checks if there is something above the player and if not, move the player
            if "up" not in colList:
                #disable movement to the left and right if the up key is pressed and the player is at the tip of the bottom left or right of an object (this handles diagonal movement)
                if "upleft" in colList and keys[pygame.K_a]:
                    colList += ["left"]

                elif "upright" in colList and keys[pygame.K_d]:
                    colList += ["right"]

                self.y -= 8

        #repeat this with all other keys
        if keys[pygame.K_s]:
            idle = False
            self.curSpriteSheet = c.playerSprites["left"]
            self.facing = "down"

            if "down" not in colList:
                if "downleft" in colList and keys[pygame.K_a]:
                    colList += ["left"]

                elif "downright" in colList and keys[pygame.K_d]:
                    colList += ["right"]

                self.y += 8

        if keys[pygame.K_a]:
            idle = False
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

        #if no keys were pressed
        elif idle:
            #switch the sprite sheet to idle according to the facing of the player
            if self.facing == "right" or self.facing == "up":
                self.curSpriteSheet = c.playerSprites["idler"]

            elif self.facing == "left" or self.facing == "down":
                self.curSpriteSheet = c.playerSprites["idlel"]

        #updates the player sprite after a certain amount of time has past
        self.timeBetweenSprite += 1
        if self.timeBetweenSprite >= 10:
            self.updateSprite()
            self.timeBetweenSprite = 0

    def updateSprite(self):
        #checks if the sprite counter reaches the end of the sprite sheet
        if self.spriteCount == len(self.curSpriteSheet):
            #reset the counter
            self.spriteCount = 0

        #update the image
        self.img = self.curSpriteSheet[self.spriteCount]
        self.spriteCount += 1