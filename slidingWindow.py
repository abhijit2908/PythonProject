from signal import valid_signals


def maxSubarraySum(arr,num):
    if num > len(arr):
        return "array smaller than length of window"

    maxSum = 0
    tempSum = 0
    for val in range(0,num):
        maxSum += arr[val]

    tempSum = maxSum
    for val in range(num,len(arr)):
        tempSum = tempSum - arr[val-num] + arr[val]
        if tempSum > maxSum:
            maxSum = tempSum
    return maxSum


maxSubarraySum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3)        
