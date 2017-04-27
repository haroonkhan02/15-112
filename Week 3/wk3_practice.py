#################################################
# Week3 Practice
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
# Tue Lecture
#################################################

def isVowel(c):
    if c== "a" or c == "e" or c=="i" or c=="o" or c=="u": return True
    
def vowelCount(s):
    s=s.lower()
    count=0
    for c in s:
        if isVowel(c):
            count+=1
    return count

def interleave(s1, s2):
    result=""
    shorterStrLen= min(len(s1), len(s2))
    for i in range(shorterStrLen): #alternating for len of shorter str
        result+= s1[i] + s2[i]
    result= result + s1[shorterStrLen:]+ s2[shorterStrLen:]
    return result

def isLeft(c):
    if c=="(": return True

def isRight(c):
    if c==")": return True
    
def hasBalancedParentheses(s):
    if s=="": return True
    if s[0] == ")": return False
    numLeft=0
    numRight=0
    for c in s:
        if isLeft(c):
            numLeft+=1
        elif isRight(c):
            numRight+=1
    if numRight == numLeft:
        return True
    else:
        return False

#################################################
# Wed Recitation
#################################################

def rotateStringLeft(s, k):
    return s[k%len(s):len(s)+1] + s[0: k%len(s)]

def rotateStringRight(s, k):
    return s[len(s)-k%len(s): len(s)] + s[0: len(s)-k%len(s)]

def wordWrap(text, width):
    text= text.strip()
    result= ""
    count=-1
    for a in text:
        count+=1
        if count%width==0:
            result += "\n"
        result+=a
    result= result.replace(" ", "-")
    result= result.strip()
    return result

def largestNumber(s):
    return 42

#################################################
# Thu Lecture
#################################################

def longestSubpalindrome(s):
    return 42

def leastFrequentLetters(s):
    s=s.lower()
    currCount=0
    bestCount=1000
    bestLetter=""
    currLetter=""
    for a in s:
        print("a", a)
        for i in range(len(s)):
            print("i", i)
            if a == s[i]:
                currCount+=1
                currLetter=a
                print(currCount)
                print(currLetter)
            if currCount< bestCount:
                print("adfk")
                bestCount=currCount
                bestLetter=currLetter
                print("bestLetter", bestLetter)
            elif currCount==bestCount:
                bestLetter+=currLetter
        currCount=0
        currLetter=""
    print("end",bestLetter)
    return bestLetter

# some interactive console game!

#################################################
# Extra Practice
#################################################

def sameChars(s1, s2):
    return 42

def mostFrequentLetters(s):
    return 42

def areAnagrams(s1, s2):
    return 42

def collapseWhitespace(s):
    return 42

def replace(s1, s2, s3):
    return 42

def encodeOffset(s, d):
    return 42

def decodeOffset(s, d):
    return 42

def encrypt(msg, pwd):
    return 42

def decrypt(msg, pwd):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Passed!")

def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert(hasBalancedParentheses("()") == True)
    assert(hasBalancedParentheses("") == True)
    assert(hasBalancedParentheses("())") == False)
    assert(hasBalancedParentheses("()(") == False) 
    assert(hasBalancedParentheses(")(") == False)
    assert(hasBalancedParentheses("(()())") == True)
    assert(hasBalancedParentheses("((()())(()(()())))") == True)
    assert(hasBalancedParentheses("((()())(()((()())))") == False)
    assert(hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")

def testRotateStringLeft():
    print("Testing rotateStringLeft()...", end="")
    assert(rotateStringLeft("abcde", 0) == "abcde")
    assert(rotateStringLeft("abcde", 1) == "bcdea")
    assert(rotateStringLeft("abcde", 2) == "cdeab")
    assert(rotateStringLeft("abcde", 3) == "deabc")
    assert(rotateStringLeft("abcde", 4) == "eabcd")
    assert(rotateStringLeft("abcde", 5) == "abcde")
    assert(rotateStringLeft("abcde", 25) == "abcde")
    assert(rotateStringLeft("abcde", 28) == "deabc")
    print("Passed!")

def testRotateStringRight():
    print("Testing rotateStringRight()...", end="")
    assert(rotateStringRight("abcde", 0) == "abcde")
    assert(rotateStringRight("abcde", 1) == "eabcd")
    assert(rotateStringRight("abcde", 2) == "deabc")
    assert(rotateStringRight("abcde", 3) == "cdeab")
    assert(rotateStringRight("abcde", 4) == "bcdea")
    assert(rotateStringRight("abcde", 5) == "abcde")
    assert(rotateStringRight("abcde", 25) == "abcde")
    assert(rotateStringRight("abcde", 28) == "cdeab")
    print("Passed!")

def testSameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("abcabcabc", "cba") == True)
    assert(sameChars("cba", "abcabcabc") == True)
    assert(sameChars("abcabcabc", "cbad") == False)
    assert(sameChars("abcabcabc", "cBa") == False)
    assert(sameChars(42,"The other parameter is not a string") == False)
    assert(sameChars("","") == True)
    assert(sameChars("","a") == False)
    print("Passed!")

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("Cat") == 'ACT')
    assert(mostFrequentLetters("A cat") == 'A')
    assert(mostFrequentLetters("A cat in the hat") == 'AT')
    assert(mostFrequentLetters("This is a test") == 'ST')
    assert(mostFrequentLetters("This is an I test?") == 'IST')
    assert(mostFrequentLetters("") == "")
    print("Passed!")

def testWordWrap():
    print("Testing wordWrap()...", end="")
    assert(wordWrap("abcdefghij", 4) == """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg", 4) == """\
a*b
c*de
fg""")
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testLeastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    assert(leastFrequentLetters("abc def! GFE'cag!!!") == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".lower()) == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".upper()) == "bd")
    assert(leastFrequentLetters("") == "")
    assert(leastFrequentLetters("\t \n&^#$") == "")
    noq = string.ascii_lowercase.replace('q','')
    assert(leastFrequentLetters(string.ascii_lowercase + noq) == "q")
    print("Passed!")

def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert(areAnagrams("", "") == True)
    assert(areAnagrams("abCdabCd", "abcdabcd") == True)
    assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\n\n\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") ==
                              "a b c ")
    print("Passed!")

def testReplace():
    print("Testing replace()...", end="")
    (s1, s2, s3) = ("abcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abcdeabcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("babababa", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abb", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "", "q")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "ab", "")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    print("Passed!")

def testEncodeOffset():
    print("Testing encodeOffset()...", end="")
    assert(encodeOffset("ACB", 1) == "BDC")
    assert(encodeOffset("ACB", 2) == "CED")
    assert(encodeOffset("XYZ", 1) == "YZA")
    assert(encodeOffset("ABC", -1) == "ZAB")
    assert(encodeOffset("ABC", -27) == "ZAB")
    assert(encodeOffset("Abc", -27) == "Zab")
    assert(encodeOffset("A2b#c", -27) == "Z2a#b")
    print("Passed!")

def testDecodeOffset():
    print("Testing decodeOffset()...", end="")
    assert(decodeOffset("BDC", 1) == "ACB")
    assert(decodeOffset("CED", 2) == "ACB")
    assert(decodeOffset("YZA", 1) == "XYZ")
    assert(decodeOffset("ZAB", -1) == "ABC")
    assert(decodeOffset("ZAB", -27) == "ABC")
    assert(decodeOffset("Zab", -27) == "Abc")
    assert(decodeOffset("Z2a#b", -27) == "A2b#c")
    print("Passed!")

def testEncrypt():
    print("Testing encrypt()...", end="")
    assert(encrypt("Go Team!", "azby") == "GNUCAL")
    assert(encrypt("a1m2a3z4i5n6g !?!?", "yes") == "YQSXMFE")
    assert(encrypt("", "wow") == "")
    assert(encrypt("Wow!", "AZBY") == "password must be all lowercase")
    print("Passed!")

def testDecrypt():
    print("Testing decrypt()...", end="")
    assert(decrypt("GNUCAL", "azby") == "GOTEAM")
    assert(decrypt("YQSXMFE", "yes") == "AMAZING")
    assert(decrypt("", "wow") == "")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testVowelCount()
    testInterleave()
    testHasBalancedParentheses()
    testRotateStringLeft()
    testRotateStringRight()
    #testWordWrap()
    #testLargestNumber()
    #testLongestSubpalindrome()
    testLeastFrequentLetters()
    testSameChars()
    testMostFrequentLetters()
    testAreAnagrams()
    testCollapseWhitespace()
    testReplace()
    testEncodeOffset()
    testDecodeOffset()
    testEncrypt()
    testDecrypt()

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
