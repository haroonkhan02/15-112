
import math
import string

### Quiz 2

# def isND(n):
#     if n<10 and n%2==1:
#         return True
#     n= str(n)
#     for i in range(len(str(n)),0,-1):
#         if n[i]%2==0: return False
#         else:
#             if n[i]<= n[i-1]:
#                 return False
#     return True
#     
# def nthND(n):
#     found=-1
#     guess=0
#     while found<n:
#         guess+=1
#         if isND(guess)==True:
#             found+=1
#     return guess
# 
# def testNthND():
#     print("testing nthND")
#     assert(nthND(0) ==1)
#     assert(nthND(9) == 71)
#     assert(nthND(13) == 93)
#     print("Passed")
# 
# # testNthND()
# 
# def h(f,x):
#     return f(x)
# 
# def latticePointCount(f,x1,x2):
#     x1=math.ceil(x1)
#     x2= math.floor(x2)
#     count=0
#     if i in range(x1, x2+1):
#         if isinstance(h(f,i),int) == True:
#             if h(f,i) >=x1 or h(f,i) <= x2:
#                 count+=1
    # return count
    # 
# grid-demo.py

# ### Quiz 3
# 
# def encode(s,pwd):
#     newS= ""
#     count= len(s)

#### Quiz 6

# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.lines=[]
    data.undo=[]
    data.animating=False
    data.xFinal=0
    data.text= "hello"
    

def mousePressed(event, data):
    if data.animating==False:
        data.lines.append(event.y)
        data.undo=[]
        if data.xFinal>=data.width:
            data.xFinal=0
    if data.animating==True:
        data.text="ignored mousePress"

def keyPressed(event, data):
    if data.animating==True: 
        if event.keysym=="u":
            data.text= "ignored undo"
        if event.keysym=="r":
            data.text="ignored redo"
    if data.animating==False:
        if event.keysym=="u":
            if len(data.lines)>0:
                data.undo.append(data.lines.pop())
        if event.keysym=="r":
            if len(data.undo)>0:
                data.lines.append(data.undo.pop())

def timerFired(data):
    data.xFinal+=20


def drawText(canvas,data):
    canvas.create_text(data.width/2,data.height-30, text=data.text)

def redrawAll(canvas, data):
    if len(data.lines)>0:
        data.drawingLine= data.lines[-1]
        data.drawnLines= data.lines[:-1]
        for line in range(len(data.drawnLines)):
            canvas.create_line(0,data.drawnLines[line],data.width, data.drawnLines[line])
            canvas.create_text(data.width/2, data.drawnLines[line], text=str(line+1))
        canvas.create_line(0,data.drawingLine,data.xFinal,data.drawingLine)
        canvas.create_text(data.width/2, data.drawingLine, text= len(data.lines))
    drawText(canvas,data)

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

def animatedLines():
    run(400,400)

#animatedLines()
    
    
def encode(s,pwd):
    newS=""
    n= len(s)
    pwd=str(pwd)
    m= len(pwd)
    for i in range(n):
        numOffset= int(pwd[i%m])
        print(ord(s[i]))
        newS+= chr((ord(s[i])+numOffset)%26)
    return newS

def test():
    print("testing")
    assert(encode("abyzc",234) == "cecbf")
    print("passed")

test()
    
    
    
    