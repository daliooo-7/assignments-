"""
Dalio Benavidez Jr.
Assignment 2
Intro to Scripting
2-8-2022
"""
ROW_SIZE = 5 #declare range of how many stars

for x in range(ROW_SIZE): #for loop
    for r in range(x+1): # for loop that adds a star per row
        print("*", end = ' ') # prints pattern
    print()

C_SIZE = 5 #declare range of how many stars
b = 2*C_SIZE - 2  #operation that flips the pattern
for a in range(C_SIZE): # for loop
    for c in range(b):
        print(end=' ')
    b = b - 2 #operation that subtracts to percieve a flipped pattern
    for c in range(a+1): #for loop that adds star per row
        print("*", end = ' ') # prints patter
    print()

# question 2
print()

num1 = int(input("Enter n number: ")) # asks user to input n
num2 = int(input("Enter r number: ")) # asks user to input r
num3 = num1 - num2 # operation that subtracts n and r

loop_counter_1 = 1 # counter
result_fact_number = 1 # sets result first to 1
while loop_counter_1 <= num1: # while loop
    result_fact_number = result_fact_number *loop_counter_1 # operation that multiplies the counter by result number
    loop_counter_1 += 1 # increments the loop counter by 1

loop_counter_2 = 1 # counter
result_fact_number2 = 1 # sets result first to 1
while loop_counter_2 <= num2: # while loop
    result_fact_number2 = result_fact_number2 *loop_counter_2 # operation that multiplies the counter by result number
    loop_counter_2 += 1  # increments the loop counter by 1

loop_counter_3 = 1  # counter
result_fact_number3 = 1 # sets result first to 1
while loop_counter_3 <= num3: # while loop
    result_fact_number3 = result_fact_number3 *loop_counter_3 # operation that multiplies the counter by result number
    loop_counter_3 += 1 # increments the loop counter by 1
print("Perm form: ", result_fact_number / result_fact_number3) # formula for permutations form and prints
print("combo form: ", result_fact_number / (result_fact_number2*result_fact_number3)) # formula for combinations form and prints


#problem 3
print()
list = [20, 68, 41, 88, 16, 40, 65, 97, 85]
i = 0

for i in range(i,len(list)): # sets i in range of the list
    for j in range(i +1, len(list)): # sets j in range and adds i by 1, will sort
        if (list[i] > list[j]): # conditional statement
            temp = list[i] # creates temporary list
            list[i] = list[j] # sets sorted list to list[i]
            list[j] = temp # sets temp list to list[j]

print("Sorted numbers in the list:", list) # prints sorted list

#problem 4
print()
list2 = [2, 8, 4, 88, 3, 66, 75, 99, 21]
loopCount = 0
sum = 0
total = 0

for i in range(sum, len(list2)): # sets i in range of list
    sum = sum + list2[i] # adds the numbers of list together
print("Sum of numbers in list 2:", sum) # prints the sum

print()

print("Even numbers in list 2: ")

while loopCount < len(list2): # goes through list
   if list2[loopCount] % 2 == 0: # checks if number in list is even
        print(list2[loopCount], end =" ") # prints the even numbers
   loopCount+= 1 # increments loop count

print()

print("Odd numbers in list 2: ")

for num in list2: # for loop that checks every number in list
    if num  % 2 == 1: # checks if number is odd
        print(num, end =" ") # prints odd numbers

print()

print("Sum off odd numbers: ")

total = 0
for a in range(0,len(list2)): # check size of list
    if list2[a] % 2 == 1: # check if it is odd 
        total = total + list2[a] # adds sum
        i+=1
print(total, end = "") #prints odds

print()

print("Sum off even numbers: ")

for b in range(0, len(list2)):  # check size of list
    if list2[b] % 2 == 0: # checks if it is even
        total = total + list2[b] # adds sum
print(total, end ="") # prints evens

print()
print()

#question 5
first = 2 # first number
last = 50 # last number

print("Prime numbers are: ")

for num in range(first, last + 1): # for loop that goes through every number 2 through 50
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0: # checks if number is prime
               break
       else:
           print(num, end = " ") # prints prime numbers

print()
print()

#question 6
def function1(): # function
    numN = num1 # correlates num1 to new variable
    numR = num2 # correlates num2 to new variable
    print("N and R:", numN, "and", numR) # prints N and R

function1()

def function2(): # function
    funList = list # correlates list to new variable
    print("List in function:", funList) # prints the list by new varible

function2()

#bonus question 8
print()

def fibonacci():
    Fnum = int(input("Enter a number: ")) # asks user for number
    i = 0
    val = 0
    val2 = 1

    while i < Fnum:
        print(val, end =" ") # prints the fibonacci numbers
        Folval = val + val2 # addition operation
        val = val2 # current and the following value and the sum set to following value
        val2 = Folval # assigns it to following value
        i += 1 # increments by 1

fibonacci()

# bonus question 9
print()
print()
print("Corrected code that prints even numbers: ")
loop_counter = 1

while loop_counter <= 10:
    if loop_counter % 2 == 0:
        print(loop_counter)
    loop_counter += 1
# all i did was remove the first print statement
