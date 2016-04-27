import constants as c
import room

class Level:
    def __init__(self, levelNum):
        self.levelNum = levelNum
        self.fishesLeft = c.levelSettings[levelNum]
        self.fishPlacements = [(240,320), (240,320), (500,96),(96,280),(32,32)]
        self.roomList = []
        for i in range (0,len(room.roomDoorList)):
            self.roomList += [room.Room(i,self.fishPlacements)]
        self.curRoomNum = 0
        self.curRoom = self.roomList[0]
