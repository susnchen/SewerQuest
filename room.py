import constants as c
import enemy

roomDoorList = [
    # index of this list is the room number
    # where the 0th index of each item correspond to door 0 (top door)
    # where the 1st index of each item correspond to door 1 (right door)
    # where the 2nd index of each item correspond to door 2 (bottom door)
    # where the 4rd index of each item correspond to door 3 (left door)
    # the number in each index of the item represents the room the door leads to
    # for example, room 0's door 1 leads to room 1
    # room -1 does not exist so it leads to no where
    (-1,1,-1,-1),
    (2,3,-1,0),
    (-1,-1,1,-1),
    (-1,-1,-1,1)
]

#placements of fishes

class Room:
    def __init__(self,roomNum,fishPlacements,enemyList):
        self.obstacleList = []
        self.roomNum = roomNum
        self.roomImg = c.roomImg[roomNum]
        self.fishPlacements = fishPlacements

        for y in range(-32, 544, 32):
            for x in range(-32, 672, 32):
                if c.roomImg[roomNum].get_at((x + 32, y + 32)) == (129, 149, 173, 255):
                    self.obstacleList += [(x, y)]

        #print(enemyList)
        self.enemyList = enemyList
        self.fishPlacement = self.getFish()

    def getFish(self):

        fishPlacement = False
        if self.fishPlacements[self.roomNum] != False:
            fishPlacement = self.fishPlacements[self.roomNum]
        return fishPlacement

    def getObstacleList(self):
        return self.obstacleList

def transition(inCDoorNum,inCRoomNum):
    nextRoomNum = roomDoorList[inCRoomNum][inCDoorNum]

    print("the door " + str(inCDoorNum) + " from room " + str(inCRoomNum) + " is " + str(nextRoomNum))

    if inCDoorNum == 3 or inCDoorNum == 2:
        outGDoorNum = inCDoorNum - 2

    else:
        outGDoorNum = inCDoorNum + 2

    return nextRoomNum, outGDoorNum
