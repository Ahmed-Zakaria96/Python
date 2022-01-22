import os

# ask about the project
# task 1
def GenerateList(length, start):
    result = []
    for i in range(length):
        result.append(start)
        start += 1
    return result

print(GenerateList(4, 5))
print(GenerateList(6, 7))

os.system("pause")

# task 2
def FizzBuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        print("FIZZ BUZZ")
    elif x % 3 == 0:
        print("FIZZ")
    elif x % 5 == 0:
        print("BUZZ")

FizzBuzz(3)
FizzBuzz(5)
FizzBuzz(15)
os.system("pause")

# task 3
def strReversed(x):
    return x[::-1]

sInput = input("Enter a string: ")
print(strReversed(sInput))

os.system("pause")

# task 4
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")

sInput = input("Enter you name: ")
if len(sInput) > 0 and sInput.isalpha():
    data = {}
    data['name'] = sInput
    email = input("Enter your email: ")
    check(email)
    mobile = input("Enter your mobile: ")
    data['mail'] = email
    data['mobile'] = mobile

print(data)
os.system("pause")

# task 5
def LongestSub(s):
    start = 0
    end = 0
    l = len(s)
    maxSub = ""
    temp = ""
    for i in range(0, l-1):
        maxSub = temp if len(temp) > len(maxSub) else maxSub
        if s[i] < s[i+1]:
            end += 1
            temp = s[start: end+1]
        else:
            start = i
            end = i+1
    return maxSub if len(maxSub) > len(temp) else temp

input1 = input("Enter a string: ")
print(LongestSub(input1))

os.system("pause")

# task 6
numbersL = []
numSum = 0
count = 0
avg = 0

while (True):
    x = input("Enter a number: ")
    if x.isnumeric():
        numbersL.append(x)
        numSum += int(x)
        count += 1
    elif x == "done":
        break
print(f'Sum = {numSum} count = {count} avg = {numSum/count}')

os.system("pause")
# task 7
import random

words = ['ahmed', 'test', 'nice', 'wow', 'victory']

ranWord = random.choice(words)
wordL = len(ranWord)

userName = input("Enter your name: ")
i = 0
s = ['_'] * wordL
print(s)
print(ranWord)
correct = wordL
while (i < 7):

    guess = input("Enter your guess: ")
    if len(guess) > 0:
        if guess == ranWord:
            print("Victory")
            break
        indices = [index for index, element in enumerate(ranWord) if element == guess]
        for i in indices:
            if i >= 0:
                s[i] = guess
                wordL -= 1
        if wordL == 0:
            print("Victory")
            break
        print(s)
    i+=1
