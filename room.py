import constants as c

class Room:
    def __init__(self,roomNum,fishPlacement,enemyList,roomImg):
        self.obstacleList = []
        self.waterList = []
        self.roomNum = roomNum
        self.roomImg = roomImg

        for y in range(-32, 544, 32):
            for x in range(-32, 672, 32):
                if self.roomImg.get_at((x + 32, y + 32)) == (88, 84, 75, 255) or self.roomImg.get_at((x + 32, y + 32)) == (74,86,89, 255):
                    self.obstacleList += [(x, y)]
                elif self.roomImg.get_at((x + 32, y + 32)) == (97,115,113, 255):
                    self.waterList += [(x,y)]

        #checks rbg values of each block (32 by 32 blocks) to see if they are walls
        #walls have rgb values of (88,84,75) and (74,86,89) and water has values of (97,115,113)

        self.enemyList = enemyList
        self.fishPlacement = fishPlacement

    def getObstacleList(self):
        return self.obstacleList

def transition(inCDoorNum,inCRoomNum,levelNum):
    nextRoomNum = c.roomDoorDict[levelNum][inCRoomNum][inCDoorNum]
    if inCDoorNum == 3 or inCDoorNum == 2:
        outGDoorNum = inCDoorNum - 2

    else:
        outGDoorNum = inCDoorNum + 2

    return nextRoomNum, outGDoorNum
