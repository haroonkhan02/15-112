#################################################
# Hw2
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

def isKap(n):
    n=n**2
    count=0
    if n<0:
        return False
    while 10**count <=10*n:
        firstHalf= n%(10**(1+count))
        secondHalf= n//(10**(1+count))
        count+=1
        if firstHalf!=0 and firstHalf + secondHalf == int(math.sqrt(n)):
            return True
    return False
    
def nthKaprekarNumber(n):
    found=0
    guess=0
    while found <=n:
        guess+=1
        if isKap(guess):
            found+=1
    return guess

def integral(f, a, b, N):
    totalArea=0
    width= (b-a)/N
    for NofRect in range(0,N):
        x1=a+ ((NofRect)*width)
        x2= x1+width
        h1= f(x1)
        h2= f(x2)
        totalArea+= (h1+h2)/2*width
    return (totalArea)


def nearestKaprekarNumber(n):
    a=n
    n=math.floor(n)
    guess1=0
    guess2=0
    if n<=0:
        return 1
    if isKap(n) == True:
        return n
    while True:
        if isKap(n+guess1)==True:
            x1= n+guess1
            break
        guess1+=1
    
    while True:
        if isKap(n+guess2) ==True:
            x2= n+guess2
            break
        guess2-=1
    if (a%1>0.5)and((guess1)-abs(guess2))<=1 and((guess1)-(abs(guess2))>0):
        return x1
    elif (a%1<=0.5) and a%1!=0 and ((guess1)==abs(guess2)):
        return x1
    elif guess1 < abs(guess2):
        return x1
    elif guess1 > abs(guess2):
        return x2
    elif guess1== abs(guess2):
        return x2
    
    
def carrylessAdd(x1, x2):
    count=0
    total=0
    if x1==0 or x2==0:
        return x1+x2
    while (x1>0 or x2>0):
        a=((x1%10) + (x2%10)) %10
        total= a*(10**count)+total
        count+=1
        x1//=10
        x2//=10
    return total

def carrylessMultiply(x1, x2):
    count1=0
    total1=0
    count2=0
    finaltotal=0
    temp=x1
    while x2>0:
        while x1>0:
            a1=x1%10
            b1=x2%10
            total1 = (((a1*b1)%10)*(10**count1)) + total1
            x1//=10
            count1 +=1
        total1=total1*(10**count2)
        finaltotal=carrylessAdd(total1,finaltotal)
        total1=0
        x2//=10
        count2+=1
        count1=0
        x1=temp
    return finaltotal

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

#(Taken from http://www.cs.cmu.edu/~112/notes/notes-loops.html)
    
def digitAdd(n):
    total=0
    count=0
    while n>0:
        digit=n%10
        total+= digit
        n//=10
    return total

def isSmith(n):
    totalAdd=0
    count=2
    temp=n
    if n<=3 or isPrime(n)==True:
        return False
    while n>1:
        while n%count==0 and isPrime(count)==True:
            n=n//count
            totalAdd+= digitAdd(count)
            count+=1
            if count >=n:
                count=2
        if totalAdd==digitAdd(temp) and n==1:
            return True
        elif count >=n:
            count=2
        else:
            count+=1
    return False


def nthSmithNumber(n):
    found=-1
    guess=0
    while found<n:
        guess +=1
        if isSmith(guess) ==True:
            found +=1
    return guess
    
    
##### Bonus #####

def play112(game):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    #kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    #bigKaps = [994708, 999999]
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testNthKaprekarNumber()
    testIntegral()
    testNearestKaprekarNumber()
    testCarrylessMultiply()
    testNthSmithNumber()
    #testBonusPlay112()

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
        #'range,reversed,str,' # added 'str' for play112 bonus
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
