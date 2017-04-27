# events-example0.py
# Barebones timer, mouse, and keyboard events
# Sydney Howard, showard

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.mode="introMode"
    data.boardSide=600
    data.rows=10
    data.cols=10
    data.cellSize= data.boardSide/data.rows
    data.offsetX= data.boardSide-data.width
    data.offsetY= data.boardSide-data.height
    data.fontInfo= 12
    data.helpScrollBool=True
    data.helpScroll=data.width//2
    data.isGameOver=False
    data.timeLeft=20000
    data.boardScore= make2dList(data.rows,data.cols,0)
    data.currRow=7
    data.currCol=7
    
def mousePressed(event, data):
    if data.mode== "helpMode":
        mousePressedHelpMode(event,data)
    if data.mode== "gameOverMode":
        mousePressedGameOverMode(event,data)
    if data.mode== "winMode":
        mousePressedWinMode(event,data)
    if data.mode== "playMode":
        mousePressedPlayMode(event,data)

def keyPressed(event, data):
    if data.mode== "introMode":
        keyPressedIntroMode(event,data)
    elif data.mode== "playMode":
        keyPressedPlayMode(event,data)
    elif data.mode == "helpMode":
        keyPressedHelpMode(event,data)
    elif data.mode == "gameOverMode":
        keyPressedGameOverMode(event,data)
    elif data.mode== "winMode":
        keyPressedWinMode(event,data)
    
def timerFired(data):
    if data.mode== "introMode":
        timerFiredIntroMode(data)
    if data.mode== "helpMode":
        timerFiredHelpMode(data)
    if data.mode== "playMode":
        timerFiredPlayMode(data)
    
def redrawAll(canvas, data):
    if data.mode== "introMode":
        drawIntroText(canvas,data)
    if data.isGameOver==False:
        if data.mode== "playMode":
            drawBoard(canvas, data)
            drawBoardText(canvas,data)
            drawTimer(canvas,data)
    if data.mode=="helpMode":
        drawHelpText(canvas,data)
    if data.mode== "gameOverMode":
        drawGameOver(canvas,data)
    if data.mode == "winMode":
        drawWinMode(canvas,data)

def make2dList(rows, cols,n):       #creates a 2D list 
    a=[]
    for row in range(rows): a += [[n]*cols]
    return a
#from: http://www.cs.cmu.edu/~112/notes/notes-2d-lists.html     
        
### INTRO MODE
 
def keyPressedIntroMode(event,data):
    if event.keysym== 'p':
        data.mode= "playMode"
    if event.keysym== 'h':
        data.mode= "helpMode"

def timerFiredIntroMode(data):  #makes text zoom in and out
    if data.fontInfo<=25:
        data.fontInfo+=2
    else: data.fontInfo = 12

def drawIntroText(canvas,data):
    (canvas.create_text(data.width//2, data.height//3, 
        text= "The Hw6 Game-Like App!",font=( "Papyrus",data.fontInfo)))
    (canvas.create_text(data.width//2, data.height//2, 
        text= "Press 'p' to play, 'h' for help!",font="Papyrus"))


### HELP MODE

def mousePressedHelpMode(event,data):
    data.mode= "introMode"

def timerFiredHelpMode(data):
    if data.helpScrollBool==False:      #makes text move side to side
        data.helpScroll-=10
        if data.helpScroll<=0:
            data.helpScrollBool= True
    elif data.helpScrollBool==True:
        data.helpScroll+=10
        if data.helpScroll>=data.width:
            data.helpScrollBool= False

def drawHelpText(canvas,data):      
    if data.helpScrollBool==True:           #changes color of text
        color="maroon"  
    else: color= "darkGreen"
    (canvas.create_text(data.helpScroll, data.height//2, 
        text= "This is not very helpful!!",fill=color,
        font=("Papyrus", 25, UNDERLINE)))
    (canvas.create_text(data.width//2, data.height-data.height//6, 
        text="Press mouse to return to caller's mode", font= ("Papyrus", 12)))

def keyPressedHelpMode(event,data):
    if event.keysym== "h":
        data.mode= "playMode"

    
 ### PLAY MODE   

def drawBoard(canvas,data):
    for row in range(data.rows):    #creates board grid
        for col in range(data.cols):
            if (row+col)%2 == 0: 
                if data.currRow==row and data.currCol==col:
                    color="yellow"  #changes color if dot is in cell
                else: color= "lightYellow"
            else: 
                if data.currRow==row and data.currCol==col:
                    color='blue'
                else: color= "lightBlue"
            x0= col*data.cellSize-data.offsetX
            y0= row*data.cellSize - data.offsetY
            x1= x0+data.cellSize
            y1= y0+data.cellSize
            canvas.create_rectangle(x0,y0,x1,y1,fill=color)
            drawDot(canvas,data)
            (canvas.create_text((x0+x1)/2,(y0+y1)/2-data.cellSize/3,
                text="("+ str(row) + "," + str(col) + ")"))
            (canvas.create_text((x0+x1)/2,(y0+y1)/2+data.cellSize/4,
                text=data.boardScore[row][col]))

def drawBoardText(canvas,data):
    (canvas.create_text(data.width/2,data.height-10, 
        text="Press 'h' for help! Use Space, Tab,MouseButton + Arrows!", 
        fill="blue", font=("Papyrus",11)))

def boardScore(data):
    xDist= data.offsetX+data.width/2       #gets score of points on board
    yDist= data.offsetY+data.height/2
    row=int(yDist//data.cellSize)
    col=int(xDist//data.cellSize)
    if row!= data.currRow or col!=data.currCol: #checks if dot is in cell
        data.boardScore[row][col]+=1
        data.currRow=row
        data.currCol=col
  
def clickOnBoard(event,data):
    x= data.width/2-event.x         #difference between click and dot
    y= data.height/2-event.y
    data.offsetX= (data.offsetX-x)  #relocates screen
    data.offsetY= (data.offsetY-y)
    boardScore(data)
    

def drawDot(canvas,data): 
    radius=7
    (canvas.create_oval(data.width/2-radius,data.height/2-radius, 
        data.width/2+radius, data.height/2+radius, fill="maroon"))

def drawTimer(canvas,data):
    rectWidth= 100
    rectHeight=20
    if data.timeLeft <=5000:        #draws rectangle behind timer
        color="red"
    elif data.timeLeft <= 10000:
        color="yellow"
    else:
        color="grey"
    canvas.create_rectangle(0,0,rectWidth,rectHeight,fill=color)
    (canvas.create_text(rectWidth/2,rectHeight/2, 
        text= str(data.timeLeft//1000) + " seconds"))
 
    
def timerFiredPlayMode(data):
    data.timeLeft-=data.timerDelay  #makes timer count down 
    if data.timeLeft<=0:
        data.isGameOver= True       #checks if timer goes to 0
        data.timeLeft=20000
        data.mode= "gameOverMode"

def keyPressedPlayMode(event,data):
    data.dotSpeed=5
    if event.keysym== "Up":
        data.offsetY-= data.dotSpeed
    if event.keysym== "Down":
        data.offsetY+= data.dotSpeed
    if event.keysym== "Right":
        data.offsetX+= data.dotSpeed
    if event.keysym== "Left":
        data.offsetX-= data.dotSpeed
    if event.keysym== "h":
        data.mode= "helpMode"
    if event.keysym== "space":
        data.timeLeft=20000
    if event.keysym== "Tab":
        data.mode="winMode"
    boardScore(data)

def mousePressedPlayMode(event,data):
    clickOnBoard(event,data)

### GAME OVER MODE

def drawGameOver(canvas,data):
    (canvas.create_text(data.width/2, data.height/3, 
        text= "Game Over!!! You Lose :(", font= ("Papyrus", 20)))
    (canvas.create_text(data.width/2, data.height-20, 
        text= "Press key or mouse to start over", font= ("Papyrus", 15)))
    
def keyPressedGameOverMode(event,data):
    init(data)                          #resets game when game is over
    data.mode= "playMode"

def mousePressedGameOverMode(event,data):
    init(data)                          #resets game
    data.mode= "playMode"

### WIN MODE

def drawWinMode(canvas,data):
    (canvas.create_text(data.width/2, data.height/3, 
        text= "Game Over!!! You Win :)", font= ("Papyrus", 20)))
    (canvas.create_text(data.width/2, data.height-20, 
        text= "Press key or mouse to start over", font= ("Papyrus", 15)))
    
def keyPressedWinMode(event,data):
    init(data)                      #reset game
    data.mode= "playMode"

def mousePressedWinMode(event,data):
    init(data)                      #resets game
    data.mode= "playMode" 
    
 #### TEST FCNS
 
 
def initTest(data): 
    data.cellSize=data.boardSide/data.rows
    data.width=600
    data.height=600
    data.offSetX=64.0
    data.offSetY=-4.0
    data.currRow=2
    data.currCol=3
    boardScore(data)
    
def testBoardScore():
    class Struct(object): pass
    testData = Struct()
    initTest(testData)
    assert(data.boardScore[row][col], data.currRow, data.currCol== 1,2,3)
    
    
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
    data.timerDelay = 100 # milliseconds
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

run(300, 300)