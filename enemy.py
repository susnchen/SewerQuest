import constants as c
import collision

class Enemy:
    def __init__(self, strength, spd, x, y):
        self.spd = spd
        self.x = x
        self.y = y
        self.strength = strength
        self.timeBetweenEnemy = 0

        # the curSpriteSheet gets a list of all images of this state from the dictionary
        self.spriteCount = 0
        self.curSpriteSheet = c.enemySprites["down"]
        self.img = self.curSpriteSheet[0]

        #timeBetweenSprite variable will be use to so sprites do not loop too fast
        self.timeBetweenSprite = 0

    def movement(self,playerpos,curRoom):

        playerx = playerpos[0]
        playery = playerpos[1]

        colList = collision.checkCollision((self.x,self.y),curRoom.obstacleList)
        #rats aren't scared of water, therefore they can walk over water

        if self.y > playery and "up" not in colList:# and dy >= dx:
            if "upleft" in colList:
                colList += ["left"]

            elif "upright" in colList:
                colList += ["right"]

            self.y -= self.spd

            self.curSpriteSheet = c.enemySprites["up"]

        if self.y < playery and "down" not in colList:# and dy >= dx:
            if "downleft" in colList:
                colList += ["left"]

            elif "downright" in colList:
                colList += ["right"]

            self.y += self.spd

            self.curSpriteSheet = c.enemySprites["down"]

        if self.x < playerx and "right" not in colList:# and dx >= dy:
            self.x += self.spd
            self.curSpriteSheet = c.enemySprites["right"]

        if self.x > playerx and "left" not in colList:# and dx >= dy:
            self.x -= self.spd
            self.curSpriteSheet = c.enemySprites["left"]

        #updates the player sprite after a certain amount of time has past
        self.timeBetweenSprite += 1
        if self.timeBetweenSprite >= 2:
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

    def deathCollision(self,bulletList):
        death = False
        deathBullet = None

        for i in bulletList:
            death = collision.spritesCollision((self.x,self.y),(i.x,i.y),5,5)
            deathBullet = i

        return death,deathBullet

    def playerCollision(self,playerpos):
        return collision.spritesCollision((self.x,self.y),(playerpos))

