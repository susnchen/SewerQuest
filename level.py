# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# level.py
# contains the Level class that contains list of all the rooms and creates each room

# input: level number as int and various level settings from the constants files such as lists, pygame surfaces, and dictionaries
# output: list of rooms, enemies, and fish placements

import constants as c
import room
import enemy
import random

class Level:
    def __init__(self, levelNum):
        self.levelNum = levelNum

        #gets the fishe placements of each room in the level, the amount of fishes in the level, and a fishLeft variable that shows how many fishes have not been collected
        self.fishPlacements = c.fishPlacements[levelNum]
        self.fishNums = len(self.fishPlacements) - self.fishPlacements.count(False)
        self.fishLeft = self.fishNums

        #initializes the roomList and creates the first room
        self.roomList = []
        self.roomList += [room.Room(0,self.fishPlacements[0], [], c.roomImgs[levelNum][0])]

        self.roomEnemyDict = {
            0: []
        }

        #creates all the enemies in each room
        for i in range(1, len(c.roomDoorDict[levelNum])-1):
            enemyList = []
            for j in range(0, random.randint(1, 3)):
                randx = random.randint(1, 18)
                randy = random.randint(1, 14)
                enemyList += [enemy.Enemy(1, c.enemySpeedSetting[levelNum], 32 * randx, 32 * randy)]

            self.roomEnemyDict[i] = enemyList

        #creates all the rooms in the level
        for i in range (1,len(c.roomDoorDict[levelNum])-1):
            self.roomList += [room.Room(i,self.fishPlacements[i], self.roomEnemyDict.get(i),c.roomImgs[levelNum][i])]
    '''
        self.roomList[0].minimapPos = (2,0)
        for i in range(0,len(self.roomList)):
            curMinimapPos = self.roomList[i].minimapPos
            doorList = c.roomDoorDict[levelNum][i]

            for doorNum in range(0,len(doorList)):
                adjRoomNum = doorList[doorNum]

                if adjRoomNum != -1:
                    if doorNum == 0:
                        self.roomList[adjRoomNum].minimapPos = (curMinimapPos[0],curMinimapPos[1] - 1)
                    elif doorNum == 1:
                        self.roomList[adjRoomNum].minimapPos = (curMinimapPos[0] + 1,curMinimapPos[1])
                    elif doorNum == 2:
                        self.roomList[adjRoomNum].minimapPos = (curMinimapPos[0],curMinimapPos[1] + 1)
                    elif doorNum == 3:
                        self.roomList[adjRoomNum].minimapPos = (curMinimapPos[0] - 1,curMinimapPos[1])

                print((curMinimapPos[0] - 1,curMinimapPos[1]))
                print(doorList[doorNum])
    '''



        #for i in range(1,len(self.roomList)):
        #   self.roomList[i].minimapPos = (0,0)