#################################################
# Hw1
#Sydney Howard (showard)
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
# Hw1 problems
#################################################

def fabricYards(inches):
    yards = inches / 36
    return math.ceil(yards)

def fabricExcess(inches):
    excess = fabricYards(inches)*36 - inches
    return excess

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
def isRightTriangle(x1, y1, x2, y2, x3, y3):
    a = distance(x1,y1,x2,y2)
    b = distance(x2,y2,x3,y3)
    c = distance(x1,y1,x3,y3)
    hypot = max(a,b,c)
    side1 = min(a,b,c)
    side2 = a+b+c-hypot-side1
    if almostEqual(math.sqrt(side1**2 + side2**2), hypot):
        return True
    else:
        return False

def colorBlender(rgb1, rgb2, midpoints, n):
    red1= rgb1//10**6
    red2= rgb2//10**6
    reddif = (red2 - red1) / (midpoints+1)
    red= roundHalfUp(red1+(reddif*n))
    green1= rgb1//10**3
    green1= green1%10**3
    green2= rgb2//10**3
    green2= green2%10**3
    greendif= (green2 - green1)/ (midpoints+1)
    green= roundHalfUp(green1+(greendif*n))
    blue1= rgb1%10**3
    blue2= rgb2%10**3
    bluedif= (blue2 - blue1)/ (midpoints+1)
    blue= roundHalfUp(blue1+(bluedif*n))
    if n>=0 and n<=midpoints+1:
        return ((red*10**6+(green)*10**3+blue))
    else:
        return None
    
    

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Hw1 Test Functions
#################################################

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def testAll():
    testFabricYards()
    testFabricExcess()
    testIsRightTriangle()
    testColorBlender()
    testBonusFindIntRootsOfCubic()

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
