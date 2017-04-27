#################################################
# Lab1- Sydney Howard (showard)
# Lab Partners:
    # Max Perry (maperry)
    # Jenn Choi (jaeeunc1)
#################################################

import cs112_s17_linter
import math

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
# Lab1 problems
#################################################



def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1<x2:
        if x1+w1 >= x2:
            if y1 < y2:
                if y1+h1 >= y2:
                    return True
                else:
                    return False
            elif y2< y1:
                if y2+h2 >= y1:
                    return True
                else: 
                    return False
            else: 
                return False
        return False
    elif x2 < x1:
        if x2+w2 >= x2:
            if y2< y1:
                if y2+h2 >= y1:
                    return True
                else:
                    return False
            elif y1 < y2:
                if y1+h1 >= y2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return True
    

def isPerfectSquare(n):
    if isinstance(n,int) == True and n>=0:
        if n == (int(n**.5))**2:
            return True
        else:
            return False
    else:
        return False
    
def getKthDigit(n, k):
    n= abs(n)
    hi= n//10**k
    hi= hi%10
    return hi

def setKthDigit(n, k, d):
    if n >= 0:
        return n-getKthDigit(n,k) * 10**k + d*10**k
    else:
        return -(abs(n)-getKthDigit(n,k) * 10**k + d*10**k)

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    a= totalTime
    b= -(totalDistance)
    c= -(riverCurrent**2*totalTime)
    speed1= ((-b + (math.sqrt(b**2-4*a*c)))/(2*a))
    speed2= ((-b - (math.sqrt(b**2-4*a*c)))/(2*a))
    maxspeed= max(speed1,speed2)
    return ((totalDistance/2)/(maxspeed-riverCurrent))
    

#################################################
# Lab1 Test Functions
################################################


def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testRiverCruiseUpstreamTime():
    print('Testing riverCruiseUpstreamTime()... ', end='')
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.7888736053508778)) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.5))
    assert(almostEqual(riverCruiseUpstreamTime(4,56,2),2.2801098892805185))
    print('Passed.')

#################################################
# Lab1 Main
################################################

def testAll():
    testRectanglesOverlap()
    testIsPerfectSquare()
    testGetKthDigit()
    testSetKthDigit()
    testRiverCruiseUpstreamTime()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
