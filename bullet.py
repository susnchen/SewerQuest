import collision, constants as c

class Bullet:
    def __init__(self,playerpos,direction):
        self.x = playerpos[0]+13
        self.y = playerpos[1]+13
        self.direction = direction
        self.timeBetweenBullet = 0
        self.bulletimg = c.bulletd

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