
import math
import string

## Quiz 2

def isND(n):
    if n<10 and n%2==1:
        return True
    n= str(n)
    for i in range(len(str(n)),0,-1):
        if n[i]%2==0: return False
        else:
            if n[i]<= n[i-1]:
                return False
    return True
    
def nthND(n):
    found=-1
    guess=0
    while found<n:
        guess+=1
        if isND(guess)==True:
            found+=1
    return guess

def testNthND():
    print("testing nthND")
    assert(nthND(0) ==1)
    assert(nthND(9) == 71)
    assert(nthND(13) == 93)
    print("Passed")

# testNthND()

def h(f,x):
    return f(x)

def latticePointCount(f,x1,x2):
    x1=math.ceil(x1)
    x2= math.floor(x2)
    count=0
    if i in range(x1, x2+1):
        if isinstance(h(f,i),int) == True:
            if h(f,i) >=x1 or h(f,i) <= x2:
                count+=1
    return count
    
grid-demo.py

### Quiz 3

def encode(s,pwd):
    newS= ""
    count= len(s)
    lenPwd= len(str(pwd))
    for i in range(len(s)):
        offset= int(pwd[i%pwd])
        distFroma= ord(s[i]- ord("a"))
        shifted= distFroma+ offset
        newS+= chr(ord("a") + shifted%26)
    return newS
    
### Quiz 4

def nearMedians(L):
    if L== []: return None
    for j in L:
        if isinstance(j, int) == False:
            return None
    L.sort()
    list=[]
    if len(L)%2==1:
        median= L[len(L)//2]
    else:
        medianIndex= len(L)//2)
        median= (L[medianIndex]+ L[medianIndex+1])/2
    for i in L:
        if i <= median+10 and i >= median-10:
            list+= i
    return list
    