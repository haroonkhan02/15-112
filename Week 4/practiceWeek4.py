
from tkinter import *

def isPalindromicList(a):
    result=[]
    for i in range(len(a),0,-1):
        result.append(a[i])
    if result==a:return True
    else: return False
    
def isRotation(a1,a2):
    if a1.sort() == a2.sort():return True
    else: return False

def mostCommonNames(a):
    a.sort() 
    currName=""
    bestName=[]
    currCount=1
    bestCount=-1
    for name in a:
        currName= name
        currCount+=1
        if currCount> bestCount:
            bestName.append(currName)
            bestCount=currCount
            currCount=0
        elif currCount< bestCount:
            currCount=0
        elif currCount==bestCount:
            bestName.append(currName)
            print("alsdkf")
            currCount=0
    print(bestName)
    return bestName


# def drawBelgianFlag(canvas,winWidth,winHeight):
#     canvas.create_rectangle(0,0,width/3, height,fill='black')
#     canvas.create_rectangle(width/3,0, width*2/3, height, fill='yellow')
#     canvas.create_rectangle(width*2/3,0, width, height, fill='red')
# 
# 
# def runBelgianFlag(winWidth=500,winHeight=500):
#     root=Tk()
#     canvas= canvas(root, width=winWidth, height=winHeight)
#     canvas.pack()
#     drawBelgianFlag(canvas,width,height)
#     root.mainloop()


#### TEST FCNS

def testIsPalindromicList():
    assert(isPalindromicList([a,b,a]) == True)
    assert(isPalindromicList([1,2,3]) == False)
    assert(isPalindromicList([2,3,2]) == True)
    
def testIsRotation():
    assert(isRotation([2,3,4,5,6],[4,5,6,2,3]) == True)
    assert(isRotation([2,3,4,5,6],[3,2,4,5,6]) == False)
    
def testMostCommonNames():
    assert(mostCommonNames(['Jane', 'Aaron', 'Jane', 'Cindy', 'Aaron']) == ['Aaron', 'Jane'])

testMostCommonNames()

    

    
    