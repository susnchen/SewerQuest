import collision
import constants as c
import enemy
import pathfinder
from math import sqrt

roomDoorList = [
    # "room" + room index : ((this room's door, the room index the door leads to))
    # for example:
    # room0 has door1 and 3 open and door1 links to room2 and door3 links to room3
    (-1,1,-1,-1),
    (2,3,-1,0),
    (-1,-1,1,-1),
    (-1,-1,-1,1)
]

roomEnemyDict = {
    0: [],
    1: [enemy.Enemy(1,1,c.u*8,c.u*7)],#,enemy.Enemy(1,1,c.u*16,c.u*3),enemy.Enemy(1,1,c.u*10,c.u*13)],
    2: [enemy.Enemy(1,1,c.u*8,c.u*7),enemy.Enemy(1,1,c.u*16,c.u*3)],
    3: [enemy.Enemy(1,1,c.u*16,c.u*3),enemy.Enemy(1,1,c.u*16,c.u*3),enemy.Enemy(1,1,c.u*16,c.u*3),enemy.Enemy(1,1,c.u*16,c.u*3)],
}

class Room:
    def __init__(self,roomNum):
        self.obstacleList = []
        self.roomNum = roomNum
        self.roomImg = c.roomImg[roomNum]

        for y in range(-32, 544, 32):
            for x in range(-32, 672, 32):
                if c.roomImg[roomNum].get_at((x + 32, y + 32)) == (129, 149, 173, 255):
                    self.obstacleList += [(x, y)]

        self.enemyList = roomEnemyDict.get(roomNum)

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

roomList = []
for i in range(0, len(roomDoorList)):
    roomList += [Room(i)]
