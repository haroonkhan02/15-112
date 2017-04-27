#Hw 11
#Sydney Howard, showard

# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.level=0
    
def drawHFractal(canvas,x,y,size,level):
    if level==0:
        canvas.create_line(x-size/2,y,x+size/2,y)   #horiz line
        canvas.create_line(x-size/2,y-size/2,x-size/2,y+size/2) #left vert line
        canvas.create_line(x+size/2,y-size/2,x+size/2,y+size/2)#right vert line
        
    else:
        canvas.create_line(x-size/2,y,x+size/2,y) #create small H at each point
        canvas.create_line(x-size/2,y-size/2,x-size/2,y+size/2)
        canvas.create_line(x+size/2,y-size/2,x+size/2,y+size/2)
        drawHFractal(canvas,x-size/2,y-size/2,size/2,level-1)
        drawHFractal(canvas,x+size/2,y-size/2,size/2,level-1)
        drawHFractal(canvas,x-size/2,y+size/2,size/2,level-1)
        drawHFractal(canvas,x+size/2,y+size/2,size/2,level-1)  

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym in ["Up", "Right"]:
        data.level+=1   #increase levels
    elif (event.keysym in ["Down", "Left"]) and data.level>0:
        data.level-=1   #decrease levels

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawHFractal(canvas,data.width/2,data.height/2,data.width/2,data.level)
            
    
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

#run(500, 500)


def make2dList(rows, cols):
    a=[]
    for row in range(rows):
        a += [[0]*cols]
    return a
#from: http://www.cs.cmu.edu/~112/notes/notes-2d-lists.html


def solveABC(constraints,aLocation):
    rows,cols= 5,5
    abcBoard= make2dList(rows,cols)
    aRow,aCol=aLocation
    abcBoard[aRow][aCol]="A"        #initialize A on board
    letters="BCDEFGHIJKLMNOPQRSTUVWXY"
    def solve(abcBoard,row=aRow, col=aCol,letters = letters):
        isEmpty=True
        possibleMoves=[(-1,-1),(-1,0),(-1,1),
                        (0,-1),      (0,1),
                        (1,-1),(1,0),(1,1)]
        for i in abcBoard:  #check for full board
            if 0 in i:
                isEmpty=False
        if isEmpty==True:
            return True
        else:
            letter=letters[0]
            for move in possibleMoves:
                if (isOnBoard(constraints,abcBoard,row+move[0],\
                col+move[1],letter)) and isLegal(constraints,abcBoard,\
                row+move[0],col+move[1],letter):
                    row=row+move[0] #check directions
                    col=col+move[1]
                    letters=letters[1:]
                    abcBoard[row][col]=letter
                    result=solve(abcBoard,row,col,letters)
                    if result==False:
                        abcBoard[row][col]=0    #undo move
                        letters=letter+letters
                        row=row-move[0]
                        col=col-move[1]
                    else:
                        return True
            return False
    if solve(abcBoard,aRow,aCol)==False:
        return None
    return abcBoard 

def isOnBoard(constraints,abcBoard,row,col,letter):
    rows,cols= 5,5  #check in bounds
    if row<0 or row>=rows or col<0 or col>=cols or abcBoard[row][col]!=0:
        return False   
    else: return True
        
def isLegal(constraints,abcBord,row,col,letter):
    constraints=list(constraints)
    clIndex= constraints.index(letter)  #check if in possible row/col
    if (clIndex==0 or clIndex==12) and row==col: return True
    if clIndex==6 or clIndex==18:
        if (row,col) in [(0,4), (1,3), (2,2), (3,1), (4,0)]: return True
    if (clIndex==1 or clIndex==17) and col==0: return True
    if (clIndex==2 or clIndex==16) and col==1: return True
    if (clIndex==3 or clIndex==15) and col==2:return True
    if (clIndex==4 or clIndex==14) and col==3:return True
    if (clIndex==5 or clIndex==13) and col==4: return True
    if (clIndex==7 or clIndex==23) and row==0: return True
    if (clIndex==8 or clIndex==22) and row==1: return True
    if (clIndex==9 or clIndex==21) and row==2:return True
    if (clIndex==10 or clIndex==20) and row==3: return True
    if (clIndex==11 or clIndex==19) and row==4:return True
    else:
        return False
  

def isinstance(a,b):
    return type(a) == b     #check for same class



class ComplexNumber(object):
    zero=None
    @staticmethod
    def getZero():      #check for class attribute
        if ComplexNumber.zero==None:
            ComplexNumber.zero=ComplexNumber()
            return ComplexNumber.zero
        else:
            return ComplexNumber.zero
    def __init__(self,real=0,imag=0,zero=None):
        self.zero=zero
        self.real=real
        self.imag=imag
        if isinstance(self.real,ComplexNumber): #when real num is entire num
            self.real,self.imag=int(str(self.real)[0]),int(str(self.real)[2])   
    def __repr__(self):
        return "%s+%si" % (self.real,self.imag)
    def realPart(self):
        return self.real
    def imaginaryPart(self):
        return self.imag
    def __eq__(self,other):
        if self.imag==0 and self.real==other:
            return True
        return isinstance(other,ComplexNumber) and self.imag==other.imag\
        and self.real==other.real and self.zero==other.zero
    def __hash__(self):
        return hash(self.imag)
    
def testComplexNumberClass():
    print("Testing ComplexNumber class... ", end="")
    # Do not use the builtin complex numbers in Python!
    # Only use integers!

    c1 = ComplexNumber(1, 2)
    assert(str(c1) == "1+2i")
    assert(c1.realPart() == 1)
    assert(c1.imaginaryPart() == 2)

    c2 = ComplexNumber(3)
    assert(str(c2) == "3+0i") # default imaginary part is 0
    assert(c2.realPart() == 3)
    assert(c2.imaginaryPart() == 0)

    c3 = ComplexNumber()
    assert(str(c3) == "0+0i") # default real part is also 0
    assert(c3.realPart() == 0)
    assert(c3.imaginaryPart() == 0)

    # Here we see that the constructor for a ComplexNumber
    # can take another ComplexNumber, which it duplicates
    c4 = ComplexNumber(c1)
    assert(str(c4) == "1+2i")
    assert(c4.realPart() == 1)
    assert(c4.imaginaryPart() == 2)

    assert((c1 == c4) == True)
    assert((c1 == c2) == False)
    assert((c1 == "Yikes!") == False) # don't crash here
    assert((c2 == 3) == True)

    s = set()
    assert(c1 not in s)
    s.add(c1)
    assert(c1 in s)
    assert(c4 in s)
    assert(c2 not in s)

    assert(ComplexNumber.getZero() == 0)
    assert(isinstance(ComplexNumber.getZero(), ComplexNumber))
    assert(ComplexNumber.getZero() == ComplexNumber())
    # This next one is the tricky part -- there should be one and
    # only one instance of ComplexNumber that is ever returned
    # every time you call ComplexNumber.getZero():
    assert(ComplexNumber.getZero() is ComplexNumber.getZero())
    # Hint: you might want to store the singleton instance
    # of the zero in a class attribute (which you should
    # initialize to None in the class definition, and then
    # update the first time you call getZero()).

    print("Passed!")

#testComplexNumberClass()

def testSolveABC():
    print('Testing solveABC()...', end='')
    constraints = "CHJXBOVLFNURGPEKWTSQDYMI"
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    constraints= "TYFSQMEOXLIJUKHBVWNGDCPR"
    aLocation=(3,1)
    board=solveABC(constraints,aLocation)
    solution=[["W","V","R","Q","O"],
              ["X","U","S","N","P"],
              ["Y","C","T","L","M"],
              ["D","A","B","I","K"],
              ["E","F","G","H","J"]]
    constraints="QYFSTMEOXLIJUKHBVWNGDCPR"
    aLocation=(3,1)
    board=solveABC(constraints,aLocation)
    solution=None
    assert(board == solution)
    print('Passed!')

#testSolveABC()





