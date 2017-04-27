def ct1(s):
    (a, t1) = ( [ ], '' )
    for i in range(len(s)):
        t2 = s[i : i//2 : -1]
        if (len(t2) > len(t1)):
            a.append(t2)
            t1 = t2
    while (a != [ ]):
        print(a.pop())
#ct1('abcdef') # prints 3 values

def ct2(L):
    n = len(L)
    for i in range(n):
        M = L[i]
        if (i == 2): L[i] = L[i-1]
        M.reverse()
    for i in range(n):
        print(L[i][i])
#ct2([[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9,10,11],
     #[ 12, 13, 14, 15]]) # prints 4 values
     
     
def ct3(L, x):
    for f in L:
        if (f == ct3): break
        x = f(x)
        if (f == h): print("h")
        print(x)
def g(x): return x*10
def h(x): return x+g(x)
L = [g, h, g, ct3, h, g, h]
#ct3(L, 2) # prints 4 values

def rc1(n):
    assert(isinstance(n, int) and
(n >= 0) and (n < 1234)) 
    x=y=0
    for i in range(2, 1234):
        if ((i % (i//2) > 0) and
            ((i//10) == (i%10))):
            (x, y) = (y, i)
    return (x == n)
    
#print(rc1(77)) 

def rc2(M):
    assert(isinstance(M, list))
    (i, n) = (3, 1)
    for val in M:
        if (int(str(i)*n) != val):
            return False
        i -= 1
        if (i == 0): (i, n) = (3, n+1)
    return (len(M) == 7)
    
#print(rc2([3,2,1,33,22,11,333]))

def ct4(a):
    (b, c, d) = (a, [a[0]], [a[0][:], a[1][:]]) 
    b[0][0] += 3
    a = a + [4]
    print(d + [b[0]])
    print(d.append(b[1]))
    print(a, b, c, d)
a = [[2,9], [3, 7]]

#ct4(a)


def ct1(s):
    print(chr(ord('G') + ord(s[1]) - ord(s[0])), end='')
    t, count = '', 0
    for c in s:
        if (not c.isalnum()): t += c
        if (c.isdigit()): print(c, end='')
        elif (c.isupper()): print(c.lower(), end='') 
        else: count += 1
    return ('\tt=%s\t%d' % (t, count))
print(ct1('ae1#B2cD!'))
    

    