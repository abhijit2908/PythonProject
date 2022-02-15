def palindrome(x):
    return x[::-1].casefold() == x.casefold()


word = input("please enter a word to check if its Palindrome ")
if palindrome(word):
    print("'{}' is a Palindrome".format(word))
else:
    print("'{}' is not a Palindrome".format(word))