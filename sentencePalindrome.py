import string

def sentencePalindrome(x):
    x = x.translate(str.maketrans('', '', string.punctuation))
    x = x.replace(" ","")
    return x.casefold() == x[::-1].casefold()

sentence = input("Please enter sentence for palindrome check ")
if sentencePalindrome(sentence):
    print("'{}' is a palindrome ".format(sentence))
else:
    print("'{}' is not palindrome ".format(sentence))
