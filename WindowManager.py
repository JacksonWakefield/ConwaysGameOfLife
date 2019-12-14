"""Graphics controller"""
from graphics import *
import math

class GridWindow:
    
    #width and height of the window in pixels
    width = 0
    height = 0
    
    #size of each individual cell (squares)
    cell_size = 0
    
    #how many cells across
    cell_num = 0
    
    
    def __init__(self, _cell_size, _cell_num):
        #weird way to make something accessable to a different class, but it works 
        #just fine in python so
        import graphics
        self.graphics = graphics
        
        self.cell_size = _cell_size
        self.cell_num = _cell_num
        
        self.width = _cell_size * _cell_num
        self.height = _cell_size * _cell_num
        
        self.window = GraphWin("Conway's Game Of Life", self.width, self.height)
                
        self.initGrid()
        
        #self.window.getMouse()
        #self.window.close()
        
    
    #instantiates a grid based on width and height
    def initGrid(self):
        for i in range(self.cell_num):
            pt1 = Point(0, i * self.cell_size)
            pt2 = Point(self.width, i * self.cell_size)
            
            pt3 = Point(i * self.cell_size, 0)
            pt4 = Point(i * self.cell_size, self.height)
            
            line = Line(pt1, pt2)
            line2 = Line(pt3, pt4)
            
            line.draw(self.window)
            line2.draw(self.window)
    
    
            
    #takes in multidimensional array with 0s and 1s
    def updateGrid(self, oldTiles, newTiles):
        for x in range(self.cell_num):
            for y in range(self.cell_num):
                oldTile = oldTiles[x, y]
                newTile = newTiles[x, y]
                
                if(oldTile != newTile):
                    self.fillCell((x, y), True if newTile == 1 else False)
    
    def updateGridPoint(self, position, on):
        self.fillCell((position[0], position[1]), True if on == 1 else False)
    
    #takes in tuple position and boolean for fill or unfill
    def fillCell(self, position, fill):
        pt1 = Point((position[0] - 1) * (self.cell_size), (position[1] - 1) * (self.cell_size))
        pt2 = Point(position[0] * (self.cell_size), position[1] * (self.cell_size))
        
        
        rectFillArea = Rectangle(pt1, pt2)
        
        if(fill):
            rectFillArea.setFill("red")
            #print("here")
        else:
            rectFillArea.setFill("white")
            #print("white")
        
        rectFillArea.draw(self.window)
    
    #get a cell from the point that you click
    def getCellFromPoint(self, point):
        point = Point(math.ceil(point.x / self.cell_size), math.ceil(point.y / self.cell_size))
        
        return point
    
    
    









