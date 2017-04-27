#Hw 10
#Sydney Howard, showard

import operator

def sumOfSquaresOfDigits(n):
    n=str(n)
    if n=="":
        return 0
    else:               #computes sum of square dig
        return int(n[0])**2 + sumOfSquaresOfDigits(n[1:]) 
        
def isHappyNumber(n):
    if n<1 or n==4:     #if 4, not happy
        return False
    if n==1:           #1 is happy
        return True
    if n>1:
        return isHappyNumber(sumOfSquaresOfDigits(n))

def binSearch(L,v,lo,high):
    mid= int((high+lo)/2)
    result=[]
    if L[mid]==v:
        result=[(mid,L[mid])]
        return result
    if lo>high:         #detects if v isn't in L
        return result
    else:
        if L[mid]>v:    #gets left side of list
            result= [(mid,L[mid])] + binSearch(L,v,lo,mid-1)
        if L[mid]<v:    #gets right side of list
            result= [(mid,L[mid])] + binSearch(L,v,mid+1,high)
        return result

def binarySearchValues(L,v):
    return binSearch(L,v,0,len(L)-1)    #set high and low values
    
   
def evalPrefixNotation1(L,nOnDeck=None,depth=0):
    if L==[]: return nOnDeck
    else:
        if isinstance(L[len(L)-1],int):     #check for integers
            if nOnDeck==None:
                nOnDeck=[L[len(L)-1]]
                return nOnDeck +\
                    (evalPrefixNotation1(L[:len(L)-1],nOnDeck,depth+1))
            else:
                nOnDeck.insert(0,L[len(L)-1])
                return nOnDeck +\
                    (evalPrefixNotation1(L[:len(L)-1],nOnDeck,depth+1))
                
        else:           #check for ops
            if L[len(L)-1] == "+":     
                currTotal= operator.add(nOnDeck[0],\
                        (nOnDeck[1]))  #calc total
                nOnDeck.remove(nOnDeck[0])  #remove first two elem
                nOnDeck.remove(nOnDeck[0])
            if L[len(L)-1] == "-":
                currTotal= operator.sub(nOnDeck[0],\
                        (nOnDeck[1]))
                nOnDeck.remove(nOnDeck[0])
                nOnDeck.remove(nOnDeck[0])
            if L[len(L)-1] == "*":
                currTotal= operator.mul(nOnDeck[0],\
                        (nOnDeck[1]))
                nOnDeck.remove(nOnDeck[0])
                nOnDeck.remove(nOnDeck[0])
            nOnDeck.insert(0, currTotal)      #add total to computing list
            return nOnDeck +evalPrefixNotation1(L[:len(L)-1],nOnDeck,depth+1)
            
def evalPrefixNotation(L,nOnDeck=None,depth=0):
    L=evalPrefixNotation1(L,nOnDeck=None,depth=0)
    return L[0]


def isinstance(a,b):
    return type(a)==b

class Polynomial(object):
    def __init__(self,coeffs):
        temp=[]
        indicator=False
        self.coeffs= coeffs
        if len(self.coeffs)==0:
            self.coeffs=[0]
        for j in self.coeffs:
            if j!=0 and indicator==False:       #gets rid of leading 0's
                temp.append(j)
                indicator=True
            elif indicator==True:
                temp.append(j)
        self.coeffs=temp
    def __repr__(self):
        if self.coeffs==[0]:
            return "Polynomial(%s)" % str(self.coeffs)
        else:
            return "Polynomial(coeffs=%s)" %self.coeffs
    def __hash__(self):
        return hash(tuple(self.coeffs))
    def __eq__(self,other):
        temp=[]
        if self.coeffs==[0]:          #deals with empty list
            return isinstance(other,Polynomial) and self.coeffs ==other.coeffs
        if self.degree()==0:        #returns integer if degree is 0
            for i in self.coeffs:
                self.coeffs=i
            return isinstance(other,int) 
        else:
            return isinstance(other,Polynomial) and self.coeffs ==other.coeffs
    def coeff(self,other):
        return self.coeffs[self.degree()-other]
    def degree(self):
        return len(self.coeffs)-1
    def evalAt(self,other):
        result=0
        for i in range(len(self.coeffs)):   #evaluates 'y' at point 'x'
            if len(self.coeffs)-1-i==0:
                result+= self.coeffs[i]
            else:
                result+= self.coeffs[i]*(other**(len(self.coeffs)-1-i))
        return result
    def scaled(self,other):     #finds new equation
        result=[]
        for i in range(len(self.coeffs)):
            result+= [self.coeffs[i]*other]
        self.coeffs=result
        return Polynomial(self.coeffs)
    

### Test Fcns

def testSumOfSq():
    print("testing testSumOfSq")
    assert(sumOfSquaresOfDigits(19) == 82)
    assert(sumOfSquaresOfDigits(82) == 68)
    assert(sumOfSquaresOfDigits(68) == 100)
    print("passed")

def testIsHappy():
    print("testing isHappyNum")
    assert(isHappyNumber(28) == True)
    assert(isHappyNumber(27) == False)
    assert(isHappyNumber(97) == True)
    print("passed")

def testBinSearch():
    print("testing binSearch")
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'c') ==\
        ([(2,'f'), (0,'a'), (1,'c')]))
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'm') ==\
        ([(2,'f'), (4,'m')]))
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'g') ==\
        ([(2,'f'),(4,'m'),(3,'g')]))
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'z')==\
        ([(2,'f'),(4,'m'),(5,'q')]))
    print("passed")

def testEvalPrefix():
    print("testing evalPrefix")
    assert(evalPrefixNotation(['+', 2, '*', 3, 4])==14)
    assert(evalPrefixNotation( ['+', '*', 2, 3, '*', 4, 5])==26)
    assert(evalPrefixNotation([42])==42)
    assert(evalPrefixNotation(['-', '+', 2, 3, -1])==6)
    assert(evalPrefixNotation(['-', '+', '*', 5, 2, 3, '*', 3, 4])==1)
    print("passed")

def testPolynomialClass():
    print('Testing Polynomial class...', end='')
    testPolynomialBasics()
    testPolynomialEq()
    testPolynomialConstructor()
    testPolynomialInSets()
    print('Passed.')

def testPolynomialBasics():
    # we'll use a very simple str format...
    assert(str(Polynomial([1,2,3])) == "Polynomial(coeffs=[1, 2, 3])")
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
    assert(p1.degree() == 2)
    # p.coeff(i) returns the coefficient for x**i
    assert(p1.coeff(0) == 5)
    assert(p1.coeff(1) == -3)
    assert(p1.coeff(2) == 2)
    # p.evalAt(x) returns the polynomial evaluated at that value of x
    assert(p1.evalAt(0) == 5)
    assert(p1.evalAt(2) == 7)
    # p.scaled(scale) returns a new polynomial with all the
    # coefficients multiplied by the given scale
    p2 = p1.scaled(10) # 20x**2 - 30x + 50
    assert(isinstance(p2, Polynomial))
    assert(p2.evalAt(0) == 50)
    assert(p2.evalAt(2) == 70)

def testPolynomialEq():
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42)
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42)

def testPolynomialConstructor():
    # If the list is empty, treat it the same as [0]
    assert(Polynomial([]) == Polynomial([0]))
    assert(Polynomial([]) != Polynomial([1]))
    # Remove leading 0's
    assert(Polynomial([0,0,0,1,2]) == Polynomial([1,2]))
    assert(Polynomial([0,0,0,1,2]).degree() == 1)
    # Require that the constructor be non-destructive
    coeffs = [0,0,0,1,2]
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    assert(coeffs == [0,0,0,1,2])
    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert(Polynomial(coeffs) == Polynomial([1,2]))

def testPolynomialInSets():
    s = set()
    assert(Polynomial([1,2,3]) not in s)
    s.add(Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2]) not in s)

#testSumOfSq()
#testIsHappy()
#testBinSearch()
#testPolynomialClass()
testEvalPrefix()
