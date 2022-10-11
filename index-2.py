import generator as gen
from ursina import *

scale = 50
lineWidth = 1
size = 12
cells = gen.generateMaze(gen.generateGrid(size))
startPosition = 0
gen.solveMaze(cells, startPosition)
solution = gen.mazesolution

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)

EditorCamera()
app.run()
