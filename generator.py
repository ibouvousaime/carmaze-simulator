import random
import math
import asyncio

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
    return result if result > 0 and result < size * size else -1


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
    if (firstCell % 10 == 0) :
        print(cells, firstCell, secondCell, direction)
    return cells

def generateMaze(cells, chosenCellIndex = -1, stack = []) :
    if chosenCellIndex == -1:
        chosenCellIndex = random.randint(0, len(cells) - 1)
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
            return cells
    return generateMaze(cells, chosenNeighbor, stack)

