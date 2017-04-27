#HW 7
#Sydney Howard, showard

import random
import copy
import math
import string

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


### 3. s16-quiz7x:
"""
CT1: 
start: [[0,1],[0]]
a [[6,1,5],[0],[6,1,5]]
b [[3,4],[0]]
c [[6,1,5],[5,1]]
d [[5,1],[6,1,5]]
end: [[6,1,5],[0]]

RC1: n=5

"""
### F16 Midterm

"""
1.
CT1: 
fed
dc
b

CT2:
3
6
5
12

CT3:
20
h
220
2200

2.
ROC1: didn't answer
correct answer: n=77

ROC2: didn't answer
correct answer: n= [3,2,1,33,22,11,333]

3. 
A. False or 1/0

B. 
s="hello"
s=[:2]
print(s)

C. drew it on the far right edge and at half the height

D. advantage: It is easily accesible and debatably more clear than placing it in a list of tuples.
disadvantage: It wasts space reassigning the variable everytime. 

E. 
def mousePressed(event,data):
    drawCircle(canvas,data)

4.
def nthZeddish(n):
    found=0
    guess=0
    while found<= n:
        guess+=1
        if isZeddish(guess):
            found+=1
    return guess
    
def isZeddish(n):
    if n<0: return False
    if n%10 == 0: return False
    if 0 in list[n]==-1: return False
    if n%10 ==0: return False
    m=[]
    for i in list[n]:
        if i!=0:
            m+=[i]
    if n%int(m)!=0:
        return False
    else: return True

5.

def init(data):
    data.score=0
    data.margin=20
    data.blueHit=True
    isHit(data)
    data.redSpeed=10
    data.blueSpeed=10

def timerFired(data):
    data.redY+=d.redSpeed
    if data.redY>=data.height:
        data.redY=0
    if data.blueHit==True:
        data.blueX+=10
    else: data.blueX-=10
    if data.blueX>=data.width and data.blueHit==True:
        data.blueHit=False
    else: data.blueHit=True
    
def redrawAll(canvas,data):
    drawRedCirc(canvas,data)
    drawBlueCirc(canvas,data)
    canvas.create_text(data.width-data.margin, data.height-data.margin, text= data.score)
    
def drawRedCirc(canvas,data):
    data.redRad=5
    data.redY=0
    data.redX=data.width/2
    canvas.create_oval(data.redX-data.redRad, data.redY, data.redX+data.redRad*2, data.redRad*2+data.redY, fill="red")
    
def drawBlueCirc(canvas,data):
    data.blueRad=10
    data.blueY=data.height/2
    data.blueX=0
    canvas.create_oval(data.blueX,data.blueY-data.blueRad, data.blueX+2*data.blueRad, data.blueY+data.blueRad*2, fill="blue")
    
def isHit(data):
    if distance(data.blueX, data.blueY, data.redX, data.redY) <= data.blueRad+data.redRad:
        data.score+=1
        data.blueX, data.blueY=0,data.height/2
        data.redX, data.redY=data.width/2, 0

def distance(x1,y1,x2,y2):
    return((x1-x2)**2+(y1-y2)**2)**0.5

def keyPressed(event,data):
    if event.keysym== "Up" or event.keysym== "Right":
        data.redSpeed+=5
    if (event.keysym=="Down" or event.keysym== "Left") and data.speed>0:
        d.redSpeed-=5
        
def mousePressed(event,data):
    if distance(event.x, event.y, data.blueX, data.blueY) <= data.blueRad:
        data.score+=1
    else: data.score-=1
    
6.

def gpc(rows,cols):
    findList=[]
    for row in range(rows):
        for col in range(cols):
            if col== cols: break
            else: finalList+=(row,col)
        findList+=(row,cols)
    for col in range(cols,0,-1):
        finalList+=(rows,col)
    for col in range(cols,1,-1):
        finalList+=(0,col)
    return finalList

def rp(L,n):
    rows,cols=len(L),len(L[0])
    listRC=gpc(rows,cols)
    secondHalf=listRC[:(len(listRC)-n)%len(listRC)]
    firstHalf= [(len(listRC)-n)%len(listRC):]
    newList=[]
    for i in firstHalf:
        newList.append(i)
    for j in secondHalf:
        newList.append(j)
    for pairs in newList:
        r,c=pairs
    count=0
    finalL=[]
    rowL=[]
    for k in range(len(newList)):
        for row in range(rows):
            rowL.append(L[r][c])
        finalL.append(rowL)
        rowL=[]
    return rowL
"""
    



#Random Number Grid

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.rows= 5
    data.cols=10
    data.rowHeight= data.height/data.rows
    data.colWidth= data.width/data.cols
    data.circles=make2dList(data.rows,data.cols,False)
    getBoardNums(data)

def mousePressed(event, data):
    if inBounds(event.x,event.y,data)==True:
        data.circles=make2dList(data.rows,data.cols,False)
    
def timerFired(data):
    pass
    
def make2dList(rows,cols,n):
    list=[]
    for row in range(rows):
        list.append([n]*cols)
    return list

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 +(y1-y2)**2)**0.5 

def inBounds(x,y,data):
    row= int(x//data.colWidth)
    col= int(y//data.rowHeight)
    cX= int(row*data.colWidth+ data.colWidth/2)
    cY= int(col*data.rowHeight+ data.rowHeight/2)
    if distance(x,y, cX, cY) <= min(data.colWidth, data.rowHeight)/2:
        return True
    
def getBoardNums(data):
    data.boardNums= make2dList(data.rows,data.cols,0)
    for row in range(data.rows):
        for col in range(data.cols):
            data.boardNums[row][col]= random.randint(0,9)

def addCircles(data):
    for row in range(data.rows):
        for col in range(data.cols):
            if data.boardNums[row][col]== data.digitPressed:
                data.circles[row][col]= True

def getCellBounds(row, col,data):
    x0= col*data.colWidth
    x1=(col+1)*data.colWidth
    y0= row*data.rowHeight
    y1=(row+1)*data.rowHeight
    return x0,x1,y0,y1
    
def drawGrid(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            x0,x1,y0,y1= getCellBounds(row,col,data)
            canvas.create_rectangle(x0, y0, x1,y1)
            if data.circles[row][col]==True:
                canvas.create_oval(x0,y0,x1,y1, fill="yellow")
            (canvas.create_text((x0+x1)/2, (y0+y1)/2, 
                text=data.boardNums[row][col]))

def keyPressed(event,data):
    if event.keysym in string.digits:
        data.digitPressed= int(event.keysym)
        addCircles(data)

def redrawAll(canvas,data):
    drawGrid(canvas,data)
        


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


### 5. selected exercises frm W1-5


def nearestBusStop(street):
    if street%8 <= 4:
        return street-(street%8)
    else:
        return street+8-(street%8)

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2== 0:
        return False
    maxFactor= roundHalfUp(n**0.5)
    for i in range(3, maxFactor+1,2):
        if n%i == 0:
            return False
    return True

def isCircularPrime(n):
    lenN= len(str(n))
    for i in range(lenN):
        if isPrime(n)==False:
            return False
        n= n%(10**(lenN-1))*(10**(lenN-1)) + (n//(10**(lenN-1)))
    return True

def nthCircularPrime(n):
    found=0
    guess=0
    while found<=n:
        guess+=1
        if isCircularPrime(guess):
            found+=1
    return guess

def replace(s1,s2,s3):
    currS=""
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                currS+= s1[i]
            if currS==s2:
                s1= s1[:i-j]+s3+s1[(i-j+len(s2)):]
                currS=""
    return s1
    
def join(L, delimiter):
    newS=""
    L=str(L)
    for i in L.split(delimiter):
        for j in i:
            if j== " ":
                newS+= delimiter
            if j.isalpha() ==True:
                newS+=j
    return newS

def map(f,a):
    newL=[]
    for i in a:
        newL.append(f(i))
    return newL
    
def nQueensChecker(a):
    rows,cols= len(a),len(a)
    colList=[]
    for row in range(rows):
        if a[row].count(True)>1:
            return False
    for col in range(cols):
        for row in range(rows):
            colList.append(a[row][col])
        if colList.count(True)>1:
            return False
        else: colList=[]
    return True


### TEST FCNS

def testNearestBusStop():
    print("testing nearestBusStop()")
    assert(nearestBusStop(3)== 0)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13)==16)
    print("passed")

def testnthCircularPrime():
    print("testing nthCircPrime")
    assert(nthCircularPrime(6)==17)
    assert(nthCircularPrime(9)==71)
    assert(nthCircularPrime(0) ==2)
    print("passed")

def testIsCircPrime():
    print("testing isCircPrime")
    assert(isCircularPrime(13)== True)
    assert(isCircularPrime(113)== True)
    assert(isCircularPrime(129) == False)
    print("passed")

def testIsPrime():
    print("testing isPrime")
    assert(isPrime(15) == False)
    assert(isPrime(25)== False)
    assert(isPrime(3) == True)
    print("passed")

def testReplace():
    print("testing replace")
    assert(replace("baab","a","3") == "b33b")
    assert(replace("hihello","h","b")== "bibello")
    assert(replace("heheheee","he","no") == "nononoee")
    print("passed")

def testJoin():
    print("testing join")
    assert(join(["ab", "cd", "efg"], ",") =="ab,cd,efg")
    assert(join(["abc", "cdc", "efgc"], ",") =="abc,cdc,efgc")
    assert(join(["adsb", "cdsd", "efdsg"], ",") =="adsb,cdsd,efdsg")
    print("passed")
    
def testMap():
    print("tesing map")
    def plus3(x):
        return x+3
    def times2(x):
        return x*2
    assert(map(plus3,[2,4,7]) ==[5,7,10])
    assert(map(times2,[2,4,7]) ==[4,8,14])
    assert(map(plus3,[1,2,0]) ==[4,5,3])
    print("passed")
    
def testnQueensChecker():
    print("testing queensChecker")
    assert(nQueensChecker(
    [[True, False],
    [False,True]]) == True)
    assert(nQueensChecker(
    [[True, True, False],
    [False,False,True],
    [True, True,True]]) == False)
    assert(nQueensChecker(
    [[True, False,False],
    [False,True,False],
    [False,False,True]]) == True)
    print("passed")
    
    
#testnQueensChecker()
#testMap()
#testJoin()
#testReplace()    
# testIsCircPrime()    
# testIsPrime()
# testnthCircularPrime()
#testNearestBusStop()

    
