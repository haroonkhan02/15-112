#Lab 5
#Sydney Howard, showard
#Group: Kasdan Bakos (kbakos), Jack Sampiere (jsampier)

import string, math


def removeRowAndCol(A,row,col):
    result, minusCol=[], []
    minusRow= A[0:row] + A[row+1:]          #removes row
    for i in minusRow:
        minusCol= i[0:col] + i[col+1:]      #removes column
        result.append(minusCol)
    return result
    
def destructiveRemoveRowAndCol(A,row,col):
    A.remove(A[row])                            #removes row
    for i in range(len(A)):
        A[i].remove(A[i][col])                  #removes column

def areLegalValues(values):
    digits=string.digits
    if len(values)!= (math.sqrt(len(values))**2): #checks if it's a symmetrical
        return False
    for i in range(len(values)):
        if (values.count(values[i]) >1) and (values[i] != 0):return False
        if values[i] not in range(len(values)+1): return False
    return True                                            
    
def isLegalRow(board,row):
    return areLegalValues(board[row])

def isLegalCol(board,col):
    colList=[]
    for num in range(len(board)):          #creates list of numbers in columns
        colList.append(board[num][col])
    return areLegalValues(colList)

def isLegalBlock(board,block):
    n= int(len(board)**.5)
    blockList=[]
    row, col= block//n, block%n 
    for i in range(row * n, (row+1)*n):         #isolates select rows
        for j in range(col*n, (col+1)*n):       #isolates select columns
            blockList.append(board[i][j])      
    return areLegalValues(blockList)
    
def isLegalSudoku(board):
    n= int(len(board)**.5)
    for i in range(n**2): #checks if board is correct
        if ((isLegalRow(board,i) == True) and (isLegalCol(board,i) == True)
                                        and (isLegalBlock(board,i) == True)):
            continue
        else: return False
    return True
    
    
######
def testRemoveRowAndCol():
    print("testing RemoveRowAndCol")
    assert(removeRowAndCol([[ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]],1,2) == 
                            [[ 2, 3, 5],[ 0, 1, 3]])
    assert(removeRowAndCol([[1,2,3],[4,5,6]],0,2) == 
                            [[4,5]])
    assert(removeRowAndCol([[1,2,3],[4,5,6],[7,8,9]],0,1) == 
                            [[4,6],[7,9]])
    assert(removeRowAndCol([[1,2],[3,4],[5,6],[7,8]],3,0) == 
                            [[2],[4],[6]])
    print("Passed!")
    
def testDestructiveRemoveRowAndCol():
    print("testing DestructiveRemoveRowAndCol")
    assert(destructiveRemoveRowAndCol([[ 2, 3, 4, 5],[ 8, 7, 6, 5],
                                    [ 0, 1, 2,3]],1,2) == None)
    assert(destructiveRemoveRowAndCol([[1,2,3],[4,5,6]],0,2) == None)
    assert(destructiveRemoveRowAndCol([[1,2,3],[4,5,6],[7,8,9]],0,1) == None)
    assert(destructiveRemoveRowAndCol([[1,2],[3,4],[5,6],[7,8]],3,0) == None)
    print("Passed!")


def testAreLegalValues():
    print("testing areLegalValues")
    assert(areLegalValues([ 5, 3, 0, 0, 7, 0, 0, 0, 0 ]) == True)
    assert(areLegalValues([ 4, 0, 0, 8, 0, 3, 0, 0, 1 ]) == True)
    assert(areLegalValues([ 4, 4, 0, 8, 0, 3, 0, 0, 1 ]) == False)
    print("Passed")

def testIsLegalRow():
    print("testing islegalrow")
    assert(isLegalRow([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]], 1) == True)
  
    assert(isLegalRow([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]], 5) == True)
  
    assert(isLegalRow([
  [ 5, 3, 0, 0, 7, 1, 1, 1, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]], 0) == False)
    print("Passed")

def testIsLegalCol():
    print("testing islegalcol")
    assert(isLegalCol([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]], 1) == True)
  
    assert(isLegalCol([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]], 5) == True)
  
    assert(isLegalCol([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 5, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 5, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 5, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]], 0) == False)
    print("passed")

def testIsLegalBlock():
    print("Testing isLegalBlock()...", end='')
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assert(isLegalBlock(board,1) == True)
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]
    assert(isLegalBlock(board, 2) == False)
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 1, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert(isLegalBlock(board, 5) == False)
    print("Passed!")

def testIsLegalSudoku():
    print("testing isLegalSudoku")
    assert(isLegalSudoku([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]) == True)
    assert(isLegalSudoku([
  [ 5, 3, 3, 3, 7, 3, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]) == False)
    assert(isLegalSudoku([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 9, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 9, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]) == False)
    assert(isLegalSudoku([
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0,3,0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]) == False)
    print("Passed!")

# testRemoveRowAndCol()
# testDestructiveRemoveRowAndCol()
# testAreLegalValues()
# testIsLegalRow()
# testIsLegalCol()
# testIsLegalBlock()
# testIsLegalSudoku()

