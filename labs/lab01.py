import os
# task 1
vowels = ['a', 'e', 'i', 'o', 'u']

sOne = "Ahmed Zakaria Ali Ahmed"

vowelsCount = 0
for i in sOne:
    if i.lower() in vowels:
        vowelsCount += 1

print(f"Vowels count in '{sOne}' is {vowelsCount}")

os.system("pause")
# task 2
sOne = []

for i in range(1, 6):
    sOne.append(input(f"Enter element number {i}: "))

sOne.sort(reverse = True)
print(sOne)
sOne.sort()
print(sOne)

os.system("pause")

# task 3
subString = "iti"
sInput = input("Enter string:")
inputLen = len(sInput)
itiCount = sInput.count(subString, 0, inputLen)
print(f"iti Count is {itiCount}")

# or 
itiCount = 0
i = 0
while i < inputLen:
    temp = sInput[i:i+3]
    if temp == "iti":
        itiCount +=1
        i += 3
        continue
    i+=1

print(f"iti count method 2 is: {itiCount}")

os.system("pause")

# task 4
sInput = input("Enter string:")
inputLen = len(sInput)
newStr = ""
for i in sInput:
    if i.lower() not in vowels:
        newStr += i
print(f"Vowels deleted {newStr}")

# task 4
char = input("Enter char to look for: ")
indexList = []
sInput = input("Enter string to search at: ")
inputLen = len(sInput)
for i in range(0, inputLen):
    if char == sInput[i]:
        indexList.append(i)

print(indexList)

os.system("pause")

# task 5 
nInput = int(input("Enter number: "))
result = []
for i in range(1, nInput+1):
    result.append([])
    for j in range(1, i+1):
        result[i-1].insert(j-1, j*i)

print(result)

os.system("pause")

# task 6
height = int(input("Enter height"))
for i in range(0, height):
    for j in range(0, height):
        if i + j < height-1:
            print(" ", end='')
        else:
            print("*", end="")
    print()