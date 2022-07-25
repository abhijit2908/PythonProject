def squaredSame(arr1,arr2):
    if len(arr1) != len(arr2):
        return "arrays not of same length"
    
    frequencyCounter1 = {}
    frequencyCounter2 = {}

    for val in arr1:
        if val in frequencyCounter1:
            frequencyCounter1[val] += 1
        else:
            frequencyCounter1[val] = 1    

    for val in arr2:
        if val in frequencyCounter2:
            frequencyCounter2[val] += 1
        else:
            frequencyCounter2[val] = 1

    for key,count in frequencyCounter1.items():
        if(key**2 not in frequencyCounter2):
            return False
        if(frequencyCounter2[key**2] != frequencyCounter1[key]):
            return False
    return True


squaredSame([1,2,3],[1,4,9])
squaredSame([1,2,4],[16,1,4])
squaredSame([1,2,3],[1,2])
squaredSame([1,2,3],[9,9,1])
