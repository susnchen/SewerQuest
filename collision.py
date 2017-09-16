
# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# collision.py
# a library of collision functions that checks if 2 items collide, the direction of the collision, and check collision of items in a list

# input: position, width, and height of objects in tuples and ints
# output: direction of collision as strings, list of these collision in a list, and if it collides as a bool

import pygame
import constants as c

#checks if a position collides with items of a list
def checkCollision(pos,obstacleList):
        col = []
        for i in obstacleList:
            col += spriteCollision(pos,i)[0]

        return col

#checks if the player collides with any of the door positions
def checkTransition(pos):
    doorNum = -1

    for i in c.doorPos:
        playerRect = pygame.Rect(pos,(32,32))

        #if player collides with any of the door position
        if playerRect.collidepoint(i):
            #calculates the door number the player collided with
            #since there are 2 position for each door, the door number is its index divided by 2
            doorNum = int((c.doorPos.index(i)/2))

    # returns -1 if player does not collide with a door, else return the door the player collided with
    return doorNum

#returns a list of directions a sprite collides with
def spriteCollision(pos,objpos,objW = 32, objH = 32):
    collision = []
    collided = False

    #if sprite position is to the right or left of the object and y coordinate of player is within 32 pixels of the y coordinate of the object

    #for example, for there to be collision left, the x coordinate of the top left point of the sprite is the same as the top right point of the object and the y coordinate of the sprite is within the top and bottom of the object
    if pos[0] == objpos[0] + objW and not(pos[1] >= objpos[1] + objH-3 or pos[1] + 29 <= objpos[1]):
        collision += ["left"]
        collided = True

    if pos[0] + 32 == objpos[0] and not(pos[1] > objpos[1] + objH-3 or pos[1] + 29 < objpos[1]):
        collision += ["right"]
        collided = True

    if pos[1] == objpos[1] + objH and not(pos[0] > objpos[0] + objW-3 or pos[0] + 29 < objpos[0]):
        collision += ["up"]
        collided = True

    if pos[1] + 32 == objpos[1] and not(pos[0] > objpos[0] + objW-3 or pos[0] + 29 < objpos[0]):
        collision += ["down"]
        collided = True

    #if player is at the tip of a block (it handles diagonal walking so you don't walk diagonally through a wall)
    if pos[0] == objpos[0] + objW and pos[1] == objpos[1] + objH:
        collision += ["upleft"]

    if pos[0] == objpos[0] + objW and pos[1] + 32 == objpos[1]:
        collision += ["downleft"]

    if pos[0] + 32 == objpos[0] and pos[1] + 32 == objpos[1]:
        collision += ["downright"]

    if pos[0] + 32 == objpos[0] and pos[1] == objpos[1] + objH:
        collision += ["upright"]

    return collision,collided

#checks if two sprites overlap and default width and height equaling 32
def spritesCollision(pos,objpos,objw = 32, objh = 32):
    #creates two rects where the two sprites are
    mask1 = pygame.Rect((pos),(32,32))
    mask2 = pygame.Rect((objpos),(objw,objh))

    #checks and returns if they overlap
    collided = bool(mask1.colliderect(mask2))

    return collided