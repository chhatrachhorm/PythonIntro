import random
import sys
import os

# Control flow in python
age = 21
# if else
if age > 16 :
    print('Welcome to High School')
else :
    print('Not yet')
# if else ladder
if age >= 21:
    print('Let\'s go to college')
elif age >= 16:
    print('Welcome to High School')
# for loop

for x in range(0, 10):
    print(x , " " , end="")
print()
for x in range(0, 3):
    for y in range(0, 3):
        print(x, y)

random_num = random.randrange(0, 100)
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)

# define a function
def addNumber(fNum, lNum):
    return fNum + lNum
print("Calling addNumber: ", addNumber(52, 12))

# getting  input

name = sys.stdin.readline()
print('Hello', name)
