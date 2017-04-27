#Sydney Howard, showard

from tkinter import *
import string, math


def checkIfEmpty(a):            #checks if gradebook has no quizzes
    cols= len(a[0])
    rows= len(a)
    for col in range(cols):
        for row in range(rows):
            if a[row][col]!=-1:
                return True

def bestQuiz(a):
    cols, rows= len(a[0]),len(a)
    currGradeNum, bestGradeNum=-1, -1
    currGradeAve, bestGradeAve=0, -1
    numOfNums,sum=0, 0
    if checkIfEmpty(a) == True:
        for col in range(cols):
            for row in range(rows):
                if (a[row][col]) == -1:continue #ignore empty quiz scores
                else: 
                    sum+=(a[row][col])
                    numOfNums+=1
            if numOfNums!=0: currGradeAve= int(sum/numOfNums) #disregard -1's
            currGradeNum,sum,numOfNums =col,0,0
            if currGradeAve> bestGradeAve: #updates bestGradeAve
                bestGradeAve= currGradeAve
                bestGradeNum=currGradeNum
            elif currGradeAve== bestGradeAve:
                bestGradeNum= min(currGradeNum, bestGradeNum)
            currGradeAve=0
        return bestGradeNum

def findInitialStart(board):
    rows, cols= len(board), len(board[0])   #finds the 1 position
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1: 
                return row, col,1
    return False

def checkDirections(board,startRow, startCol,dir,currNum):
    rows, cols= len(board), len(board[0])
    dirs= [ (-1,-1), (-1,0), (-1, +1), #the directions to check in
            (0,-1),          (0, +1),
            (+1,-1), (+1,0), (+1,+1)]
    (drow, dcol) = dirs[dir]
    for i in range(8):
        row= startRow + drow        #checks for consecutive numbers
        col = startCol + dcol
        if row<0 or col<0 or row>=rows or col>=cols: return False
        elif (board[row][col] == currNum+1):
            return row, col, (board[row][col])
    return False
    

def isKingsTour(board): 
    rows= len(board)
    if findInitialStart(board) == False: return False #gets initial position
    else: startRow, startCol, currNum= findInitialStart(board)
    for i in range(rows**2):
        for dir in range(8):        #checks all directions
            if checkDirections(board,startRow,startCol,dir,currNum) !=False:
                startRow, startCol, currNum= checkDirections(board,
                                    startRow,startCol,dir,currNum)
            else: continue
    if currNum== rows**2: return True
    else: return False
            


####### test fcns

def testCheckIfEmpty():
    print("testing checkIfEmpty()...", end="")
    a = [ [-1,  -1, -1 ],
        [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    a = [ [-1,  -1, -1,-1 ],
        [-1, -1, -1,  -1],
        [-1,-1,-1,-1]]
    assert(bestQuiz(a) == None)
    a = [[],
        []]
    assert(bestQuiz(a) == None)
    print("passed")


def testBestQuiz():
    print("Testing bestQuiz()...", end="")
    a = [ [ 88,  80, 91 ],
        [ 68, 100, -1 ]]
    assert(bestQuiz(a) == 2)
    a = [ [ 88,  80, 80 ],
            [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88,  -1, -1 ],
        [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1,  -1, -1 ],
        [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    a = [ [ 88, -1, 91 ],
        [ 68, 100, -1 ]]
    assert(bestQuiz(a) == 1)
    a = [ [ 80, 91 ],
        [ 100, -1 ]]
    assert(bestQuiz(a) == 1)
    a = [ [ 0,  80],
        [ 68, 100]]
    assert(bestQuiz(a) == 1)
    print("Passed!")

def testCheckDirections():
    print("testing checkDirections")
    assert(checkDirections([ 
      [  1, 14, 15, 16],
      [ 13,  2,  7,  6],
      [ 12,  8,  3,  5],
      [ 11, 10,  9,  4]
    ], 0,0,1,1) == 1,1,2)
    assert(checkDirections([[3,2,1],
    [6,4,9],
    [5,7,8]], 0,2,1,1) == 0,1,2)
    assert(checkDirections([[3,2,1],
    [6,4,9],
    [5,7,8]], 2,0,3,4) == 2,0,5)
    print("passed")

def testFindInitialStart():
    print("testing findInitialStart")
    assert(findInitialStart([ 
      [  1, 14, 15, 16],
      [ 13,  2,  7,  6],
      [ 12,  8,  3,  5],
      [ 11, 10,  9,  4]
    ]) == 0,0,1)
    assert(findInitialStart([
    [3,2,1],
    [6,4,9],
    [5,7,8]]) == 0,2,1)
    assert(findInitialStart(
    [[7,8,9,10],
    [6,3,2,11],
    [5,4,0,12],
    [16,15,14,13]]) == False)
    print("passed")

def testIsKingsTour():
    print("Testing isKingsTour()")
    assert( isKingsTour([ [  1, 14, 15, 16],
      [ 13,  2,  7,  6],
      [ 12,  8,  3,  5],
      [ 11, 10,  9,  4]
    ]) == True)
    assert(isKingsTour(
    [[3,2,1],
    [6,4,9],
    [5,7,8]]) == True)
    assert(isKingsTour(
    [[1,2,3],
    [7,4,8],
    [6,5,9]]) == False)
    assert(isKingsTour(
    [[3,2,1],
    [6,4,0],
    [5,7,8]]) == False)
    assert(isKingsTour(
    [[1,2,3,4],
    [7,4,8],
    [6,5,9]]) == False)
    assert(isKingsTour(
    [[1,1,3],
    [7,4,8],
    [6,5,9]]) == False)
    assert(isKingsTour(
    [[7,8,9,10],
    [6,3,2,11],
    [5,4,1,12],
    [16,15,14,13]]) == True)
    print("passed")


# testCheckIfEmpty()
# testBestQuiz()
# testIsKingsTour()
# testFindInitialStart()
# testCheckDirections()



####################################
# customize these functions
####################################

def make2dList(rows, cols,n):
    a=[]
    for row in range(rows): a += [[n]*cols]
    return a
#from: http://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
    
def init(data):
    data.currRow= data.rows//2
    data.currCol= data.cols//2
    data.cellValues = make2dList(data.rows,data.cols,-1)
    data.currPlayer= 0
    data.highlightColors= ['lightBlue', 'orange']
    data.textColors= ['darkBlue', 'darkOrange']
    data.cellColors= make2dList(data.rows,data.cols,-1)
    data.cellTextColors=make2dList(data.rows,data.cols,-1)
    data.scoreP1=0
    data.scoreP2=0
    data.turnSum=0
    data.finalScore=5
    data.bestRoundTurnSum=[0,0]

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == "Right":             #checks direction keys
        data.currCol = data.currCol +1
        if data.currCol >= data.cols:
            data.currCol= 0
    if event.keysym == "Left":
        data.currCol = data.currCol-1
        if data.currCol <0:
            data.currCol= data.cols-1
    if event.keysym == "Up":
        data.currRow = data.currRow -1
        if data.currRow <0:
            data.currRow= data.rows-1
    if event.keysym== "Down":
        data.currRow= data.currRow+1
        if data.currRow >=data.rows:
            data.currRow = 0
    if event.keysym == "r":
        data.cellValues= make2dList(data.rows,data.cols,-1)
        if data.currPlayer==0:
            data.scoreP1+=1
        if data.currPlayer==1:
            data.scoreP2+=1
    if (event.keysym in string.digits and     #checks for digit keys pressed
        data.cellValues[data.currRow][data.currCol]==-1):
        data.cellValues[data.currRow][data.currCol]= event.keysym
        if data.cellColors[data.currRow][data.currCol]==-1:
            data.cellColors[data.currRow][data.currCol]=\
            (data.highlightColors[data.currPlayer])
        if data.cellTextColors[data.currRow][data.currCol]==-1:
            data.cellTextColors[data.currRow][data.currCol]=\
            (data.textColors[data.currPlayer])
        if data.currPlayer==0:      #change player
            data.currPlayer=1 
            if turnSum(data) == True:
                data.scoreP1+=1
                data.cellValues = make2dList(data.rows,data.cols,-1)
                data.bestRoundTurnSum=[0,0]
                data.currRow= data.rows//2
                data.currCol= data.cols//2
        else:
            data.currPlayer=0       #change player
            if turnSum(data)==True:
                data.scoreP2+=1
                data.cellValues = make2dList(data.rows,data.cols,-1)
                data.bestRoundTurnSum=[0,0]
                data.currRow= data.rows//2
                data.currCol= data.cols//2
    if data.scoreP1==data.finalScore+1 or data.scoreP2==data.finalScore+1:
        data.scoreP1=0
        data.scoreP2=0
                
                
def timerFired(data):
    pass
    
def turnSum(data):
    data.turnSum=0
    dirs = [ (-1, -1), (-1, 0), (-1, +1),       #check in all directions
                ( 0, -1),(0,0),( 0, +1),
                (+1, -1), (+1, 0), (+1, +1) ]
    for dir in range(9):
        drow,dcol= dirs[dir]
        row=data.currRow+drow
        col= data.currCol+dcol
        if (row<0 or row>=data.rows or col<0 or col>= data.cols 
            or data.cellValues[row][col]==-1):  #makes sure doesn't check
            continue                            #outside of board
        if data.cellValues[row][col] !=-1:
            data.turnSum+= int(data.cellValues[row][col])
            data.bestRoundTurnSum[data.currPlayer]=data.turnSum
        if data.turnSum== 42:
            return True

def drawGrid(canvas,data):
    margin=20
    CW= (data.width-2*margin)//data.cols   
    CH= (data.height-2*margin)//data.rows
    for row in range(data.rows):
        for col in range(data.cols):    
            (canvas.create_rectangle(margin+col*CW, CH*row+2*margin,
            margin+(col+1)*CW, CH*(row+1)+2*margin)) #draws grid
            if row== data.currRow and col == data.currCol:
                (canvas.create_rectangle(margin+col*CW, CH*row+2*margin, 
                margin+(col+1)*CW, CH*(row+1)+2*margin, #draws rectangles
                fill= data.highlightColors[data.currPlayer]))
            if data.cellValues[row][col] == -1: 
                continue
            if data.cellValues[row][col]!=-1:   #draws text
                (canvas.create_text(col*CH+margin+CH//2,
                row*CW+(margin*2)+CW//2,text=data.cellValues[row][col], 
                fill= data.cellTextColors[row][col]))

def checkIfBoardFull(data):
    cellValues1D=[]
    for i in data.cellValues:       #checks for full board
        for j in i:
            cellValues1D.append(j)
    if (-1 not in cellValues1D)== True:
        return True

def drawScores(canvas,data):
    margin=20
    (canvas.create_text(data.width//2-margin, margin, 
                    text= data.scoreP1,fill= "darkBlue"))   #displays scores
    (canvas.create_text(data.width//2+margin, margin, 
                    text= data.scoreP2,fill= "darkOrange"))
    if data.scoreP1==5:     #displays winning text when someone wins
        (canvas.create_text(data.width//2, data.height//2, 
            text= "Congrats Player 1, you won!", fill="red"))
    if data.scoreP2==5:
        (canvas.create_text(data.width//2, data.height//2, 
                text= "Congrats Player 2, you won!", fill="red"))
    if checkIfBoardFull(data)==True:    #checks highest score if board full
        if data.bestRoundTurnSum[0] > data.bestRoundTurnSum[1]:
            (canvas.create_text(data.width//2, data.height//2, 
                text= "Congrats Player 1, you won!", fill="red"))
        if data.bestRoundTurnSum[0] < data.bestRoundTurnSum[1]:
            (canvas.create_text(data.width//2, data.height//2, 
                    text= "Congrats Player 2, you won!", fill="red"))

def redrawAll(canvas, data):
    drawGrid(canvas,data) 
    drawScores(canvas,data)

def playGame42(rows,cols):
    cellSize= 50
    width,height = cellSize*cols, cellSize*rows
    run(rows,cols,width,height)
    

####################################
# use the run function as-is
####################################

def run(rows,cols,width=300, height=300):
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
        #canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.rows=rows
    data.cols=cols
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

playGame42(5,5)