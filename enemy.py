import constants as c
import collision

class Enemy:
    def __init__(self, strength, spd, x, y):
        self.spd = spd
        self.x = x
        self.y = y
        self.strength = strength
        self.img = c.enemyimg
        self.timeBetweenEnemy = 0

    def movement(self,playerpos,curRoom):
        #pathfinder.pathfind(curRoom,(self.x,self.y),playerpos)

        playerx = playerpos[0]
        playery = playerpos[1]

        colList = collision.checkCollision((self.x,self.y),curRoom.obstacleList)
        #rats aren't scared of water, therefore they can walk over water
        #colList += collision.checkCollision((self.x,self.y),curRoom.waterList)

        if self.y > playery and "up" not in colList:# and dy >= dx:
            if "upleft" in colList:
                colList += ["left"]

            elif "upright" in colList:
                colList += ["right"]

            self.y -= self.spd

        if self.y < playery and "down" not in colList:# and dy >= dx:
            if "downleft" in colList:
                colList += ["left"]

            elif "downright" in colList:
                colList += ["right"]

            self.y += self.spd

        if self.x < playerx and "right" not in colList:# and dx >= dy:
            self.x += self.spd

        if self.x > playerx and "left" not in colList:# and dx >= dy:
            self.x -= self.spd

    def deathCollision(self,bulletList):
        death = False
        deathBullet = None

        for i in bulletList:
            death = collision.objectCollider((self.x,self.y),(i.x,i.y),5,5)
            deathBullet = i

        return death,deathBullet

    def playerCollision(self,playerpos):
        return collision.objectCollider((self.x,self.y),(playerpos))

