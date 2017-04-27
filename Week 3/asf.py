def ct1(s):
# Hint: ord('A') > ord('9')
    t = 'Z'
    for c in s.upper():
        if (c > t[-1]): t += c
        elif (c >= 'A'): t += str(ord(c) - ord('A')) 
        else: t += 'n' + c
    return t
print(ct1("a1B2")) # hint: prints 6 characters
