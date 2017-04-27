#Hw9
#Sydney Howard, showard
"""
F16 Quiz 7:

1.
bigOh1: O(N**2)
bigOh2: O(N**2)
bigOh3: O(N**2)

2. 
a. [2,5,3,7]

b. [2,3,7,5]

c. The worst-case big oh of mergesort is O(logN). If you make each number its
 own list and combine two lists by sorting them, the O(N). If the list has n 
 number of elements, now there are n/2 lists that are sorted within their own
  lists. Then take two lists at a time and sort/combine them into one list; 
  this has a big oh of O(N). Keep repeating until there is only one list that 
  is completely sorted. Since each time you combine two lists the big oh is 
  O(N), added up, the collective big oh is O(logN)

d. 
0: 'bc', 'abc'
1: 'ab', 'e'
2: 'cd'

3.
ct1: []

ct2: [2,15,21,32,43]

4. d= {1:3,0:0,2:2,-2:-2}

5.
def mostPopularFriend(d):
    finalS=None
    for key in d:
        if finalS!=None:
            finalS= finalS.intersection(d[key])
        else:
            finalS=d[key]
    for i in finalS:
        return i

"""


def invertDictionary(d):
    newD= dict()
    for key in d:
        if d[key] not in newD:      #creates new set for key
            newD[d[key]]=set([key])
        else:
            newD[d[key]].add(key)   #adds values to existing set if key has 
    return newD                     #multiple values
    
def friendsOfFriends(d):
    fofDict= dict()
    for friendKey in d:         #loops through keys
        currFriends= d[friendKey]
        if d[friendKey]==set():
            fofDict[friendKey]=set()
        for i in currFriends:   #loops through values
            if i in d:  
                for j in d[i]:
                    if j not in currFriends: #compares different keys' values   
                        if j==friendKey:
                            pass
                        else:
                            if friendKey not in fofDict:
                                fofDict[friendKey]=set([j])
                            else: 
                                fofDict[friendKey].add(j)
    return fofDict
                    

def getPairSumN2(a,target):
    result= []
    for i in range(len(a)):
        for j in range(i+1, len(a)):  
            if a[i]+a[j]== target:  #checks the sum of pairs in list
                result.append(a[i])
                result.append(a[j])
        return result

def getPairSumN(a,target):
    result=[]
    a=set(a)
    copy=a
    for i in a: 
        copy.discard(i)  #gets rid of value for every loop
        for j in copy:
            if i+j== target:  #checks for desired sum
                result.append(i)
                result.append(j)
        return result
        
    
    
### Test Fcns

def testInvertDict():
    print("testing invertDict")
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == 
            ({2:set([1]), 3:set([2,5]), 4:set([3])}))
    assert(invertDictionary({"a":2, "b":3, "c":4, "d":3}) == 
            ({2:set(["a"]), 3:set(["b","d"]), 4:set(["c"])}))
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3, 123:2}) == 
            ({2:set([1,123]), 3:set([2,5]), 4:set([3])}))
    print("passed")
    
def testfof():
    print("tesing fof")
    assert(friendsOfFriends(({"fred": set(["wilma", "betty", "barney",
     "bam-bam"]), "wilma": set(["fred", "betty", "dino"])})) == 
     ({"fred":set(["dino"]), "wilma": set(["barney", "bam-bam"])}))
    assert(friendsOfFriends(({"fred": set(["wilma", "betty", "barney",
     "bam-bam","bob"]), "wilma": set(["fred", "betty", "dino"])})) == 
     ({"fred":set(["dino"]), "wilma": set(["barney", "bam-bam","bob"])}))
    assert(friendsOfFriends(({"fred": set(["wilma", "betty", "barney",
     "bam-bam"]), "wilma": set(["fred", "betty", "dino","bob"])})) == 
     ({"fred":set(["dino","bob"]), "wilma": set(["barney", "bam-bam"])}))
    assert(friendsOfFriends({'fred': {'barney', 'betty', 'bam-bam', 'wilma'},\
     'barney': set(), 'betty': set(), 'bam-bam': set(), 'dino': set(),\
     'wilma': {'fred', 'betty', 'dino'}}) =={'fred': {'dino'},\
     'barney': set(), 'bam-bam': set(), 'betty': set(),\
     'wilma': {'barney', 'bam-bam'}, 'dino': set()})
    assert(friendsOfFriends({'F': {'D'}, 'A': {'F', 'D', 'B'},\
    'B': {'C', 'D', 'A', 'E'}, 'E': {'C', 'D'}, 'C': set(),\
    'D': {'E', 'F', 'B'}}) =={'F': {'E', 'B'}, 'A': {'C', 'E'},\
    'B': {'F'}, 'E': {'F', 'B'}, 'C': set(), 'D': {'C', 'A'}})

    print("passed")

def testGetPairSumN2():
    print("Testing getPairSum...", end="")
    assert(getPairSumN2([1],1) == [])
    assert(getPairSumN2([5, 2], 7) in [ [5, 2], [2, 5] ])
    assert(getPairSumN2([10,-1,1,-8,3,1], 2) in 
        ([[10, -8], [-8, 10], [-1, 3], [3, -1],[1, 1]]))
    assert(getPairSumN2([10,-1,1,-8,3,1], 10) == [])
    assert(getPairSumN2([1, 4, 3], 2) == [])
    print("Passed!")

def testGetPairSumN():
    print("Testing getPairSum...", end="")
    assert(getPairSumN([1],1) == [])
    assert(getPairSumN([5, 2], 7) in [ [5, 2], [2, 5] ])
    assert(getPairSumN2([10,-1,1,-8,3,1], 2) in 
        ([[10, -8], [-8, 10], [-1, 3], [3, -1],[1, 1]]))
    assert(getPairSumN([10,-1,1,-8,3,1], 10) == [])
    assert(getPairSumN([1, 4, 3], 2) == [])
    print("Passed!")


# testInvertDict()
#testfof()
# testGetPairSumN2()
# testGetPairSumN()