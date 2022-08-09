def areThereDuplicates(*arr):
    print(arr)
    dupCounter = {}

    for val in arr:
        if val in dupCounter:
            dupCounter[val] += 1
        else:
            dupCounter[val] = 1
    print(dupCounter)
    for val in dupCounter:
        print(val)
        if dupCounter[val]> 1:
            print("True")
            return True
    print("FALSE")
    return False


areThereDuplicates(1, 2, 3) #// false
areThereDuplicates(1, 2, 2) #// true 
areThereDuplicates('a', 'b', 'c', 'a') #// true