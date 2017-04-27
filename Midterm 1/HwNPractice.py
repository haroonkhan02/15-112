import math
import string


### Week 3 Practice

def wordWrap(text,width):
    count=0
    text.strip()
    result=""
    for i in text:
        result+= i
        count+=1
        print(count)
        if count== width:
            result+= "\n"
            count=0
    result.replace(" ", "-")
    result.strip()
    print(result)
    return result
    
### Test fcns

def testWordWrap():
    print("Testing wordWrap()...", end="")
    assert(wordWrap("abcdefghij", 4) == """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg", 4) == """\
a*b
c*de
fg""")
    print("Passed!")

#testWordWrap()
# 
# 
# def wordSearch(board,word):
#     rows,cols=len(board), len(board[0]
#     for row in range(rows):
#         for col in range(cols):
#             result= WSfromCell(board,word,row,col)
#             if result != False:
#                 return result
#             else: return False
# 
# def WSfromCell(board,word,row,col):
#     for dir in range(8):
#         result= checkDirections(board,word,row,col,dir)
#         if result != False:
#             return result
#         else: return False
#     
# def checkDirections(board,word,startRow,startCol,dir):
#     rows,cols=len(board), len(board[0])
#     dirs= [[(-1,-1), (-1,0), (-1,1)],
#             [(0,-1),         (0,1)],
#             [(1,-1), (1,0), (1,1)]]
#     drow,dcol= dirs[dir]
#     for i in range(len(word)):
#         row= startRow+i*drow
#         col= startCol+i*dcol
#         if row<0 or row>=data.rows or col<0 or col>= data.cols or board[row][col]!=word[i]:
#             return False
#     else: return (word, (row,col))




# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    pass

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
    
    
    
    
    
    