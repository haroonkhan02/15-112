#################################################
# Lab3
#Sydney Howard, showard, E
#Lab partners: Max Perry (maperry), Jen Choi (jaeeunc1)
#################################################

import cs112_s17_linter
import math, string

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Exercises
#################################################

def longestCommonSubstring(s1, s2):
    if s1=="" and s2=="": return ""
    sliced=""
    bestStr=""
    for i in range(0,len(s1)): 
       for j in range(i+1, len(s1)+1):
            sliced= s1[i:j]
            if s2.find(sliced)==-1:
                continue
            else:
                if len(sliced)>len(bestStr):
                    bestStr=sliced
                elif len(sliced)==len(bestStr):
                    bestStr= min(sliced,bestStr)
    return bestStr

def oddRows(text, rows, count1):
    code1=""
    temp=rows
    columns= math.ceil(len(text)/rows)
    for letter in text[count1: len(text): columns]:
            code1+= letter
    return code1

def evenRows(text, rows, count2):
    code2=""
    temp=rows 
    columns= math.ceil(len(text)/rows)
    for letter in text[(len(text)-count2):0: -columns]:
            code2+= letter
    return code2
    
def encodeRightLeftCipher(text, rows):
    code=""
    temp=rows
    origText=text
    count1=0
    count2=rows-1
    columns= math.ceil(len(text)/rows)
    alphabet= "zyxwvutsrqponmlkjihgfedcba"
    remainder= (columns*rows)-len(text)
    addOn= alphabet[0:remainder]
    newText= text+ addOn
    for rowNum in range(1,rows+1):
        if rowNum%2!=0:
            code+= oddRows(newText,columns,count1)
            count1+=2
        elif rowNum%2==0:
            code+=evenRows(newText, columns, count2)
            count2-=2
    return str(temp) + code

def digitRemove(cipher):
    rows=""
    for c in cipher:
        if c.isdigit():
            rows+=c
    return int(rows)
    
def digitCount(n):
    count=0
    while n>0:
        count+=1
        n//=10
    return count

def reverse(s):
    return s[::-1]

def decodeRightLeftCipher(cipher):
    rows= digitRemove(cipher)
    cipher= cipher[digitCount(rows):]
    columns=len(cipher)//(rows)
    result=""
    cipherFlipped=""
    final=""
    for i in range(rows):
        if i%2==0:
            normalText= cipher[i*columns: (i+1)*columns]
            cipherFlipped+= normalText
        if i%2!=0:
            slicedText= cipher[i*columns: (i+1)*columns]
            cipherFlipped+= reverse(slicedText)
    for rowNum in range(0, columns): 
        result+= cipherFlipped[rowNum: len(cipher)+1: columns]
    for c in result:
        if c.isupper():
            final+=c
    return final
    

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testEncodeRightLeftCipher():
    print("Testing encodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 4
    # W T A W
    # E A T N
    # A C D z
    # T K A y
    rightLeft = "4"+"WTAWNTAEACDzyAKT"
    cipher = encodeRightLeftCipher(text, rows)
    assert(rightLeft == cipher)
    

def testDecodeRightLeftCipher():
    print("testing decodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 6
    cipher = encodeRightLeftCipher(text, rows)
    plaintext = decodeRightLeftCipher(cipher)
    assert(plaintext == text)
    print("passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLongestCommonSubstring()
    testEncodeRightLeftCipher()
    testDecodeRightLeftCipher()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,repr,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
