import copy
# 
#CT1:
# 
# def p(a):
#         print(a)
# 
# def ct1(a):
#     b   =   copy.deepcopy(a)
#     c   =   a+a 
# 
#     print(a == b, a == c)
#     print(a is b, a is c)
#     print(c[0] is c[2], a[0] is c[0])
#     print(c[0][0] is a[0][0], a[0][0] is c[2][0])
# 
#     b[0][0] =   3
#     c[0][0] =   4
#     b[1]    =   [5]
#     c[1]    +=   [6]
# 
#     p(b)
#     p(c)    #   p   is  defined above
# 
# 
# a   =   [[1],[2]]
# ct1(a)
# print(p(a))    #   don't   miss    this


def ct2(a):
    (b, c) = (copy.copy(a), a[1:])
    a += [7]
    d = a
    a = a + [8]
    print(a, b, c, d)
 
a = [[5,6], [7,8]]
ct2(a)
print(a)
# 
# 
# def wordSearch(board,word):
#     rows, cols= len(board), len(board[0])
#     for row in range(rows):
#         for col in range(cols):
#             result= searchFromPosition(board,word, row,col)
#                 if result !=None:
#                   return result
#                 else: return None
# 
# def searchFromPosition(board,word,startRow,startCol):
#     for dir in range(8):
#         result= searchInDir(board,word,startRow,startCol,dir)
#             if result!=None:
#                 return result
#             else: return result
# 
# def searchInDir(board,word,startRow,startCol,dir):
#     rows,cols= len(board), len(board[0])
#     dirs= [(-1,-1), (-1,0), (-1,1),
#             (0,-1),         (0,1),
#             (1,-1), (1,0), (1,1)]
#     drow,dcol= dirs[dir]
#     for i in range(len(word)):
#         row= startRow+i*drow
#         col=startCol+i*dcol
#         if row<0 or row>=startRow or col<0 or col>=startCol or board[row][col]!= word[i]:
#             return None
#         else: return word, startRow, startCol

# 
# def checkRow(a):
#     rows= len(a)
#     for row in range(rows):
#         for i in row:
#             if a[row].count(i) >1:
#                 return False
# 
# def checkCol(a):
#     rows,cols= len(a), len(a[0])
#     colList=[]
#     for cols in range(cols):
#         colList.append(a[row][col])
#         
#             
# 
# 
# def isLatinSquare(a):
#     if checkRow(a) == True and checkCol(a) == True:
#         return True
#     else: return False
# import copy
# def f(a):
#        (b, c) = (a, copy.copy(a))
#        a[0] = 2
#        b[0] = 3
#        c[0] = 4
#        print (a[0], b[0], c[0])
#        a = c
#        a[0] = 5
#        b[0] = 6
#        c[0] = 7
#        print (a[0], b[0], c[0])      
# a = [8, 9]
# f(a)
# print(a[0])









