#Hw8
#Sydney Howard, showard

import string
import math


### Fall15 Quiz 6

"""
CT1:
[12, 12]
[5, [12]]

CT2:
46 16 26 43
26

RC1:
L= [0,3,2,1]

RC2:
L= [[4,3,2],
    [7,6,5]]
 
3A. board[row][col]!= word[i]

3B. wordSearch(board, winningWord)

3C. board[row][col]=player
"""

#4.
def medians(L):
    rows=len[L]
    if rows<2 or L==[]: return None
    finalList=[]
    for row in range(rows):
        rowList=sorted(L[row])
        for i in range(len(rowList)):
            if len(rowList)%2==1:
                middleIndex= rowList//2
                median= rowList[middleIndex]
                finalList.append(median)
            else: 
                middleIndex=rowList/2
                median=(rowList[middleIndex]+ rowList[middleIndex+1])/2
                finalList.append(median)
    finalList.sort()
    finalList.reverse()
    return finalList
    
    
###s16 Midterm1

"""
CT1:
[['2:54', 4],
 ['3:443', 5], 
 ['1:4', 3]]
 
CT2: 
a [[1], [4, 6], 0] 
b [5, [4, 6], 7] 
c [[1], [2, 3]]
[[1], [4, 6]]

RC1:
n= 96786543

RC2: 
L= [[2,2,4,4],[5,5],[]]

Short answer:
C. It must loop through every letter in the string.

D.
def redrawAll(canvas,data):
    if event.keysym=="Up":
        drawCircle(canvas,data)
        
E. False or 1/0
"""

def isPowerish(n):
    if n<0: return False
    x= len(str(n-4))
    m=10**x
    if n>=m-2 and n<=m+2:
        return True
        
def nthPowerish(n):
    found=0
    guess=0
    while found<=n:
        guess+=1
        if isPowerish(guess):
            found+=1
    return guess


#http://www.cs.cmu.edu/~112/notes/events-example0.py
# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.timerDelay=1000
    data.margin=20
    data.score=0
    data.CW=True
    data.gameOver=False
    data.timeLeft=3000
    data.moveX=0
    data.moveY=0
    data.blueRad= data.width/4
    data.redRad= 10

def mousePressed(event, data):
    if distance(event.x,event.y,data.redCX, data.redCY) <= data.redRad:
        data.score+=1
        if data.CW==True:
            data.CW=False
        else:
            data.CW= True

def keyPressed(event, data):
    if event.keysym=="Up":
        data.redRad+=1
        if data.redRad==20:
            data.gameOver=True

def timerFired(data):
    if data.timeLeft>=1000:
        data.timeLeft-= data.timerDelay
    else:
        data.timeLeft=3000
    if data.CW==True:
        if data.timeLeft==2000:
            data.moveX+=data.blueRad
            data.moveY+=data.blueRad+(data.blueRad/2)
        if data.timeLeft==1000:
            data.moveX-=data.blueRad*2
        if data.timeLeft==0:
            data.moveX=0
            data.moveY=0
    elif data.CW==False:
        if data.timeLeft==2000:
            data.moveX-=data.blueRad
            data.moveY+=data.blueRad+(data.blueRad/2)
        if data.timeLeft==1000:
            data.moveX+=data.blueRad*2
        if data.timeLeft==0:
            data.moveX=0
            data.moveY=0

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def drawBlueCirc(canvas,data):
    canvas.create_oval(data.width/2-data.blueRad, data.height/2-data.blueRad, data.width/2+data.blueRad, data.height/2+data.blueRad, fill="blue")
    
def drawRedCirc(canvas,data):
    x0=data.width/2-data.redRad+data.moveX
    y0=data.height/2-(data.blueRad+2*data.redRad)+data.moveY
    x1=data.width/2+data.redRad+data.moveX
    y1=data.height/2-data.blueRad+ data.moveY
    data.redCX= (x0+x1)/2
    data.redCY= (y0+y1)/2
    canvas.create_oval(x0,y0,x1,y1, fill="red")

def redrawAll(canvas, data):
    if data.gameOver==False:
        drawBlueCirc(canvas,data)
        drawRedCirc(canvas,data)
        canvas.create_text(data.margin, data.height-data.margin, text=data.score)
    if data.gameOver==True:
        canvas.create_text(data.width/2, data.height/2, text= "Game Over")

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

def circleAroundCircle():
    run(400,400)
    
#circleAroundCircle()
