def checkPalindrome(inputString):
    reverseString = inputString[::-1]
    print(reverseString)
    if reverseString == inputString:
        return True
    else:
        return False


print(checkPalindrome('aabaa'))