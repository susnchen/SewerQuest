import collision, constants as c
from math import atan2, degrees, pi

class Bullet:
    def __init__(self,playerpos,mousepos):
        self.x = playerpos[0]+13
        self.y = playerpos[1]+13
        self.direction = self.direction(mousepos)
        self.timeBetweenBullet = 0
        self.bulletimg = c.bulletd

    def direction(self,mousepos):
        dx = mousepos[0] - self.x
        dy = mousepos[1] - self.y
        degree = degrees(atan2(-dy,dx))
        direction = 0

        if degree >= -45 and degree < 45:
            direction = "right"
        elif degree >= 45 and degree < 135:
            direction = "up"
        elif degree >= -135 and degree < -45:
            direction = "down"
        elif degree >= 135 or degree > -180:
            direction = "left"
        return direction


    def movement(self):
        if self.direction == "right":
            self.bulletimg = c.bulletr
            self.x += 16

        elif self.direction == "down":
            self.bulletimg = c.bulletd
            self.y += 16

        elif self.direction == "up":
            self.bulletimg = c.bulletu
            self.y -= 16

        elif self.direction == "left":
            self.bulletimg = c.bulletl
            self.x -= 16

        self.timeBetweenBullet += 1

    def collide(self, curRoom):
        collided = False
        obstacleList = curRoom.obstacleList

        for i in obstacleList:
            if collision.objectCollider(i,(self.x,self.y),5,5):
                collided = True

        return collided