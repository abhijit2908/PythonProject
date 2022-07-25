# testFile = open("/Users/abhijitghosh/downloads/sample-text-file.txt")

# for line in testFile:
#     print(line)

# testFile.close()

# with open("/Users/abhijitghosh/downloads/sample-text-file.txt",'r') as testFile2:
#     line = testFile2.readline()
#     while line:
#         print(line, end='')
#         line = testFile2.readline()


# with open("/Users/abhijitghosh/downloads/sample-text-file.txt",'r') as testFile3:
#     line = testFile3.readlines()
#     print(line)


# with open("/Users/abhijitghosh/downloads/sample-text-file.txt",'r') as testFile3:
#     line = testFile3.read()
#     print(line)


# with open("/Users/abhijitghosh/downloads/sample-text-file.txt",'w') as testFile3:

with open("/Users/abhijitghosh/downloads/sample-text-file.txt",'a') as testfile4:
    for i in range (1,12):
        print(i*2, file=testfile4)