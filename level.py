import constants as c
import room
import enemy
import random

class Level:
    def __init__(self, levelNum):
        self.levelNum = levelNum

        self.fishesLeft = c.levelSettings[levelNum]
        self.fishPlacements = [(240,320), (240,320), (500,96),(96,280),(32,32)]

        self.roomList = []
        self.roomList += [room.Room(0,self.fishPlacements, [])]

        self.roomEnemyDict = {
            0: []
        }

        for i in range(1, len(room.roomDoorList)):
            enemyList = []
            for j in range(0, random.randint(1, 3)):
                randx = random.randint(1, 18)
                randy = random.randint(1, 14)
                enemyList += [enemy.Enemy(1, 1, 32 * randx, 32 * randy)]

            self.roomEnemyDict[i] = enemyList

        for i in range (1,len(room.roomDoorList)):
            print(self.roomEnemyDict.get(i))
            self.roomList += [room.Room(i,self.fishPlacements, self.roomEnemyDict.get(i))]

        self.curRoomNum = 0
        self.curRoom = self.roomList[0]
