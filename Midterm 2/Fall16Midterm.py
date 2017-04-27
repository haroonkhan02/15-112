def f(d):
    d=str(d)
    copy=d
    if 0 in list(d):
        return None
    def solve(d,smallestNum=None,removedNum=None):
        print(smallestNum)
        if len(d)<=3:
            return True
        else:
            currNum= d[:3]
            d=d[1:]
            removedNum=d[0]
            if isLegal(copy,currNum):
                smallestNum=currNum
                result=solve(d,smallestNum,removedNum)
                if result!=None:
                    return smallestNum
                d= removedNum+d
            print("a")
            return None


def isLegal(copy,currNum):
    if int(currNum)%7!=0: 
        return False
    if copy.count(currNum)>1:
        return False
    return True

print(f(11266))

def findTripleSum(L,block=0):
    if isSolution:
        return L
    else:
        for num in l[block+1:]:
            
        subl= l[block:block+3]
        compare subl to prev block
        if good:
            findTripleSum(inserted subl, block+1)
        if bad:
            make different


class A(object):
    def __init__(self,x,y=None):
        self.x=x
        self.y=y
    def __repr__(self):
        if self.x==self.y:
            return "<Just %s>" % (self.x)
        return "<%s and %s>" %(self.x,self.y)
    def __eq__(self,other):
        return isinstance(other,A) and self.x==other.x
    def plus(self,other):
        if self.y==None:
            self.y=0
        return A(self.x+other.x, self.y+other.y)
    def reverse(self):
        self.x,self.y=self.y,self.x
        return A(self.x,self.y)
    def reversed(self):
        return A(self.y,self.x)
    def __hash__(self):
        return hash(self.x)

class B(A):
    def __init__(self,x):
        super().__init__(x)
    def __repr__(self):
        return "<Just %s>" % (self.x)
    def doubled(self):
        return B(self.x*2)

assert(str(A(2,3)) == "<2 and 3>")
assert(str(A(3,2)) == "<3 and 2>")
assert(str(A(3,3)) == "<Just 3>")
assert(isinstance(B(42), A)) 
assert(B(42) == A(42, 42)) 
assert(B(42) != A(2,3))
assert(B(42) != "don't crash here!") 
assert(str(B(42)) == "<Just 42>")
assert(A(1,2).plus(A(3,4)) == A(1+3,2+4)) 
assert(B(42).plus(A(3,4)) == A(42+3,42+4))
a1 = A(4,5)
a1.reverse()
assert(str(a1) == "<5 and 4>")
a2 = a1.reversed() # note: a1.reversed() is not a1.reverse() 
assert(str(a1) == "<5 and 4>")
assert(str(a2) == "<4 and 5>")
s = set() 
assert(B(42) not in s)
s.add(B(42)) 
assert(B(42)in s)
#B's and no other A's can call doubled:
# Note: only
assert(B(2).doubled() == B(4)) 
assert(type(B(2).doubled()) == B)
crashed = False
try: a = A(3,3).doubled() # this should crash 
except: crashed = True
assert(crashed == True)
print("Passed!")


def findTripleSum(L):
    if len(L)%3!=0:
        return None
    M= [[None]*len(L)]
    copy=L
    def solve(L):
        count=0
        if len(L)==0:
            return M
        else:
            for num in copy:
                for place in len(copy):
                    M[place]=num
                    L.remove(num)
                    indexofNum=L.index(num)
                    if isLegal(M):
                        result=solve(M)
                        if result!=None:
                            return M
                        else:
                            M[place]=None
                            L.insert(indexOfNum,num)
            return None
    
    def isLegal(M):
        start=0
        end=2
        for i in M:
            if isinstance(i,int):
                count+=1
        if i >3:
            return False
        sum=M[start]+M[start+1]+M[end]
        start,end=end,end+3
        for j in range(len(M)):





def selfReferencingFileCount(path):
    if os.path.isdir(path)
















