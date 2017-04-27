#################################################
# Lab4
#Sydney Howard, showard, E
#Lab Partners: Max Perry (maperry), Jenn Choi (jaeeunc1)
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

def lookAndSay(a):
    result=[]
    for digit in a:
        if result== [] or digit!= result[-1][1]:   #checks if consecutive 
            result.append((1, digit))              #digits are the same
        else: 
            count,digit= result.pop()
            result.append((count+1, digit))      #counts the consecutive digits
    return result

def inverseLookAndSay(a):
    result=[]
    for i in a:
        count= i[0]                         #number of digits we want to print
        digit= i[1]                         #digit we want to print
        for j in range(count):
            result.append(digit)
    return result

def solvesCryptarithm(puzzle, solution):
    num1=""
    num2=""
    result=0
    resultPuzzle=0
    total=0
    puzzle= puzzle.split("=")              #split puzzle at =
    for i in puzzle[0].split("+"):         #split lists at +'s
            for j in i:
                if int(solution.find(j))==-1:   #check if sol'n has all letters
                    return False                #in puzzle
                num1+= str(solution.find(j))    #convert letters to numbers
            result+= int(num1)
            num1=""
    for k in puzzle[1]:
        if int(solution.find(k))==-1:
            return False
        num2+= str(solution.find(k))
    if int(result)==int(num2):
        return True
    else: return False

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def getStats(canvas,text,width,height):       #count number of consononats,
    text=text.replace(" ", "")                #vowels, other and total
    text=text.lower()
    vowels=0
    consonants=0
    other=0
    for i in text:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vowels+=1
        else:
            if i.isalpha():
                consonants+=1
            else:
                other+=1
    total= vowels+consonants+other
    if total==0:
        total=1
    return vowels, consonants, other, total

def getDeg(letter,total):               #converts to degrees
    degOfCircle=360
    return letter/total*degOfCircle

def getRad(letter,total):               #converts to radians
    radOfCircle=2*math.pi
    return letter/total*radOfCircle

def getCoord(width,height,vowel,total):      #finds coordinates for text
    radius= min(width,height)/3
    cX= width/2
    cY= height/2
    theta= getRad(vowel,total)/2
    x= cX-(radius/2*math.cos(theta/2))
    y= cY-(radius/2*math.sin(theta/2))
    return x, y

def getCoord1(width,height,vowel,total):      #finds coordinates for text
    radius= min(width,height)/3
    cX= width/2
    cY= height/2
    theta= getRad(vowel,total)/2 + (math.pi/2)
    x= cX-(radius/2*math.cos(theta/2))
    y= cY-(radius/2*math.sin(theta/2))
    return x, y
    
def getCoord2(width,height,vowel,consonants,total):     
    radius= min(width,height)/3
    cX= width/2
    cY= height/2
    theta= getRad(vowel,total) + getRad(consonants,total)/2 + (math.pi/2)
    x= cX-(radius/2*math.cos(theta/2))
    y= cY-(radius/2*math.sin(theta/2))
    return x, y
    
def getCoord3(width,height,vowel,consonants,other,total):      
    radius= min(width,height)/3
    cX= width/2
    cY= height/2
    theta= getRad(vowel,total) + getRad(consonants,total)+getRad(other,total)/2
    + (math.pi/2)
    x= cX-(radius/2*math.cos(theta/2))
    y= cY-(radius/2*math.sin(theta/2))
    return x, y

def drawPieChart(canvas,text,width,height):
    cX= width/2
    cY= height/2
    vowels, consonants, other,total= getStats(canvas,text,width,height)
    print(vowels,consonants,other,total)
    if vowels==0 and consonants==0 and other==0: #if there's an empty string
        return canvas.create_text(cX, cY, text="No data to display",
            font="Arial 20 bold")
    if vowels!=0:                               #displays vowel arc and text
        canvas.create_arc(0,0, width,height,start=90,
        extent=getDeg(vowels,total), fill='pink')
        x,y= getCoord1(width,height,vowels,total)
        canvas.create_text(x,y,text="vowels ("+str(vowels)+" of "+str(total)
        +", "+str(int(vowels/total*100))+"%)",font= "Arial 12 bold")
    if consonants!=0:                          #displays consonant arc and text
        canvas.create_arc(0,0, width, height, start=90+getDeg(vowels,total),
            extent=getDeg(consonants,total), fill='cyan')
        a,b= getCoord2(width,height,consonants,vowels,total)
        canvas.create_text(a,b,text="consonants ("+str(consonants)+" of "
            +str(total)+", "+str(int(consonants/total*100))+"%)", 
            font= "Arial 12 bold") 
    if other!=0:                            #displays other arc and text
        canvas.create_arc(0,0, width, height, start=90+
            getDeg(vowels,total)+getDeg(consonants,total),extent=
            getDeg(other,total),fill='lightGreen')       
        c,d= getCoord3(width,height,vowels,consonants,other,total)
        canvas.create_text(c,d,text="other ("+str(other)+" of "+
            str(total)+", "+str(int(other/total*100))+"%)", 
            font= "Arial 12 bold") 
    if consonants!=0 and vowels==0 and other==0: #if only consonants present
        canvas.create_arc(0,0, width, height, fill='cyan')
        x,y= getCoord(width,height,consonants,total)
        canvas.create_text(x,y,text="consonants ("+str(consonants)+" of "
            +str(total)+", "+str(int(consonants/total*100))+"%)", 
            font= "Arial 12 bold") 
    if other!=0 and consonants==0 and other==0: #if only other present
        canvas.create_arc(0,0, width, height,fill='lightGreen')       
        x,y= getCoord(width,height,other,total)
        canvas.create_text(x,y,text="other ("+str(other)+" of "
        +str(total)+", "+str(int(other/total*100))+"%)", font= "Arial 12 bold")
    if vowels!=0 and consonants==0 and other==0:   #if only vowels present
        canvas.create_oval(0,0, width,height, fill='pink')
        x,y= getCoord(width,height,vowels,total)
        canvas.create_text(x,y,text="vowels ("+str(vowels)+" of "+str(total)
        +", "+str(int(vowels/total*100))+"%)",font= "Arial 12 bold")
        
        
def makeLetterTypePieChart(text, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    drawPieChart(canvas,text, width=winWidth,height=winHeight)
    root.mainloop()

def testMakeLetterTypePieChart():
    print("Testing makeLetterTypePieChart()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    makeLetterTypePieChart("AB, c de!?!")
    makeLetterTypePieChart("AB e")
    makeLetterTypePieChart("A")
    makeLetterTypePieChart("               ")
    print("Done!")

#################################################
# Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolvesCryptarithm()
    testMakeLetterTypePieChart()

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
