import constants as c
import room
import enemy
import random

class Level:
    def __init__(self, levelNum):
        self.levelNum = levelNum

        self.fishPlacements = c.fishPlacements[levelNum]
        self.fishNums = len(self.fishPlacements) - self.fishPlacements.count(False)
        self.fishLeft = self.fishNums

        self.roomList = []
        self.roomList += [room.Room(0,self.fishPlacements[0], [], c.roomImgs[levelNum][0])]

        self.roomEnemyDict = {
            0: []
        }

        for i in range(1, len(c.roomDoorDict[levelNum])-1):
            enemyList = []
            for j in range(0, random.randint(1, 3)):
                randx = random.randint(1, 18)
                randy = random.randint(1, 14)
                enemyList += [enemy.Enemy(1, c.enemySpeedSetting[levelNum], 32 * randx, 32 * randy)]

            self.roomEnemyDict[i] = enemyList

        for i in range (1,len(c.roomDoorDict[levelNum])-1):
            self.roomList += [room.Room(i,self.fishPlacements[i], self.roomEnemyDict.get(i),c.roomImgs[levelNum][i])]

        self.curRoomNum = 0
        self.curRoom = self.roomList[0]
