#################################################
# Hw3
#Sydney Howard, showard, E
#################################################

import cs112_s17_linter
import math, string

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
# Autograded Exercises
#################################################

def patternedMessage(msg, pattern):
    newPattern=""
    msg=msg.replace(" ", "")
    count=0                                        #the ith letter of msg
    if pattern== "":
        return ""
    for j in range(len(pattern)):
        if pattern[j]==" ":                        #preserving spaces        
            newPattern+= " "
        elif pattern[j]== "\n":                    #preserving new lines
            newPattern += "\n"
        elif pattern[j].isspace()==False:          #input letters from msg
            newPattern+= msg[count%(len(msg))]
            count+=1
    newPattern= newPattern.strip()
    return newPattern

def bestStudentAndAvg(gradebook):
    currName=""
    bestName=""
    gradesAdded= 0
    numOfGrades=0
    currAveGrade=0
    bestAveGrade=-10000000000        #a number that most likely won't be a grade
    isNeg = 1
    for student in gradebook.splitlines():
        for a in student.split(","):
            if a.isalpha():                     #saves the name of the person
                currName= a
            if len(a) >= 1 and a[0] == "-":     #tests for negative numbers
                a = a[1:]
                isNeg = -1
            if a.isdigit():                     #adds the grades
                gradesAdded+= int(a)* isNeg
                numOfGrades+=1
                isNeg=1
                currAveGrade= roundHalfUp(gradesAdded/numOfGrades)
        if currAveGrade> bestAveGrade:
            bestAveGrade=currAveGrade
            bestName=currName
            currName= ""
        currAveGrade=0                  #reset the grades for the next person
        gradesAdded=0
        numOfGrades=0
    return bestName + ":" + str(bestAveGrade) 

###### BONUS #######

def topLevelFunctionNames(code): return 42
def getEvalSteps(expr): return 42
def bonusEncode1(msg): return 42
def bonusDecode1(msg): return 42
def bonusEncode2(msg): return 42
def bonusDecode2(msg): return 42
def bonusEncode3(msg): return 42
def bonusDecode3(msg): return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# playPig (be sure this is below the # ignore_rest line!
#################################################

import random

def invalidInput(player1):                  #function is called when the player 
    print("Invalid input.")                 #doesn't input an r or h
    if player1==True:
        playerInput= input("'r' is roll. 'h' is hold.\nPlayer 1 Turn:")
    elif player1==False:
        playerInput= input("'r' is roll. 'h' is hold.\nPlayer 2 Turn:")
    return playerInput

def playPig():
    p1Score,p2Score, playerScore, randomRoll, player1=0,0,0,0, True
    print("Welcome to PlayPig!")
    playerInput= input("'r' is roll. 'h' is hold.\nPlayer 1 Turn:")
    while True:
        if (playerInput != "r") and (playerInput != "h"):
            playerInput= invalidInput(player1)
        if playerInput == "h":
            if player1==True:               #player 1 turn
                p1Score+=playerScore
                print("Player 1 Score:", p1Score)
                if p1Score>=100:
                    print ("Congrats Player 1! You won! Try again, Player 2.")
                    return
                playerInput= input("Player 2 Turn:")
            elif player1==False:           #player 2 turn
                p2Score+=playerScore
                print("Player 2 Score:", p2Score)
                if p2Score>=100:
                    print ("Congrats Player 2! You won! Try again, Player 1.")
                    return
                playerInput= input("Player 1 Turn:")
            player1=not player1
            playerScore=0                  #resets the player score for round
        elif playerInput == "r":   
            randomRoll= random.randint(1,6)
            if randomRoll==1:
                playerScore=0
                if player1==True:          #player 1 turn
                    print("You rolled a 1.\nPlayer 1 Score:", p1Score)
                    playerInput= (input("Player 2 Turn:"))
                elif player1==False:       #player 2 turn
                    print("You rolled a 1.\nPlayer 2 Score:", p2Score)
                    playerInput= (input("Player 1 Turn:"))
                player1=not player1
            elif randomRoll !=1:
                playerScore+=randomRoll
                print("You Rolled a:", randomRoll)
                playerInput= input("Roll Agian.\nTurn:")

#######################################
def testInvalidInput():
    assert((invalidInput("True")) ==  playerInput)
    assert((invalidInput("False")) ==  playerInput)
    print("Passed!")


#################################################
# Test Functions
#################################################

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        msg,pattern = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        #observed = patternedMessage(msg, pattern).strip("\n")
        #print "\n\n***********************\n\n"
        #print msg, pattern
        #print "<"+patternedMessage(msg, pattern)+">"
        #print "<"+soln+">"
        assert(observed == soln)
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")

def testBonusTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

import random

def testBonusDecode(testFn, encodeFn, decodeFn):
    print("Testing " + testFn + "...", end="")
    s1 = ""
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(" \n\n") + random.choice(string.digits)
    for s in ["a", "abc", s1]:
        assert(decodeFn(encodeFn(s)) == s)
    print("Passed!")

def testBonusDecode1():
    testBonusDecode("testBonusDecode1", bonusEncode1, bonusDecode1)

def testBonusDecode2():
    testBonusDecode("testBonusDecode2", bonusEncode2, bonusDecode2)

def testBonusDecode3():
    testBonusDecode("testBonusDecode3", bonusEncode3, bonusDecode3)

#################################################
# testAll and main
#################################################

def testAll():
    testPatternedMessage()
    testBestStudentAndAvg()
    testBonusTopLevelFunctionNames()
    testBonusGetEvalSteps()
    testBonusDecode1()
    testBonusDecode2()
    testBonusDecode3()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,repr,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
