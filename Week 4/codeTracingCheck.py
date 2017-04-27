# def ct1(L): 
#     result = [ ]
#     M = [L[i]*10**i for i in range(len(L))] 
#     for val in M:
#         result.extend([val, L.pop()]) 
#     return result
# L = [2,5,3] 
# M = ct1(L) 
# print(L, M)

# 
# def ct2(L): 
#     result = [ ]
#     M = copy.copy(L)
#     if (M == L): result.append(1)
#     if (M is L): result.append(2)
#     if (M[0] == L[0]): result.append(3) 
#     if (M[0] is L[0]): result.append(4)
#     return result
# print(ct2([5,7,6]))


def ct3(L): 
    M=L
    L += [4]
    M = M + [5] 
    print(L, M)
ct3(list(range(1)))