def averagePair(arr,num):
    if len(arr) == 0:
        print("False")
        return False

    left = 0
    right = arr.length -1
    while(arr[left]<arr[right]):
        if float((arr[left]+arr[right])/2)<num:
            left += 1
        elif float((arr[left]+arr[right])/2)>num:
            right -= 1
        else:
            return True
    return False



averagePair([1, 2, 3], 2.5) #// true
averagePair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8) #// true
averagePair([-1, 0, 3, 4, 5, 6], 4.1) #// false
averagePair([], 4) #// false