import constants as c
import collision
from math import fabs

class Enemy:
    def __init__(self, strength,type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.strength = strength
        self.img = c.enemyimg

    def movement(self,playerpos,curRoom):
        playerx = playerpos[0]
        playery = playerpos[1]

        dx = fabs(playerx - self.x)
        dy = fabs(playery - self.y)

        colList = collision.checkCollision((self.x,self.y),curRoom.obstacleList)

        if self.x < playerx and "right" not in colList and dx >= dy:
            self.x += 4

        elif self.x > playerx and "left" not in colList and dx >= dy:
            self.x -= 4

        elif self.y > playery and "up" not in colList and dy >= dx:
            self.y -= 4

        elif self.y < playery and "down" not in colList and dy >= dx:
            self.y += 4

    def deathCollision(self,bulletList):
        obj = []
        death = False
        deathBullet = None

        for i in bulletList:
            if collision.objectCollider((self.x,self.y),(i.x,i.y)) == True:
                death = True
                deathBullet = i

        return death,deathBullet

    def playerCollision(self,playerpos):
        return collision.objectCollider((self.x,self.y),(playerpos))

