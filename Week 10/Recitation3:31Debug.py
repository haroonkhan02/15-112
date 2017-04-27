def flatten(L,depth=0): #this implementation has a bug!
    print("\t"*depth +str(L))
    if (not(isinstance(L,list))): return [L]
    result=[]
    for elem in L:
        result += flatten(elem,depth+1)
    print(result)
    return result

assert(flatten([1,[2]]) ==  [1,2])
assert(flatten([1,2,[3,[4,5],6],7]) ==  [1,2,3,4,5,6,7])
assert(flatten(['wow', [2,[[]]], [True]]) ==  ['wow', 2, True])

#############################################

class A(object): #this also has a bug!
    def __init__(self,x,y=42):
        self.x = x 
        self.y = y
    def __str__(self):
        return "A<x is %i, y is %i>" % (self.x,self.y)

    def getSwapped(self):
        temp = self.y
        self.y = self.x
        self.x = temp
        return self

assert(str(A(5)) == "A<x is 5, y is 42>")
assert(str(A(5, 99)) == "A<x is 5, y is 99>")
a = A(2, 3)
b = a.getSwapped()
assert(type(b) == A)
assert(str(b) == "A<x is 3, y is 2>")
assert(str(a) == "A<x is 2, y is 3>")