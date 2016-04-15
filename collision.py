import pygame

class Collision:
    def __init__(self,position):
        self.x = position[0]
        self.y = position[1]
        self.pos = position

    def checkCollision(self,objs):
        col = []
        for i in objs:
            col += self.objcollision(self.pos,(i[1],i[2]),i[0][0],i[0][1])[0]
        return col

    def objcollision(self,pos,objpos,objW,objH):
        collision = []
        collided = False
        #if player position is to the right or left of the object and y coordinate of player is within 32 pixels of the y coordinate of the object
        if pos[0] == objpos[0] + objW and not(pos[1] >= objpos[1] + objH-1 or pos[1] + 31 <= objpos[1]):
            collision += ["left"]
            collided = True
        if pos[0] + 32 == objpos[0] and not(pos[1] > objpos[1] + objH-1 or pos[1] + 31 < objpos[1]):
            collision += ["right"]
            collided = True
        if pos[1] == objpos[1] + objH and not(pos[0] > objpos[0] + objW-1 or pos[0] + 31 < objpos[0]):
            collision += ["up"]
            collided = True
        if pos[1] + 32 == objpos[1] and not(pos[0] > objpos[0] + objW-1 or pos[0] + 31 < objpos[0]):
            collision += ["down"]
            collided = True
        return collision,collided

    def enemyCollider(self,pos,objpos):
        collided = False
        enemy = pygame.Rect((pos),(32,32))
        object = pygame.Rect((objpos),(32,32))

        if enemy.colliderect(object) == True:
            collided = True

        return collided
