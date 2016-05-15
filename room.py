# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# room.py
# contains the room class that contains the obstacles and water coordinates, if it was visited or not, room number, fish and enemy placements, and the image

# input: arguments for parameters defined by functions, this includes int, list, and pygame surfaces
# output: transition function returns the doorNum and nextRoom Num as an int

import constants as c

class Room:
    def __init__(self,roomNum,fishPlacement,enemyList,roomImg):
        #obstacleList will contain coordinates of all walls in the room
        #players, enemies and bullets cannot cross items in this list
        self.obstacleList = []

        #waterList will contain coordinates of all water in the room
        #the player will not be able to cross items in this list
        self.waterList = []

        self.roomNum = roomNum
        self.roomImg = roomImg

        #visited variable will be used to display the minimap
        self.visited = False
        self.minimapPos = (0,0)

        #checks rbg values of each block (32 by 32 blocks) to see if they are obstacles or water
        #walls have rgb values of (88,84,75) and (74,86,89) and water has values of (97,115,113)
        #since our room image is placed at (-32,-32), we start checking at (-32,-32)
        #room image will be placed at (-32,-32) because there are walls with y and x coordinates equating to -32
        #that will block bullets from leaving the screen without being destroyed
        for y in range(-32, 544, 32):
            for x in range(-32, 672, 32):
                #if it is a obstacle
                if self.roomImg.get_at((x + 32, y + 32)) == (88, 84, 75, 255) or self.roomImg.get_at((x + 32, y + 32)) == (74,86,89, 255):
                    #add to the obstacleList
                    self.obstacleList += [(x, y)]

                #same with the water
                elif self.roomImg.get_at((x + 32, y + 32)) == (97,115,113, 255):
                    self.waterList += [(x,y)]

        self.enemyList = enemyList
        self.fishPlacement = fishPlacement

#checks which room to go out
def transition(inCDoorNum,inCRoomNum,levelNum):
    #the next room will be what the door of the current room leads to
    #this is stored inside the roomDoorDict variable
    nextRoomNum = c.roomDoorDict[levelNum][inCRoomNum][inCDoorNum]

    #the top door is door 0, right door is door 1, bottom door is door 2, left door is door 3
    #top doors would lead to bottom doors and vice versa
    #left doors would lead to right doors and vice versa
    if inCDoorNum == 3 or inCDoorNum == 2:
        outGDoorNum = inCDoorNum - 2

    else:
        outGDoorNum = inCDoorNum + 2

    #returns the door that the player will be coming out from and to which room
    return nextRoomNum, outGDoorNum
