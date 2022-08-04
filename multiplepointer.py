# sumZero([-3,-2,-1,0,1,2,3])
# sumZero([-4,-3,-2,-1,0,1,2,5])


def sumZero(arr1):
    left = 0
    right = len(arr1) - 1
    while(left < right):
        sum = arr1[left] + arr1[right]
        if sum == 0:
            print(arr1[left],arr1[right])
            return [arr1[left],arr1[right]]
        elif sum > 0:
            right -= 1
        elif sum < 0:
            left += 1
        else:
            return "we dont have a combo"            


sumZero([-3,-2,-1,0,1,2,3])
sumZero([-4,-3,-2,-1,0,1,2,5])