
# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# bullet.py
# contains a class that will control a bullet's motion and collision

# input: player position and mouse position as tuples
# output: position and direction of bullet 

import collision, constants as c
from math import atan2, degrees

#the Bullet class that is created by the player upon mouse click in game
class Bullet:
    def __init__(self,playerpos,mousepos):
        #the starting position will be near the center of the player position when the bullet was shot
        self.x = playerpos[0]+13
        self.y = playerpos[1]+13

        #direction the bullet will travel in
        self.direction = self.direction(mousepos)

        #there will be a delay before you are able to shoot again, and is counted using the timeBetweenBullet variable in this class
        self.timeBetweenBullet = 0
        self.bulletimg = c.bullet

    #function calculates the direction the bullet will travel in according to mouse position
    def direction(self,mousepos):
        direction = 0

        #calculates the difference in x and difference in y between the player
        dx = mousepos[0] - self.x
        dy = mousepos[1] - self.y

        #calculates the angle, where dx is the adjacent and dy is the opposite
        rad = atan2(-dy,dx)

        #if the angle is between -pi/4 and pi/4 radians, or between 7pi/4 and pi/4 radians, this means the mouse is to the right of the player, therefore the direction of the bullet is right
        #this calculation is used for other directions
        if rad >= -0.785 and rad < 0.785:
            direction = "right"
        elif rad >= 0.785 and rad < 2.355:
            direction = "up"
        elif rad >= -2.355 and rad < -0.785:
            direction = "down"
        elif rad >= 2.355 or rad > -3.142:
            direction = "left"

        return direction

    #updates the position
    def movement(self):
        #updates the position according to the direction the bullet is travelling in
        if self.direction == "right":
            self.x += 16

        elif self.direction == "down":
            self.y += 16

        elif self.direction == "up":
            self.y -= 16

        elif self.direction == "left":
            self.x -= 16

        self.timeBetweenBullet += 1

    #checks the collision
    def collide(self, curRoom):
        collided = False
        obstacleList = curRoom.obstacleList

        #checks if the bullet collides with any obstacles
        for i in obstacleList:
            if collision.spritesCollision(i,(self.x,self.y),5,5):
                collided = True

        return collided