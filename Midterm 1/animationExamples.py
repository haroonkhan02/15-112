### Grid Demo

from tkinter import *

def init(data):
    data.rows=5
    data.cols=5
    data.width=400
    data.height=400
    data.margin=20
    data.selection=(-1,-1)
  
def inBounds(x,y,data):
    return data.margin<=x<= data.width-data.margin and data.margin<=y<data.height-data.margin

def getCell(x,y,data):
    if inBounds(x,y,data)==False:
        return (-1,-1)
    boardWidth=data.width-2*data.margin
    boardHeight=data.height-2*data.margin
    cellWidth=boardWidth/data.cols
    cellHeight=boardHeight/data.rows
    col=(y-data.margin)//cellHeight
    row=(x-data.margin)//cellWidth
    return row,col
    
    
    
def getCellBounds(row,col,data):
    data.cellHeight= (data.height-2*data.margin)/data.rows
    data.cellWidth= (data.width-2*data.margin)/data.cols
    x0= data.margin+ row*data.cellHeight
    y0= data.margin + col*data.cellWidth
    x1= data.margin+ (1+row)*data.cellHeight
    y1= data.margin + (col+1)*data.cellWidth
    return x0,y0,x1,y1

def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            fill= "orange" if data.selection == (row,col) else "cyan"
            x0,y0,x1,y1= getCellBounds(row,col,data)
            canvas.create_rectangle(x0,y0,x1,y1, fill=fill)

def redrawAll(canvas,data):
    drawBoard(canvas,data)

def mousePressed(event,data):
    (row,col)= getCell(event.x,event.y,data)
    if data.selection== (row,col):
        data.selection=(-1,-1)
    else:
        data.selection=(row,col)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

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

#run(300, 300)

#### Undo Redo

def init(data):
    data.points=[]
    data.undo=[]

def mousePressed(event, data):
    data.points.append((event.x,event.y))

def keyPressed(event, data):
    if event.keysym=="u":
        if data.points!=[]:
            data.undo.append(data.points.pop())
    if event.keysym=="r":
        if data.undo!=[]:
            data.points.append(data.undo.pop())
    if event.keysym=="c":
        data.points,data.undo= [],[]
        
def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.points!=[]:
        canvas.create_polygon(data.points,fill="pink", outline="gold")
    canvas.create_text(data.width/2,40, text="To add points, click on screen. To undo points, type "u". To redo points, type "r"")

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

#run(400, 200)

### side scroller

def init(data):
    data.scrollX=0
    data.scrollMargin=50
    data.playerX=data.scrollMargin
    data.playerY=0
    data.playerHeight=20
    data.playerWidth=10
    data.walls=5
    data.wallPoints=[0]*data.walls
    data.wallWidth=20
    data.wallHeight=40
    data.wallSpacing=90
    data.currentWallHit=-1

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym=="Up": movePlayer(0,5,data)
    if event.keysym=="Down": movePlayer(0,-5,data)
    if event.keysym=="Right": movePlayer(5,0,data)
    if event.keysym=="Left": movePlayer(-5,0,data)

def timerFired(data):
    pass

def getPlayerBounds(data):
    x0,y1= data.playerX, data.height/2-data.playerY
    x1,y0= x0+data.playerWidth, y1-data.playerHeight
    return x0,y0,x1,y1

    
def getWallHit(data):
    playerBounds= getPlayerBounds(data)
    for wall in range(data.walls):
        wallBounds= getWallBounds(wall,data)
        if boundsIntersect(playerBounds,wallBounds):
            return wall
    return -1
    
def getWallBounds(wall,data):
    x0,y1= (1+wall)*data.wallSpacing, data.height/2
    x1,y0= x0+data.wallWidth, y1-data.wallHeight
    return x0,y0,x1,y1

def boundsIntersect(boundsA, boundsB):
    x0,y0,x1,y1= boundsA
    x2,y2,x3,y3= boundsB
    return x1>=x2 and x3>=x0 and y1>=y2 and y3>=y0

def movePlayer(dx,dy,data):
    data.playerX+=dx
    data.playerY+=dy
    if data.playerX< data.scrollX+data.scrollMargin:
        data.scrollX= data.playerX-data.scrollMargin
    if data.playerX>data.scrollX+data.width-data.scrollMargin:
        data.scrollX= data.playerX-data.width+data.scrollMargin
    wall=getWallHit(data)
    if wall!=data.currentWallHit:
        data.currentWallHit= wall
        if wall>=0:
            data.wallPoints[wall]+=1


def redrawAll(canvas, data):
    groundHeight=5
    canvas.create_rectangle(0,data.height/2,data.width,data.height/2+groundHeight, fill="black")
    for wall in range(data.walls):
        x0,y0,x1,y1= getWallBounds(wall,data)
        fill="orange" if wall==data.currentWallHit else "pink"
        canvas.create_rectangle(x0-data.scrollX, y0, x1-data.scrollX, y1,fill=fill)
        cx,cy= (x0+x1)/2- data.scrollX, (y0+y1)/2
        canvas.create_text(cx,cy,text= str(data.wallPoints[wall]))
        
    x0,y0,x1,y1= getPlayerBounds(data)
    canvas.create_oval(x0-data.scrollX, y0,x1-data.scrollX, y1, fill="cyan")

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

run(400, 200)

        