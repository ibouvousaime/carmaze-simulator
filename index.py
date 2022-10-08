from turtle import color
import pyglet

import generator as gen
scale = 50
lineWidth = 1
window = pyglet.window.Window(1600, 900)
size = 12
cells = gen.generateMaze(gen.generateGrid(size))
gen.solveMaze(cells,0)
solution = gen.mazesolution
@window.event
def on_draw():
    window.clear()
    for cell in cells:
        text = pyglet.text.Label(str(gen.getCellIndex(cell)),
                          font_name='Times New Roman',
                          font_size=10,
                          color=(255 if gen.getCellIndex(cell) in solution else 50, 50, 30, 255), 
                          x=gen.getCellCoords(cell, scale, size)[0], y=gen.getCellCoords(cell, scale, size)[1],
                          anchor_x='center', anchor_y='center')
        text.draw()
        if (gen.doesCellHasWallOn(cell, gen.left)) :
            leftLine = pyglet.shapes.Line(gen.getCellCoords(cell, scale, size)[0] - scale / 2 , gen.getCellCoords(cell, scale, size)[1] - scale / 2, gen.getCellCoords(cell, scale, size)[0] - scale / 2, gen.getCellCoords(cell, scale, size)[1] + scale / 2, lineWidth, color = (255, 255, 255))
            leftLine.draw()
        if (gen.doesCellHasWallOn(cell, gen.top)) :  
            topLine = pyglet.shapes.Line(gen.getCellCoords(cell, scale, size)[0] - scale / 2, gen.getCellCoords(cell, scale, size)[1] + scale / 2, gen.getCellCoords(cell, scale, size)[0] + scale / 2, gen.getCellCoords(cell, scale, size)[1] + scale / 2, lineWidth, color = (255, 225, 255))
            topLine.draw()
        if (gen.doesCellHasWallOn(cell, gen.bottom) and gen.isCellAtTheEdge(cell, size, gen.bottom)) :  
            bottomline = pyglet.shapes.Line(gen.getCellCoords(cell, scale, size)[0] - scale / 2, gen.getCellCoords(cell, scale, size)[1] - scale / 2, gen.getCellCoords(cell, scale, size)[0] + scale / 2, gen.getCellCoords(cell, scale, size)[1] - scale / 2, lineWidth, color = (255, 255, 255))
            bottomline.draw()
        if (gen.doesCellHasWallOn(cell, gen.right) and gen.isCellAtTheEdge(cell, size, gen.right)) :  
            rightline = pyglet.shapes.Line(gen.getCellCoords(cell, scale, size)[0] + scale / 2, gen.getCellCoords(cell, scale, size)[1] - scale / 2, gen.getCellCoords(cell, scale, size)[0] + scale / 2, gen.getCellCoords(cell, scale, size)[1] + scale / 2, lineWidth, color = (255, 225, 255))
            rightline.draw()
        for index, solutionElement in enumerate(solution):
            if index != len(solution) - 1 :
                currentLine = pyglet.shapes.Line(gen.getCellCoords(cells[solutionElement], scale, size)[0], gen.getCellCoords(cells[solutionElement], scale, size)[1], gen.getCellCoords(cells[solution[index + 1]], scale, size)[0], gen.getCellCoords(cells[solution[index + 1]], scale, size)[1], lineWidth, color = (255, 100, 100))
                currentLine.draw()


pyglet.app.run()

