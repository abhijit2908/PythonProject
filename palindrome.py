def palindrome(x):
    return x[::-1].casefold() == x.casefold()


word = input("please enter a word to check if its Palindrome ")
if palindrome(word):
    print("'{}' is a Palindrome".format(word))
else:
    print("'{}' is not a Palindrome".format(word))


def palindrome2(x):
    for i in range(0,int(len(x)/2)):
        if x[i].casefold() != x[len(x)-1-i].casefold():
            return False
    return True


word = input("please enter a word to check if its Palindrome ")
if palindrome2(word):
    print("'{}' is a Palindrome".format(word))
else:
    print("'{}' is not a Palindrome".format(word))
