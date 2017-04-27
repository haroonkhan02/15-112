# events-example0.py
# Barebones timer, mouse, and keyboard events
#Sydney Howard, showard


from tkinter import *
import math
import string
import random

####################################
# customize these functions
####################################

def init(data):
    data.rows=10
    data.cols=10
    data.rowHeight= data.height/data.rows
    data.colWidth= data.width/data.cols
    data.direction= (0,1)
    data.snake=[(data.rows//2, data.cols//2)]
    placeFood(data)
    data.gameOver=False
    data.isPaused=False

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym=="Up":
        data.direction=(-1,0)
    if event.keysym== "Down":
        data.direction=(1,0)
    if event.keysym== "Right":
        data.direction= (0,1)
    if event.keysym== "Left":
        data.direction= (0,-1)
    if event.keysym== "p":
        data.isPaused=True

def timerFired(data):
    if data.gameOver==False and data.isPaused==False:
        getDirection(data)
    if data.gameOver==True:
        pass

def drawBoard(canvas,data):
    if data.gameOver== False and data.isPaused==False:
        for row in range(data.rows):
            for col in range(data.cols):
                x0= col*data.colWidth
                x1= (col+1)*data.colWidth
                y0= row*data.rowHeight
                y1= (row+1)*data.rowHeight
                canvas.create_rectangle(x0, y0,x1,y1)
        if (data.foodRow,data.foodCol) not in data.snake:
            drawFood(canvas,data)
    drawSnake(canvas,data)
    if data.gameOver==True:
        drawGameOver(canvas,data)

def drawFood(canvas,data):
    (canvas.create_oval(data.foodCol*data.colWidth, 
        data.foodRow*data.rowHeight, (data.foodCol+1)*data.colWidth,
        (data.foodRow+1)*data.rowHeight,fill= "green"))

def drawSnake(canvas,data):
    for pair in data.snake:
        row,col= pair
        canvas.create_oval(col*data.colWidth, row*data.rowHeight, 
        (col+1)*data.colWidth, (row+1)*data.rowHeight, fill="blue")

def getDirection(data):
    drow, dcol= data.direction
    headRow, headCol= data.snake[0]
    newHeadRow, newHeadCol= (headRow+drow), (headCol+dcol)
    if newHeadRow <0 or newHeadRow>=data.rows or newHeadCol<0 or\
    newHeadCol>=data.cols or (newHeadRow,newHeadCol) in data.snake:
        data.gameOver=True
    else:
        data.snake.insert(0, (newHeadRow, newHeadCol)) 
        data.snake.pop()
        if newHeadRow==data.foodRow and newHeadCol==data.foodCol:
            data.snake.append((newHeadRow, newHeadCol)) 
            placeFood(data)

def drawGameOver(canvas,data):
    if data.gameOver==True:
        canvas.create_text(data.width/2, data.height/2, text= "GAME OVER")

def placeFood(data):
    while True:
        data.foodRow= random.randint(0, data.rows-1)
        data.foodCol = random.randint(0, data.cols-1)
        if (data.foodRow,data.foodCol) not in data.snake:
            return True
            
    


def redrawAll(canvas, data):
    drawBoard(canvas,data)

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
    data.timerDelay = 500 # milliseconds
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

run(400, 400)