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

        #spawns all the enemies in each room
        for i in range(1, len(c.roomDoorDict[levelNum])):
            enemyList = []
            for j in range(0, random.randint(3, 7)):
                randx = random.randint(3, 16)
                randy = random.randint(3, 11)
                enemyList += [enemy.Enemy(1, c.enemySpeedSetting[levelNum], 32 * randx, 32 * randy)]

            self.roomEnemyDict[i] = enemyList

        #creates all the rooms in the level
        for i in range (1,len(c.roomDoorDict[levelNum])):
            self.roomList += [room.Room(i,self.fishPlacements[i], self.roomEnemyDict.get(i),c.roomImgs[levelNum][i])]