def countUniqueValues(arr1):
    if len(arr1) == 0:
        return 0
    
    i = 0    
    j = i+1
    while j < len(arr1):
        if arr1[i] != arr1[j]:
            i += 1
            arr1[i] = arr1[j]
        j += 1
    print(i+1)
    return i+1


countUniqueValues([1, 1, 1, 1, 2])