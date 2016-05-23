import constants as c
import collision

class Enemy:
    def __init__(self, spd, x, y):
        #initial variables such as speed and position of the enemy
        self.spd = spd
        self.x = x
        self.y = y

        #the timeBetweenEnemy variable is used to make a delay between everytime the movement function is called
        self.timeBetweenEnemy = 0

        # the curSpriteSheet gets a list of all images of this state from the dictionary
        self.spriteCount = 0
        self.curSpriteSheet = c.enemySprites["down"]
        self.img = self.curSpriteSheet[0]

        #timeBetweenSprite variable will be use to so sprites do not loop too fast
        self.timeBetweenSprite = 0

    #movement function, updates the enemy's position according to the player position
    def movement(self,playerpos,curRoom):
        playerx = playerpos[0]
        playery = playerpos[1]

        #checks collisions of the rat with all the walls in the room
        #rats aren't scared of water, therefore they can walk over water
        colList = collision.checkCollision((self.x,self.y),curRoom.obstacleList)

        #if player is above enemy and enemy is able to move up
        if self.y > playery and "up" not in colList:
            #checks the diagonals of the enemy and disables ability to go left or right if they're trying to go diagonal
            if "upleft" in colList:
                colList += ["left"]

            elif "upright" in colList:
                colList += ["right"]

            self.y -= self.spd

            #set current sprite sheet with the state of up
            self.curSpriteSheet = c.enemySprites["up"]

        #repeat if player is beneath enemy
        if self.y < playery and "down" not in colList:
            if "downleft" in colList:
                colList += ["left"]

            elif "downright" in colList:
                colList += ["right"]

            self.y += self.spd

            self.curSpriteSheet = c.enemySprites["down"]

        #repeat if player is to the right
        if self.x < playerx and "right" not in colList:#
            self.x += self.spd
            self.curSpriteSheet = c.enemySprites["right"]

        #repeat if player is to the left
        if self.x > playerx and "left" not in colList:
            self.x -= self.spd
            self.curSpriteSheet = c.enemySprites["left"]

        #updates the player sprite after a certain amount of time has past
        self.timeBetweenSprite += 1
        if self.timeBetweenSprite >= 2:
            self.updateSprite()
            self.timeBetweenSprite = 0

    #updates the sprite
    def updateSprite(self):
        #checks if the sprite counter reaches the end of the sprite sheet
        if self.spriteCount == len(self.curSpriteSheet):
            #reset the counter
            self.spriteCount = 0

        #update the image
        self.img = self.curSpriteSheet[self.spriteCount]
        self.spriteCount += 1

    #checks if the enemy collides with a bullet
    def deathCollision(self,bulletList):
        death = False
        deathBullet = None

        #checks all the bullet in the bulletList
        for i in bulletList:
            death = collision.spritesCollision((self.x,self.y),(i.x,i.y),5,5)
            deathBullet = i

        #return true if enemy collides with a bullet and the bullet object that did
        return death,deathBullet

    #checks if the enemy collides with the player
    def playerCollision(self,playerpos):
       #if enemy collides with player, the player will lose health
        return collision.spritesCollision((self.x,self.y),(playerpos))

