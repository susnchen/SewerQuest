from math import fabs,sqrt
import pygame
import time

import constants as c
import collision

screen = pygame.display.set_mode((c.gamew, c.gameh))

pygame.font.init()
font = pygame.font.SysFont("monospace",32)
letter = font.render("A",1,(255,255,255))

class Node:
    def __init__(self,cost,start,goal,parent = 0):
        self.cost = cost
        self.openList = []
        self.closeList = []
        self.start = start
        self.goal = goal
        if parent:
            self.parent = parent

def sortList(obj):
    return obj.cost

def adjacentPos(i,objpos):
    if i == 0:
        checkNode = (objpos[0],objpos[1]-1)
    elif i == 1:
        checkNode = (objpos[0]+1, objpos[1])
    elif i == 2:
        checkNode = (objpos[0], objpos[1]+1)
    elif i == 3:
        checkNode = (objpos[0-1], objpos[1])
    return checkNode

def checkCloseList(closeList,Node):
    notInList = True
    for i in closeList:
        if Node.start == i.start: notInList = False

    return notInList


def pathfind(curRoom,start,goal):
    curNode = Node(0,start,goal)
    openList = [curNode]
    closeList = []
    loop = 0
    notFound = True

    while notFound:
        curNode = Node(0,(start),goal)
        openList += [curNode]
        openList.sort(key=sortList)
        closeList += [curNode]
        openList.remove(curNode)
        curCost = 0

        for i in range(4):
            nextNodepos = adjacentPos(i,curNode.start)
            nextNode = Node(curNode.cost + 1,nextNodepos,goal,curNode)

            if (nextNodepos) not in curRoom.obstacleList and checkCloseList(closeList,nextNode):
                #print(nextNodepos)

                screen.blit(letter,(nextNodepos[0]*32,nextNodepos[1]*32))
                pygame.display.update()
                if nextNodepos == goal:
                    notFound = False
                    break

                openList += [nextNode]
                openList.sort(key=sortList)
                curNode = openList[0]
                curCost = curNode.cost

            else:
                closeList += [nextNode]

            loop += 1
    time.sleep(30)





'''
class status:
    def __init__(self,value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal

        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def getDist(self):
        pass

    def children(self):
        pass

class stateStr:
    def __init__(self,value, parent, start = 0, goal = 0):
        super(stateStr, self).__init__(value, parent, start, goal)
        self.dist = self.getDist()

    def getDist(self):
        dist = 0
        if self.value == self.goal:
            return 0

        for i in range (len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))

        return dist

    def children(self):
        if not self.children():
            for i in range((len.goal)-1):
                val = self.value
                val = val[:1] + val[i+1] + val[i] +val[i+2:]
                child = stateStr (val,self)
                self.children().append(child)

class solver:
    def __init__(self,start,goal):
        self.path = []
        self.visitedQ = []
        self.priorityQ = PriorityQueue()
        self.start = start
        self.goal = goal

    def solver(self):
        startState = stateStr(self.start,0,self.start,self.goal)
        count = 0
        self.priorityQ.put((0,count,startState))
        while(not self.path and self.priorityQ.qsize()):
            closestChild = self.priorityQ.qsize()[2]
            closestChild.children()
            self.visitedQ.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQ:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQ.put((child.dist,count,child))
        print(self.path)
        return self.path

    def __init__(self, tile, parent, gCost, hCost):
        self.tile = tile
        self.parent = parent
        self.gCost = gCost
        self.hCost = hCost
        self.fCost = gCost + hCost

def pathfinder(playerpos,enemypos,obstaclelist):
    x = fabs(enemypos[0]-playerpos[0])
    y = fabs(enemypos[1]-playerpos[1])
    heuristic = x+y
    moveCost = sqrt(x**2+y**2)
    print(heuristic,moveCost)
'''