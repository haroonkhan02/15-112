#Lab 7
#Sydney Howard, showard
#Lab Partner: Kasden Bakos, kbakos

import string
import math

#slow1: 

def largestSumOfPairs(a):
    copy=a
    if len(a) <=1: return None     #check length of list
    maxNum= max(copy) 
    copy.pop(copy.index(maxNum))   #remove maximum number
    secondMaxNum= max(copy)
    return maxNum+ secondMaxNum


def containsPythagoreanTriple(a):
    for i in range(len(a)): 
        for j in range(i+1,len(a)):
            c= (a[i]**2 + a[j]**2)**0.5     #find third side
            if c in a:                 #check if c is in list
                return True
    return False
    
    
### Test Fcns

def testLargestSumOfPairs():
    print("testing largestSumOfPairs")
    assert(largestSumOfPairs([8,4,2,8]) == 16)
    assert(largestSumOfPairs([10,3,4,21]) == 31)
    assert(largestSumOfPairs([5,2,8,10]) == 18)
    assert(largestSumOfPairs([]) == None)
    print("passed")
    
def testContainsPythagoreanTriple():
    print("testing containsPythagoreanTriple")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4]) == True)
    assert(containsPythagoreanTriple([1,3,6,2,5,1]) == False)
    assert(containsPythagoreanTriple([6,10,5,4,12,20,13]) ==True)
    print("passed")
    
    
#testLargestSumOfPairs()
#testContainsPythagoreanTriple()