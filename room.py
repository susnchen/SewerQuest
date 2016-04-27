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

#a list of all the enemies in each room
roomEnemyDict = {
    0: [],
    1: [enemy.Enemy(1,1,c.u*8,c.u*7),enemy.Enemy(1,1,c.u*16,c.u*3),enemy.Enemy(1,1,c.u*10,c.u*13)],
    2: [enemy.Enemy(1,1,c.u*8,c.u*7),enemy.Enemy(1,1,c.u*16,c.u*3)],
    3: [enemy.Enemy(1,1,c.u*16,c.u*3),enemy.Enemy(1,1,c.u*14,c.u*6)],
}

#placements of fishes

class Room:
    def __init__(self,roomNum,fishPlacements):
        self.obstacleList = []
        self.roomNum = roomNum
        self.roomImg = c.roomImg[roomNum]
        self.fishPlacements = fishPlacements

        for y in range(-32, 544, 32):
            for x in range(-32, 672, 32):
                if c.roomImg[roomNum].get_at((x + 32, y + 32)) == (129, 149, 173, 255):
                    self.obstacleList += [(x, y)]

        self.enemyList = roomEnemyDict.get(roomNum)
        self.fishPlacement = self.getFish()

    def getFish(self):

        fishPlacement = False
        if self.fishPlacements[self.roomNum] != False:
            fishPlacement = self.fishPlacements[self.roomNum]
        return fishPlacement

    def getObstacleList(self):
        return self.obstacleList

def transition(inCDoorNum,inCRoomNum):
    nextRoom = roomDoorList[inCRoomNum][inCDoorNum]

    if inCDoorNum == 3 or inCDoorNum == 2:
        outGDoorNum = inCDoorNum - 2

    else:
        outGDoorNum = inCDoorNum + 2

    if inCDoorNum == 1:
        print(outGDoorNum)

    return nextRoom, outGDoorNum
