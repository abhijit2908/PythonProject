def sameFrequency(num1, num2):
    # // good luck. Add any arguments you deem necessary.
    if num1 < 0 or num2 < 0:
        return False
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) != len(num2):
        return False

    frequencyCounter1 = {}
    frequencyCounter2 = {}
    
    for val in num1:
        if val in frequencyCounter1:
            frequencyCounter1[val] += 1
        else:
            frequencyCounter1[val] = 1 

    for val in num2: 
        if val in frequencyCounter2:
            frequencyCounter2[val] += 1
        else:
            frequencyCounter2[val] = 1
    print(frequencyCounter1)
    print(frequencyCounter2)        

    for key in frequencyCounter1:
        if key not in frequencyCounter2  :
            return False
        elif frequencyCounter1[key] != frequencyCounter2[key]:
            return False
    print(num1,num2,"True")
    return True


sameFrequency(182,281)
sameFrequency(34,14)
sameFrequency(3589578, 5879385)
sameFrequency(22,222)