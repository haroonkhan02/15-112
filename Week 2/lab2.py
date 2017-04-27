#################################################
# Lab2
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

def lengthOfNum(n):
    count=0
    while (n>0):
        n=n//10
        count +=1
    return count

def isRotation(x, y):
    length= lengthOfNum(x)
    if x==y:
        return True
    elif x>=10:
        for a in range(1, length):
            first= x//(10**a)
            second= x%(10**a)
            if second*(10**(length-a)) +first == y:
                return True
            else:
                continue
        return False
    else:
        return False

def isPrime(n):
    if n<2:
        return False 
    for a in range(2,n):
        if n%a==0:
            return False
    return True
    
#(Modified isPrime from http://www.cs.cmu.edu/~112/notes/notes-loops.html)

def reverseNum(n):
    total=0
    length=lengthOfNum(n)
    for a in range(0, length):
        total+=(n//(10**a)%10)*(10**(length-(1+a)))
    return total

def nthEmirpsPrime(n):
    found=-1
    guess=11
    while (found<n):
        guess += 1
        if ((isPrime(guess)==True 
        and isPrime(reverseNum(guess))==True) 
        and (guess != reverseNum(guess))):
            found +=1
    return guess
    
#(Modified nthPrime from http://www.cs.cmu.edu/~112/notes/notes-loops.html)

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

def isWithProperty309(n):
    check=0
    count=0
    n=n**5
    temp=n
    while n>0:
        if check!=((n)%10):
            n//=10
        elif check == (n)%10:
            count+=1
            n=temp
            check += 1
            if count > 9:
                return True
    return False


def nthWithProperty309(n):
    found=-1
    guess=0
    while (found<n):
        guess +=1
        if isWithProperty309(guess)==True:
            found+=1
    return guess

#(Modified nthPrime from http://www.cs.cmu.edu/~112/notes/notes-loops.html)
    

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed.')

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()... ', end='')
    assert(nthEmirpsPrime(0) == 13)
    assert(nthEmirpsPrime(5) == 73)
    assert(nthEmirpsPrime(10) == 149)
    assert(nthEmirpsPrime(20) == 701)
    assert(nthEmirpsPrime(30) == 941)
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(5) == 635)
    assert(nthWithProperty309(6) == 662)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testIsRotation()
    testNthEmirpsPrime()
    testCarrylessAdd()
    testNthWithProperty309()

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
        #'range,reversed,'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
