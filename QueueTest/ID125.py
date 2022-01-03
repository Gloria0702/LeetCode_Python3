def isPalindrome(aString):

    chare = []
    aString = aString.lower()
    for ch in aString:
        if ch in "qwertyuiopasdfghjklzxcvbnm0123456789":
            chare.append(ch)

    stillEqual = True

    while len(chare) > 1 and stillEqual:
        first = chare.pop()
        last = chare.pop(0)
        if first != last:
            stillEqual = False
    return stillEqual

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("OP"))