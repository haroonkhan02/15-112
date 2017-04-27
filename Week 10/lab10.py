#Lab 10
#Sydney Howard, showard
#lab group partners: kbakos, elenac

def alternatingSum(L):
    if len(L)==0:
        return 0
    else:                   
        return L[0]-alternatingSum(L[1:]) #change from plus and minus

def powerSum(n,k):
    if n<0 or k<0:
        return 0
    else:
        return n**k+ powerSum(n-1,k)        #loop thru values from n to 0
        
def powersOf3ToN(n,expt=0):
    if n < 1:
        return None
    if 3**expt > n:         #can't be less than 3
        return []
    else:
        return [3**expt] + powersOf3ToN(n,expt+1)      #only powers of 3

def zap1(L,M):
    if len(L) == 0 or len(M) == 0:      #get rid of extra numbers
        return []
    else:
        return [(L[0],M[0])] + zap1(L[1:], M[1:])   #get rid of first elem

def zap2(L,M):
    if len(L)==0 and len(M)==0:         #stop when list empty
        return []
    if len(L)== 0:           #add the rest of one list once the other is empty
        return [(None, M[0])] + zap2([], M[1:])
    elif len(M)==0:
        return [(L[0],None)] + zap2(L[1:], [])
    else:
        return [(L[0],M[0])] + zap2(L[1:], M[1:]) #get rid of first elem

def zap3(*args,result=[]):
    temp,nlist=[],[]
    if len(args) ==0:       #check for empty lists
        return []
    else:
        for i in args:
            if i!=[]:
                temp.append(i[0])       #add up first terms
                nlist.append(i[1:])     #remove first term
        if(len(temp) != 0):
            result+=[tuple(temp)]       #create result
        return result + zap3(*nlist)
        
def almostEqual(x,y):
    return x==y

class Line(object):
    def __init__(self,m,b):
        self.m=m
        self.b=b
    def __repr__(self):
        if self.m==0:
            return "y=%d" % self.b
        if self.b==0:
            if self.m==1:
                return "y=x"
            if self.m==-1:
                return "y=-x"
            else:
                return "y=%dx" % ( self.m)
        if self.b==0 and self.m==0:
            return "y=0"
        else:
            if self.b<0:
                return "y=%dx%d" % (self.m, self.b)
            if self.b<0 and self.m==1:
                return "y=x%d" %  self.b
            else:
                if self.m==1:
                    return "y=x+%d" % ( self.b)
                if self.m==-1:
                    return "y=-x+%d" % ( self.b)
                else:
                    return "y=%dx+%d" % (self.m, self.b)
    def __eq__(self,other):
        return isinstance(other,Line) and self.m ==other.m and self.b==other.b
    def __hash__(self):
        return hash((self.m, self.b))
    def getSlope(self):
        return self.m        
    def getIntercept(self):
        return self.b
    def getIntersection(self,other):
        if self.isParallelTo(other)==False:
            x= (other.getIntercept()- self.getIntercept())/\
            ((self.getSlope()-other.getSlope()))
            y= (self.getSlope()*x) + self.getIntercept()
            return (x, y)
    def isParallelTo(self,other):
        if self.getSlope()==other.getSlope():
            return True
        else:
            return False
    def getHorizontalLine(self,n):
        self.b= self.getSlope()*n + self.getIntercept()
        return Line(0,self.b)
        

### TEST FCNS

def testAltSum():
    print("testing alternatingSum()")
    assert(alternatingSum([1,2,3,4,5])==3)
    assert(alternatingSum([1,2,-1])==-2)
    assert(alternatingSum([1,2,100])==99)
    assert(alternatingSum([1, 6]) == -5)
    print("passed")

def testPwrSum():
    print("testing pwrSum()")
    assert(powerSum(3,2)== 14)
    assert(powerSum(5,3) ==225)
    assert(powerSum(-3,8)== 0)
    print("passed")

def testPwrsOf3():
    print("testing pwrsof3toN")
    assert(powersOf3ToN(10.5) == [1,3,9])
    assert(powersOf3ToN(12) == [1,3,9])
    assert(powersOf3ToN(35) == [1,3,9,27])
    assert(powersOf3ToN(-43) ==None)
    print("passed")

def testZap1():
    print("testing zap1")
    assert(zap1([1,2],[3,4,5]) == [(1,3), (2,4)])
    assert(zap1([1,2,3],[4,5]) == [(1,4), (2,5)])
    assert(zap1([1,2,3,4,5],[4,5]) == [(1,4), (2,5)])
    print("passed")

def testZap2():
    print("testing zap2")
    assert(zap2([1,2],[3,4,5]) == [(1,3), (2,4), (None, 5)])
    assert(zap2([1,2,3],[4,5]) == [(1,4), (2,5), (3, None)])
    assert(zap2([1,2,3,4,5],[4,5]) ==\
    ([(1,4), (2,5), (3, None),(4,None),(5,None)]))
    print("passed")

def testZap3():
    print("testing zap3")
    assert(zap3([1],[2,3],[4],[5],[6,7,8],[9]) == [(1,2,4,5,6,9),(3,7),(8,)])
    assert(zap3([1,2],[3,4,5]) == [(1,3), (2,4), (5,)])
    assert(zap3([1,2,3],[4,5]) == [(1,4), (2,5), (3,)])
    print("passed")

def testLineClass():
    print('Testing Line class...', end='')
    assert(str(Line(2,5))  == "y=2x+5")
    assert(str(Line(2,-5)) == "y=2x-5")
    assert(str(Line(0,5))  == "y=5")
    assert(str(Line(1,5))  == "y=x+5")
    assert(str(Line(-1,5)) == "y=-x+5")
    assert(str(Line(0,-5)) == "y=-5")
    assert(str(Line(0,0))  == "y=0")

    line1 = Line(2,3)
    assert(str(line1) == "y=2x+3")
    assert(line1.getSlope() == 2)
    assert(type(line1.getSlope()) == int)
    assert(line1.getIntercept() == 3)
    line2 = Line(6,-5)
    assert(str(line2) == "y=6x-5")
    assert(line2.getSlope() == 6)
    assert(line2.getIntercept() == -5)

    (x,y) = line1.getIntersection(line2) # (2, 7)
    assert(almostEqual(x, 2) and almostEqual(y, 7))

    line3 = Line(2, -3)
    (x,y) = line3.getIntersection(line2) # (0.5, -2)
    assert(almostEqual(x, 0.5) and almostEqual(y, -2))

    # parallel lines do not intersect
    assert(Line(2,3).getIntersection(Line(2,4)) == None)

    assert(line3.isParallelTo(line1) == True)
    assert(line3.isParallelTo(line2) == False)

    # getHorizontalLine returns a line that is horizontal
    # to the given line, intersecting at the given x value.
    line4 = line3.getHorizontalLine(4)
    assert(str(line4) == "y=5")
    assert(line4.getSlope() == 0)
    assert(line4.getIntercept() == 5)
    
    assert(Line(1, 2) == Line(1, 2))
    assert(Line(1, 2) != Line(1, 3))
    assert(not (Line(1, 2) == "don't crash here!"))

    s = set()
    assert(Line(1, 2) not in s)
    s.add(Line(1, 2))
    assert(Line(1, 2) in s)
    s.remove(Line(1, 2))
    assert(Line(1, 2) not in s)

    print('Passed.')

    
#testAltSum()
#testPwrSum()
#testPwrsOf3()
#testZap1()
#testZap2()
#testZap3()
#testLineClass()