def validAnagram(str1,str2):
    if len(str1) != len(str2):
        return "string not of same length"
    
    frequencyCount1 = {}
    frequencyCount2 = {}

    for char in str1:
        if char in frequencyCount1:
            frequencyCount1[char] += 1
        else:
            frequencyCount1[char] = 1
    
    for char in str2:
        if char in frequencyCount2:
            frequencyCount2[char] += 1
        else:
            frequencyCount2[char] = 1

    for key,value in frequencyCount1.items():
        print(key, value)
        if key not in frequencyCount2.keys():
            return False
        if frequencyCount1[key] != frequencyCount2[key]:
            return False

    return True





validAnagram('','')
validAnagram('aaz','zza')
validAnagram('anagram','nagaram')
validAnagram('rat','car')
validAnagram('awesome','awesom')