"""
Author: Dalio Benavidez Jr.
Intro to Scripting
Date: 2/17/22
"""

# question 2

list = []
x = 20

for i in range(0, x): # loop from 0 to 20
    print("Enter number:")
    number = int(input()) # prompts user to enter number
    list.append(number) # adds number

print("Lowest:", min(list)) # displays lowest, highest, sum, and average
print("Highest:", max(list))
print("Sum of the numbers:", sum(list))
print("Average:", sum(list)/len(list))

#question 3

n = int(input("Enter number:")) # asks user to input number
r = { x : x * x for x in range(1, n+1)} #for loop the increments n by 1

print(r) # prints r

#question 4

import random

rList = []

for i in range(100): # for loop
    a = random.randint(0,20) # takes random number
    rList.append(a) # adds number to list

print("List:") # prints list
print(rList)

secondLargest = rList[0]
largest = rList[0]

for i in range(len(rList)): # for loop that runs the length number
    if rList[i] > largest: # if statement
        largest = rList[i]

for i in range(len(rList)): # for loop that runs the length number
    if rList[i] > secondLargest and rList[i] != largest: # if statement
        secondLargest = rList[i]

print("The second largest number in the list is:") #prints result
print(secondLargest)

k = 0

temp = len(rList) # stores length of list in temp

while k < temp: # while statment
    j = k + 1
    while j < temp:
        if rList[k] == rList[j]:
            del rList[j]
            temp = temp - 1
        else:
            j += 1
    k += 1

print("List after deletion:") # prints result 
print(rList)
