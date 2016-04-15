import collision, constants as c

class Room:
    def __init__(self):
        self.roompos = (32,-32)

    def transition(self,playerpos):
        col = collision.Collision(playerpos)
        if col.objcollision(playerpos,self.roompos,32,32)[1] == True:
            print("do something!")