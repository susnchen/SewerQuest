import pygame
import constants as c

def checkCollision(pos,obstacleList):
        col = []
        for i in obstacleList:
            col += playerCollision(pos,i)[0]

        return col

def checkTransition(pos):
    roomNum = 4

    for i in c.doorPos:
        if objectCollider(pos, i):
            roomNum = int(str(c.doorPos.index(i)/2)[0])

    return roomNum

def playerCollision(pos,objpos,objW = 32,objH = 32):
        collision = []
        collided = False

        #if player position is to the right or left of the object and y coordinate of player is within 32 pixels of the y coordinate of the object
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

        return collision,collided

def objectCollider(pos,objpos,objw = 32, objh = 32):
        object1 = pygame.Rect((pos),(32,32))
        object2 = pygame.Rect((objpos),(objw,objh))

        collided = bool(object1.colliderect(object2))

        return collided

def bulletCollider(bulletpos, objpos):
    objectRect = pygame.Rect(objpos,(32,32))
    bulletRect = pygame.Rect(bulletpos,(5,5))

    collided = objectRect.contains(bulletRect)

    return bool(collided)

