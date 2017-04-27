#Lab 9
#Sydney Howard, showard
#Lab Partners: Kasden Bakos (kbakos), Elena Chan (elenac)

import string
import math

## Better Big Oh
"""
slow1:
1. the function counts the number of elements in a
2. O(N) because it goes through every element to pop it
3. 
def slow1(a):
    return len(a)
    
4. O(1) because the function acesses the length directly


slow2:
1. if none of the elements repeat, it returns True
2. O(N**2) because it loops through a twice and has a nested for loops
3.
def slow2(a):
    b= set(a)
    return a==list(b)
    
4. O(N) because we changed it from a list to a set 


slow3:
1. checks how many elements are not similar in a and b
2. O(N**2) because the for loop goes through each element of b
3.
def slow3(a,b):
    a= set(a)
    b= set(b)
    return len(b.difference(a))
    
4. O(N) becasue it changes from a list to a set

slow4:
1. it checks for the biggest difference between one term in a and one term in b
2. O(N**2) because it has a nested for loop that loops through each element 
in a and b
3. 
def slow4(a,b):
    difference1= abs(max(a)-min(b))
    difference2= abs(max(b) - min(a))
    return max(difference1,difference2)

4. O(N) because the max and min calls check every element in a list

slow5:
1. it checks for the smallest difference between an element in a and b
2. O(N**2) because it has a nested for loop that loops through each element 
in a and b
3.
def slow5(a,b):
    a= sorted(a)
    for i in b:
        index= bisect.bisect(a,i,0,len(a))
        if index== len(a):
            difference= abs(i- a[index-1])
        else:
            diff1= abs(i- a[index-1])
            diff2= abs(a[index+1] - i)
            if diff1<=diff2:
                difference= diff1
            else:
                difference= diff2
    return difference
    
4. O(NlogN) because it has one for loop that loops through the unsorted list
    
"""

def largestSumOfPairs(a):
    copy=a
    if len(a) <=1: return None     #check length of list
    maxNum= max(copy) 
    copy.pop(copy.index(maxNum))   #remove maximum number
    secondMaxNum= max(copy)
    return maxNum+ secondMaxNum


def containsPythagoreanTriple(a):
    a=set(a)
    for i in a: 
        for j in a:
            c= (i**2 + j**2)**0.5     #find third side
            if c in a:                 #check if c is in a
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