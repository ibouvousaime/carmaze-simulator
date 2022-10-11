
import random
import math
import asyncio
import json

top, right, bottom, left = [0,1,2,3]
visited = 3
offset = 100
def generateGrid(size) :
    cells = []
    index = 0
    for y in range(size):
        for x in range(size):
            cells.append([[True, True, True, True], (x, y), index, False])
            index += 1
    return cells



def doesCellHasWallOn(cell, direction) : 
    return cell[0][direction]

def getCellCoords(cell, scale, size) : 
    coordList = list(cell[1])
    coordList[0] = coordList[0] * scale + (scale*size/4)
    coordList[1] = (scale * size) - (coordList[1] * scale) + (scale*size/4)
    return tuple(coordList)

def getCellIndex(cell):
    return cell[2]

def getCellNeighbourIndices(cell, size) :
    neighbors = [getCellIndex(cell) - size, getCellIndex(cell) + size]
    if not isCellAtTheEdge(cell, size, left):
        neighbors.append(getCellIndex(cell) - 1)
    if not isCellAtTheEdge(cell, size, right):
        neighbors.append(getCellIndex(cell) + 1)
    return [x for x in neighbors if x >= 0 and x < size * size]

def isCellAtTheEdge(cell, size, direction) : 
    result = None
    if direction == top: result =  getCellIndex(cell) < size and getCellIndex(cell) >= 0 
    elif direction == bottom : result = (getCellIndex(cell) + size) >= (size * size)
    elif direction == left : result = getCellIndex(cell)  % size == 0
    elif direction == right : result = (getCellIndex(cell) + 1) % size == 0
    return result

def getNeighborIndex(cell, size, direction) :
    result = -1
    if direction == top: result =  getCellIndex(cell) - size
    elif direction == bottom : result = getCellIndex(cell) + size
    elif direction == left : result = getCellIndex(cell) - 1
    elif direction == right : result = getCellIndex(cell) + 1
    return int(result) if result > 0 and result < size * size else -1


def getDirectionBetweenCells(cellIndex1, cellIndex2, size) :
    if cellIndex1 + 1 == cellIndex2 : return right
    elif cellIndex1 - 1 == cellIndex2: return left
    elif cellIndex1 + size == cellIndex2 : return bottom
    elif cellIndex1 - size == cellIndex2 : return top
    else: assert(False); return -1

def getOppositeDirection(direction):
    if direction is top: return bottom
    if direction is left: return right
    if direction is bottom: return top
    if direction is right: return left
    else: assert(False); return -1

def openWallBetweenCells(cells, firstCell, secondCell, direction):
    cells[firstCell][0][direction] = False
    cells[secondCell][0][getOppositeDirection(direction)] = False
    return cells

def removeCellVisitedStatus(cell):
    cell[3] = False
    return cell

def generateMaze(cells, chosenCellIndex = 0, stack = []) :
    cells[chosenCellIndex][visited] = True;
    currentCell = cells[chosenCellIndex]
    neighbors = getCellNeighbourIndices(currentCell, math.sqrt(len(cells)))
    random.shuffle(neighbors)
    neighbors = [int(x) for x in neighbors]
    chosenNeighbor = None
    for neighbor in neighbors :
        if not cells[int(neighbor)][visited]:
            chosenNeighbor = neighbor
            stack.append(chosenNeighbor)
            direction = getDirectionBetweenCells(chosenCellIndex, chosenNeighbor, math.sqrt(len(cells)))
            cells = openWallBetweenCells(cells, chosenCellIndex, chosenNeighbor, direction)
            break
    if chosenNeighbor == None:
        stack.pop()
        if len(stack) != 0: 
            chosenNeighbor = stack[-1]
        else:
            cells = tuple(map(removeCellVisitedStatus, cells))
            return cells
    return generateMaze(cells, chosenNeighbor, stack)


def getPathToDestination(tree, currentList = []):
    global glist
    if isinstance(tree, dict):
        for key in tree:
            if key == "destination" and tree[key]:
                glist.append(currentList)
            elif key == "destination" and not tree[key]:
                return
            else:
                currentList.append(key)
                getPathToDestination(tree[key], currentList)
        return 



mazesolution = []
def solveMaze(cells, startCellIndex, stack = None, destination = -1 ):
    global mazesolution
    if stack is None:
        stack = []
    solution = None
    stack.append(startCellIndex)
    if destination == -1:
        destination = getCellIndex(cells[-1])
    if startCellIndex == destination : 
        mazesolution = stack.copy()
    size = math.sqrt(len(cells))
    cells[startCellIndex][visited] = True
    currentCell = cells[startCellIndex]
    cellWalls = currentCell[0]
    accessibleNeighbors = []
    topNeighbor = getNeighborIndex(currentCell, size, top)
    bottomNeighbor = getNeighborIndex(currentCell, size, bottom)
    leftNeighbor = getNeighborIndex(currentCell, size, left)
    rightNeighbor = getNeighborIndex(currentCell, size, right)

    if topNeighbor != -1 and not cellWalls[top] and (not cells[topNeighbor][visited]) : accessibleNeighbors.append(topNeighbor) 
    if bottomNeighbor != -1 and not cellWalls[bottom] and (not cells[bottomNeighbor][visited]): accessibleNeighbors.append(bottomNeighbor)
    if leftNeighbor != -1 and not cellWalls[left] and (not cells[leftNeighbor][visited]): accessibleNeighbors.append(leftNeighbor)
    if rightNeighbor != -1 and not cellWalls[right] and (not cells[rightNeighbor][visited]): accessibleNeighbors.append(rightNeighbor)
    if len(accessibleNeighbors) == 0:
        return [stack]
    else:
        for neighbor in accessibleNeighbors:
            solveMaze(cells, neighbor, stack.copy())
    return

cells = generateMaze(generateGrid(12))
solveMaze(cells, 0, [].copy(), len(cells) - 1)
print(mazesolution)