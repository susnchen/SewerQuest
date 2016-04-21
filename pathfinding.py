import constants
import collision

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


def pathfind(curRoom,start,goal):
    curNode = Node(0,start,goal)
    openList = [curNode]
    closeList = []
    notFound = True

    while notFound:
        openList.sort(key=sortList)
        curNode = openList[0]
        curCost = 0
        closeList += [curNode]
        checkNode = ()

        for i in range(4):
            nextNodepos = adjacentPos(i,curNode.start)
            nextNode = Node(curNode.cost + 1,nextNodepos,goal,curNode)

            if not bool(curRoom.grid[nextNodepos[1]][nextNodepos[0]]) and nextNode not in closeList:
                openList += [nextNode]
                openList.sort(key=sortList)
                curNode = openList[0]
                curCost = curNode.cost

            else:
                closeList += [nextNode]

        if openList == []:
            break