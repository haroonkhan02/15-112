#################################################
# Hw4
#Sydney Howard, showard
#################################################

import cs112_s17_linter
import math, string, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Problems
#################################################


def isValidWord(word,hand):         #checks if dictionary word is in hand
    a=copy.copy(hand)
    for letter in word:
        if letter in a:
            a.remove(letter)      #makes sure not to count same letter twice
        else: return False
    return True

def getWordScore(letterScores,word):    #calculates word value
    total=0
    for letter in word:
        total+= letterScores[ord(letter)-ord("a")]
    return total

def bestScrabbleScore(dictionary, letterScores, hand):
    bestScore,currScore=0,0
    currWord,bestWord="", ""
    bestList=[]
    for word in dictionary:
        if isValidWord(word,hand):
            currScore= getWordScore(letterScores,word)
            currWord=word
        if currScore > bestScore:       #documents the new bestScore
            bestScore=currScore
            bestWord= currWord
            bestList.append(bestWord)
        elif currScore==bestScore and currWord!="": #creates list for words 
            bestList.append(currWord)               #with same score
        currScore,currWord=0, ""
    if bestScore==0:return None
    if len(bestList)>1:return tuple((bestList,bestScore))
    return tuple((bestWord,bestScore))

def testIsValidWord():
    assert(isValidWord("zyx", "zyzsk") == False)
    assert(isValidWord("abc", "jkbca") == True)
    assert(isValidWord("hi", "ikli") == False)
    
def testGetWordScore():
    assert(getWordScore(([1] * 26), "zyx") == 22)
    assert(getWordScore(([1] * 26), "abc") == 7)
    assert(getWordScore(([1] * 26), "cat") == 5)


###### Autograded Bonus ########
# (place non-autograded bonus below #ignore-rest line!) #

def runSimpleProgram(program, args):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math
#keep track of the coord of turtle, angle it's facing

def getRad(n):                  #convert degrees to radians
    degOfCircle=360
    return n*2*math.pi/degOfCircle

def moveIt(canvas,winWidth,winHeight,moveNum,currDeg,currColor,currX,currY):
    finalX= currX+ moveNum*math.cos(getRad(currDeg%360)) #updates X position
    finalY= currY- moveNum*math.sin(getRad(currDeg%360)) #updates Y position
    if currColor=="none":
        return finalX, finalY
    else: canvas.create_line(currX, currY, finalX, finalY,
    fill=currColor,width=4)
    return finalX, finalY

def drawTortoise(canvas,program,winWidth,winHeight):
    currDeg,currX,currY=0,winWidth/2, winHeight/2
    canvas.create_text(10,10,text= program,font="Arial 10", fill="grey",
    anchor=NW)
    for i in program.splitlines():
        if i.startswith("#"):continue       #ignore text after "#"
        j= i.split(" ")
        if j[0] == "left":                  #rotates left
            currDeg += int(j[1])
        if j[0] == "right":                 #rotates right
            currDeg -= int(j[1])
        if j[0] == "color":                 #changes color
            currColor= str(j[1])
        if j[0] == "move":                  #moves position/draws line
            moveNum=int(j[1])
            currX, currY= moveIt(canvas,winWidth,winHeight,moveNum,
            currDeg,currColor,currX, currY)

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    drawTortoise(canvas,program,winWidth,winHeight)
    root.mainloop()
 
 
   
def testGetRad():
    assert(getRad(60)==math.pi/3)
    assert(getRad(180) == math.pi)
    assert(getRad(270) == 2*math.pi/3)

def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

#################################################
# Test Functions
#################################################

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testRunSimpleTortoiseProgram()
    testBestScrabbleScore()
    testRunSimpleProgram()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,del,is,pass,repr' +
        'as,class,except,finally,global,lambda,nonlocal,raise,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len,'+
        #'ascii,bin,dir,enumerate,format,help,hex,id,iter,'+
        #'list,oct,slice,sorted,tuple,zip,'+
        '__import__,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,' +
        'eval,exec,filter,frozenset,getattr,globals,' +
        'hasattr,hash,issubclass,' +
        'locals,map,memoryview,next,object,open,property,set,' +
        'setattr,staticmethod,super,' +
        'type,vars,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
