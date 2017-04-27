#Sydney Howard, showard
#Lab partners: Kasdan Bakos (kbakos), Jack Sampiere (jsampier)
#Also got help from: siqingy; approved by Kosbie

from tkinter import *
import random
import decimal
import string
####################################
# customize these functions
####################################

### CONTROL

def init(data):
    data.rows=15
    data.cols=10
    data.margin= 20
    data.emptyColor= "blue"
    data.board= make2dList(data.rows,data.cols,data.emptyColor)
    getTetrisPiece(data)
    newFallingPiece(data)
    data.isGameOver= False
    data.isPaused= False
    data.score=0

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):     
    if event.keysym== "Right":
        moveFallingPiece(data,0,1)
    if event.keysym== "Left":
        moveFallingPiece(data,0,-1)
    if event.keysym== "Up":
        rotateFallingPiece(data)
    if event.keysym== "Down":
        moveFallingPiece(data,1,0)
    if event.keysym== "r":          #resets game
        data.board= make2dList(data.rows,data.cols,data.emptyColor)
        data.isGameOver=False
        data.isPaused= False

def timerFired(data):
    if data.isPaused==False:
        if moveFallingPiece(data,1,0) == False:
            placeFallingPiece(data)
            newFallingPiece(data)
            removeFullRows(data)
        if fallingPieceIsLegal(data)==False:
            data.isGameOver=True
            data.score=0

### MODEL


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding optiorns here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
    
def make2dList(rows, cols,n):
    a=[]
    for row in range(rows): a += [[n]*cols]
    return a
#from: http://www.cs.cmu.edu/~112/notes/notes-2d-lists.html

def getTetrisPiece(data):
    data.iPiece = [[ True, True, True, True]]
    data.jPiece = [[ True, False, False ],[ True, True, True]]
    data.lPiece = [[ False, False, True],[ True,  True,  True]]
    data.oPiece = [[ True, True],[ True, True]]
    data.sPiece = [[ False, True, True],[ True,  True, False ]]
    data.tPiece = [[ False, True, False ],[ True,  True, True]]
    data.zPiece = [[ True,  True, False ],[ False, True, True]]
    data.tetrisPieces= ([data.iPiece, data.jPiece, data.lPiece, 
                    data.oPiece, data.sPiece, data.tPiece, data.zPiece])
    data.tetrisPieceColors = ([ "red", "yellow", "magenta", "pink",
                                "cyan", "green", "orange"])

def getCellBounds(row,col,data):        #finds coordinates for each cell
    gridWidth= data.width - 2*data.margin
    gridHeight= data.height - 2*data.margin
    x0= data.margin + gridWidth * col / data.cols
    x1= data.margin + gridWidth * (col+1) / data.cols
    y0= data.margin + gridHeight * row / data.rows
    y1= data.margin + gridHeight * (row+1) / data.rows
    return x0, y0, x1, y1

def newFallingPiece(data):       #chooses new piece and places it on board
    data.fallingPiece= random.choice(data.tetrisPieces)
    data.fallingPieceColor= random.choice(data.tetrisPieceColors)
    data.fallingPieceRow=0
    data.pieceCols= len(data.fallingPiece[0])//2
    data.fallingPieceCol=data.cols//2- data.pieceCols
    
def fallingPieceIsLegal(data):
    rows,cols=len(data.fallingPiece), len(data.fallingPiece[0])
    for row in range(rows):
        for col in range(cols):
            if data.fallingPiece[row][col] == True:    #if a colored cell
                if data.fallingPieceRow<0 or\
                data.fallingPieceCol>=data.cols-cols+1 or\
                data.fallingPieceCol<=-1 or\
                data.fallingPieceRow>=data.rows-rows+1 or\
                (data.board[data.fallingPieceRow+row][data.fallingPieceCol+col]
                !=data.emptyColor):  #checks piece is in bounds
                    return False
    return True   

def moveFallingPiece(data,drow,dcol):
    data.fallingPieceRow+=drow          #moves piece
    data.fallingPieceCol+=dcol
    if fallingPieceIsLegal(data) ==False:
        data.fallingPieceRow-=drow      #undos move
        data.fallingPieceCol-=dcol
        return False
    return True
        
def rotateFallingPiece(data):
    oldPiece,newPiece=data.fallingPiece, []
    oldRow,oldCol=data.fallingPieceRow,data.fallingPieceCol 
    oldRows,oldCols =len(data.fallingPiece), len(data.fallingPiece[0])
    newRow,newCol,newRows,newCols=oldCol, oldRow,oldCols,oldRows
    data.fallingPieceCol= oldCol + oldCols//2 - newCols//2
    data.fallingPieceRow= oldRow+ oldRows//2-newRows//2
    for i in range(oldCols): newPiece.append([0]*oldRows)
    for row in range(oldRows):   
        for col in range(oldCols):
           if oldPiece[row][col] == True:
               newPiece[oldCols-1-col][row]= True   #flips old rows and cols
    data.fallingPiece= newPiece     #rotates the piece
    if fallingPieceIsLegal(data) == True: #checks if piece is legal
        data.fallingPiece= newPiece
    else: 
        data.fallingPieceRow=0 
        data.fallingPieceCol=data.cols//2- data.pieceCols

def placeFallingPiece(data):
    rows,cols=len(data.fallingPiece), len(data.fallingPiece[0])
    for row in range(rows):
        for col in range(cols):     #places piece colors on board
            if data.fallingPiece[row][col]==True:
                data.board[data.fallingPieceRow+row][data.fallingPieceCol+col]=\
                    (data.fallingPieceColor)
    
def removeFullRows(data):
    newBoard=[]
    for row in range(data.rows):
        if "blue" not in data.board[row]:       #checks for full rows
            newBoard.insert(0,[data.emptyColor]*data.cols)
            data.score+=1
        if "blue" in data.board[row]:       #saves rows that aren't full
            newBoard.append(data.board[row])
    data.board=newBoard


### DRAW



def drawGame(canvas,data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill= "orange")
    drawBoard(canvas,data)          #draws all components of game
    drawFallingPiece(canvas,data)

def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols): 
            drawCell(canvas,data,row,col,data.board[row][col])

def drawFallingPiece(canvas,data):
    if data.isGameOver==False:
        for row in range(len(data.fallingPiece)):
            for col in range(len(data.fallingPiece[0])):
                if data.fallingPiece[row][col] == True:#draws new piece
                    (drawCell(canvas,data,data.fallingPieceRow+
                    row,data.fallingPieceCol+col,data.fallingPieceColor))
    else:
        data.isPaused=True      #is called when game is over
        (canvas.create_text(data.width//2, data.height//2, 
                text= "GAME OVER. Hit 'r' to restart game."))


def drawCell(canvas,data,row,col,color):
    miniMargin=1
    (x0, y0, x1, y1) = getCellBounds(row, col, data)#draws spaces between cells
    canvas.create_rectangle(x0, y0, x1, y1, fill="black") 
    (canvas.create_rectangle(x0+miniMargin, y0+miniMargin, x1-miniMargin, 
                                y1-miniMargin, fill=color))

def drawScore(canvas,data):
    (canvas.create_text(data.width//4, data.margin//2, 
                        text="Score="+ str(data.score)))
     
def redrawAll(canvas, data):
    drawGame(canvas,data) 
    drawScore(canvas,data)  
    
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 200 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")



def playTetris():
    rows=15
    cols=10
    margin=20
    cellSize=40
    width=2*margin+cols*cellSize
    height= 2*margin+ rows*cellSize
    run(width,height)

##### TEST FCNS    

def testMoveFallingPiece():
    print("testing moveFallingPiece")
    assert(moveFallingPiece(data,1,0) == True)
    assert(moveFallingPiece(data,0,-1) == True)
    assert(moveFallingPiece(data,-1,0) == False)
    print("passed")    
    

playTetris()
#testMoveFallingPiece()