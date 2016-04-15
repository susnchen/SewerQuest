import collision, constants as c

class Bullet:
    def __init__(self,playerpos,playerfacing):
        self.x = int(playerpos[0]/16)*16
        self.y = int(playerpos[1]/16)*16
        self.playerfacing = playerfacing
        self.timeBetweenBullet = 0
        self.bulletimg = c.bulletd

    def movement(self):
        if self.playerfacing == "right":
            self.bulletimg = c.bulletr
            self.x += 16

        elif self.playerfacing == "down":
            self.bulletimg = c.bulletd
            self.y += 16

        elif self.playerfacing == "up":
            self.bulletimg = c.bulletu
            self.y -= 16

        elif self.playerfacing == "left":
            self.bulletimg = c.bulletl
            self.x -= 16

        self.timeBetweenBullet += 1

    def collide(self):

        col = collision.Collision((self.x,self.y))
        colList = col.checkCollision(c.obstacleList)
        collided = False

        if self.playerfacing in colList:
            collided = True
            print("a")

        return collided