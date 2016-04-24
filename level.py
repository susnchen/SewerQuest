import constants as c
import room

class Level:
    def __init__(self, levelNum):
        self.levelNum = levelNum
        self.fishesLeft = c.levelSettings[levelNum]
        self.curRoomNum = 0
        self.curRoom = room.Room(self.curRoomNum)

    def updateRoom(self,roomNum):
        self.curRoomNum = roomNum
        self.curRoom = room.Room(self.curRoomNum)

    def updateFish(self):
        self.fishesLeft -= 1
