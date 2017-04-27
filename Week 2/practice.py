def isPrime(n):
    if n <2:
        return False
    if n%2==0:
        return False
    if n==2:
        return True
    maxFactor= round(n**0.5)
    for i in (3,maxFactor+1,2):
        if n%i==0:
            return False
    return True
    
def nthPrime(n):
    found=0
    guess=0
    while found<n:
        guess+=1
        if isPrime(guess)==True:
            found+=1
    return guess
    
def	ct1(x, y):
    for z	in range(y, x):
        print(42, z)
    for z	in range(x, y):
        if(z < y//2):
            if (z%2 == 0): print(2,	z)
            elif (z%5 == 0): print(5,z)
        elif	(x+y+z == 27):
            print(27, z, end)
    w = 0
    for z	in range(x, 10*x, x):
        if (z	< 5*x): continue
        elif (z >= 7*x): return w
        w += z
    return 99
print(ct1(3, 12))

def g(z):
    for x in range(1,z,3):
       print("#", x, ":")
       for y in range(z, x, -2):
           return (x,y)
       print()
(g(6))

def fc1(m):
    if ((not isinstance(m,int)) or (m<0)): return False
    x=1
    while (x<m//2): x+=10
    return (x+m==60)
print(fc1(39))
