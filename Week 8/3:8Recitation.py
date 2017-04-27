# events-example0.py
# Barebones timer, mouse, and keyboard events
#Sydney Howard,showard

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.mode="introMode"
    initGrid(data)
    urInit(data)
    initSS(data)

def mousePressed(event, data):
    if data.mode=="gridMode":
        mpGrid(event,data)
    if data.mode=="urMode":
        mpUR(event,data)

def keyPressed(event, data):
    if event.keysym=="1":
        data.mode="gridMode"
    if event.keysym=="2":
        data.mode="urMode"
    if event.keysym=="3":
        data.mode="imagesMode"
    if event.keysym=="4":
        data.mode="ssMode"
    if data.mode=="urMode":
        kpUR(event,data)

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.mode=="gridMode":
        drawGridMode(canvas,data)
    if data.mode=="urMode":
        drawUR(canvas,data)
    if data.mode=="ssMode":
        drawSS(canvas,data)

### Grid Mode

def initGrid(data):
    data.mode="introMode"
    data.rows=5
    data.cols=5
    data.margin=20
    data.click=(-1,-1)


def mpGrid(event,data):
    row= (event.y-data.margin)//data.cellHeight
    col= (event.x-data.margin)//data.cellWidth
    data.click=(row,col)

def getCellBounds(row,col,data):
    data.boardWidth= data.width-2*data.margin
    data.boardHeight=data.height-2*data.margin
    data.cellHeight=data.boardHeight/data.rows
    data.cellWidth= data.boardWidth/data.cols
    x0= row*data.cellWidth
    y0=col*data.cellHeight
    x1=(row+1)*data.cellWidth
    y1= (col+1)*data.cellHeight
    return x0,y0,x1,y1

def inBounds(x,y,data):
    return data.margin<=x<= data.width-data.margin and data.margin<=y<= data.height-data.margin

def drawGridMode(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            x0,y0,x1,y1=getCellBounds(row,col,data)
            fill= "orange" if inBounds(data.click[0],data.click[1],data)==True else "cyan"
            canvas.create_rectangle(x0,y0,x1,y1,fill=fill)
    canvas.create_text(data.width/2, data.height/2, text="Click in cells!")
            
            
            
#### Undo/Redo

def urInit(data):
    data.points=[]
    data.undo=[]

def mpUR(event,data):
    data.points.append((event.x,event.y))

def kpUR(event,data):
    if event.keysym=="u":
        if len(data.points)>0:
            data.undo.append(data.points.pop())
    if event.keysym=="r":
        if len(data.undo)>0:
            data.points.append(data.undo.pop())
    if event.keysym=="c":
        data.points=[]
        data.undo=[]
    
def drawUR(canvas,data):
    canvas.create_polygon(data.points, fill="pink")
    canvas.create_text(data.width/2, 50, text= str(len(data.points)) + " point(s) in polygon")
    canvas.create_text(data.width/2, 70, text= str(len(data.undo)) + " point(s) in the undoList")


### SideScroller

def initSS(data):
    data.scrollmarg= 50
    data.pX=0
    data.pY=0
    data.pHeight=40
    data.pWidth=20
    data.wallHeight=80
    data.wallWidth=40
    data.wallNum=5
    data.wallSpacing=100
    data.wallHit=(-1,-1)
    data.wallScore= [0]*data.wallNum

def playerBounds(data):
    x0,y1= data.width/2-data.scrollmarg, data.height/2
    x1,y0= x0+data.pWidth, y1-data.pHeight
    return x0,y0,x1,y1

def wallBounds(data):
    x0,y1= data.width/2-data.scrollmarg, data.height/2
    x1, y0= x0+ data.wallWidth, y1-data.wallHeight
    return  x0,y0,x1,y1

def intersect(x,y,data):
    ax0, ay0, ax1, ay1= x
    bx0, by0,bx1,by1=y
    return ax1>=bx0 or bx1>=ax0 or ay1>=by0 or by1>=ay0

def drawSS(canvas,data):
    playerCoords= playerBounds(data)
    canvas.create_oval(playerCoords, fill="cyan")
    wallCoords= wallBounds(data)
    fill="pink" if intersect(playerCoords, wallCoords,data) == True else "orange"
    canvas.create_rectangle(wallCoords, fill=fill)


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