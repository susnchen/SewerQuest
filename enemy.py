import constants as c
import collision
from math import atan2,pi,fabs

class Enemy:
    def __init__(self, strength,type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.strength = strength
        self.img = c.enemyimg

    def movement(self,playerpos):
        playerx = playerpos[0]
        playery = playerpos[1]

        dx = fabs(playerx-self.x)
        dy =  fabs(playery-self.y)
        '''degrees = atan2(dy,dx)*(180/pi)
        if dy < 0:
            degrees = fabs(degrees)
        elif dy > 0:
            degrees = fabs(degrees-360)'''

        col = collision.Collision((self.x,self.y))
        colList = col.checkCollision(c.obstacleList)

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
        col = collision.Collision((self.x,self.y))
        deathBullet = None

        for i in bulletList:
            if col.enemyCollider((self.x,self.y),(i.x,i.y)) == True:
                death = True
                deathBullet = i

        return death,deathBullet

    def playerCollision(self,playerpos):
        damage = False
        col = collision.Collision((self.x,self.y))

        return col.enemyCollider((self.x,self.y),(playerpos))

