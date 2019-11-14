import numpy as np
from WindowManager import GridWindow
import threading
import keyboard

"""Let's write an algorithm!

CONWAY'S GAME OF LIFE

for each live tile
if tile has 1 neigbor, starve
if tile has 2 or 3 neigbors, survive
if tile has 4 neigbors, die via overpopulation

for each dead tile
if has 3 neighbors turn live

"""

from datetime import datetime



class ConwaysGameOfLife:
    #manages the simulation
    updatedTime = datetime.now()
    
    startTime = datetime.now()
    
    def play(self):
        print("""Welcome to Conway's Game of life. The rules are as follows:
              
            Each live tile with 1 or fewer neighbors will die, equated to starvation
            Each live tile with 2 or 3 neighbors will survive
            Each live tile with 4 or more neigbors will die, equated to overpopulation
            
            Each dead tile with 3 neighbors will resurrect
            
            Click any tile to toggle, and press spacebar twice to begin
              """)
            
            
        self.window = GridWindow(20, 20)
        
        keyInput_thread = threading.Thread(target=self.keyInputThread)
        keyInput_thread.start()
        
        self.tiles = np.zeros((self.window.cell_num, self.window.cell_num))
        
        self.initValues()
        
        self.window.updateGrid(self.tiles, self.tiles)
        
        #does anyone format strings like this anymore? the world may never know.
        
        
        
        
        #print(keyInput_thread._target)
        
        while True:
            self.tick()
            #self.printTest("complete")
            #time.sleep(0.5)
            
        
        self.window.window.close()
    
    #main function that ticks the game forward
    def tick(self):
        newTiles = np.array(self.tiles)
        
        liveTiles = self.getLiveTiles()
        
        newTiles = np.zeros((self.window.cell_num, self.window.cell_num))
        
        #self.printTest("init")
        
        for tile in liveTiles:
            self.updateTile(tile)
            neighbors = self.getNeighbors(tile, False)
            
            newTiles[tile[0], tile[1]] = self.updateTile(tile)
            
            for neighbor in neighbors:
                newTiles[neighbor[0], neighbor[1]] = self.updateTile(neighbor)
        
        #self.printTest("Live Tiles")
        
        self.window.updateGrid(self.tiles, newTiles)
        
        self.tiles = newTiles
        
    
    def updateTile(self, position):
        tile = self.tiles[position[0], position[1]]
        numNeighbors = len(self.getNeighbors(position, True))
        
        if(tile == 1):
            if(numNeighbors < 2 or numNeighbors > 3):
                return 0
            else:
                return 1
        else:
            if(numNeighbors == 3): 
                return 1
    
    #returns neighbors of a cell in a list
    def getNeighbors(self, position, justOnes):
        neighborPositions = []
        for x in range(position[0] - 1, position[0] + 2):
            for y in range(position[1] - 1, position[1] + 2):
                if(x == position[0] and y == position[1]):
                    continue
                try: #nestbuilder
                    tile = self.tiles[x, y] # will trigger catch if out of the window
                    if(justOnes):
                        if(tile == 1):
                            neighborPositions.append((x, y))
                    else:
                        neighborPositions.append((x, y))
                except:
                    continue
        return neighborPositions
    
    def initValues(self):
        done = False
        while (not done):
            point = self.window.window.checkMouse()

            if(point):
                cellPosition = self.window.getCellFromPoint(point) #of type Point from graphics
                
                tile = self.tiles[int(cellPosition.x), int(cellPosition.y)]
                
                self.tiles[int(cellPosition.x), int(cellPosition.y)] = (1 if tile == 0 else 0)
                
                self.window.updateGridPoint((cellPosition.x, cellPosition.y), True if tile == 0 else False)
                
            
            if(self.window.window.checkKey()):
                if(self.window.window.getKey() == "space"):
                    done = True
        print("finished initialization. Running...")
    
    def getLiveTiles(self):
        liveTiles = []
        for x in range(self.window.cell_num):
            for y in range(self.window.cell_num):
                if(self.tiles[x, y] == 1):
                    liveTiles.append((x, y))
        return liveTiles
    
    def printTest(self, message):
        print(str(datetime.now() - self.updatedTime) + " " + str(message))
        self.updatedTime = datetime.now()
    
    def keyInputThread(self):

        if(keyboard.is_pressed("escape")):
            print("yuh")
                #if(self.window.window.getKey() == "escape"):
                    #self.window.window.close()
        
        
    
GoL = ConwaysGameOfLife()

GoL.play()