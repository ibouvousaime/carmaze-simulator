def solveMaze(cells, startCellIndex, destination = -1):
    tree = {}
    if destination == -1:
        destination = getCellIndex(cells[-1])
    if startCellIndex == destination : 
        return {"destination": True}
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
        return {"destination": False}

    for neighbor in accessibleNeighbors:
        tree[neighbor] = solveMaze(cells, neighbor)

    return cells