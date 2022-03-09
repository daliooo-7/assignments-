#question 1

MORSE_CODE_DICTIONARY = { 'A':'.-', 'B':'-...', # correlates morse code in a list
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}

string=input('Enter a string to convert to Morse code:') # asks user to enter a string
morse_string = ""

for i in string: # for loop that checks user input for morse code
  if i==' ':
      morse_string+=' '
  elif i in MORSE_CODE_DICTIONARY:
      morse_string += MORSE_CODE_DICTIONARY[i]

print(morse_string)
print()

#question 2

def vowel(string): # defines vowels
    vowels = "AaEeIiOoUu"
    c = 0
    for s in string:
        if s in vowels:
            c += 1
    return c

def cons(string2):
    vowels = "AaEeIiOoUu" # defines vowels
    c = 0
    for s in string:
        if s not in vowels:
            c += 1
    return c


string=input("Enter a String : ") # asks user to enter a string
v=vowel(string); # identifies vowels in string
print("\nNumber vowels :",v)
c=cons(string); # identifies consonants in string 
print("Number of consonants :",c)

print()

#question 3a

str1 = "P@#yn26at^&i5ve"
char_count = 0
digit_count = 0
symbol_count = 0
# ch holds each character in String str1 for every iteration of loop
for ch in str1: # ch holds each character in String str1 for every iteration of loop
    if(ch.isalpha()):     # if character is alphabet
        char_count = char_count + 1
    elif(ch.isdigit()): # if character is digit
        digit_count = digit_count + 1
    else: # if character is symbol
        symbol_count = symbol_count + 1

print("Total counts of chars,digits and symbols")
print("Chars = ",char_count," Digits = ",digit_count," Symbols = ",symbol_count)
print()

#question 3b
str1 = "/*Jon is @developer & musician"
newStr = str1[:0] + str1[2:] # appends the new strings together
newStr1 = newStr[:7] + newStr[8:]
newStr2 = newStr1[:17] + newStr1[18:]
print("")
print("Before:", str1)
print("After:",newStr2)
print()

#question 3c
str1 = "Emma-is-a-data-scientist"
str2 = str1[0:4] + " " + str1[5:7] + " " + str1[8:9] + " " + str1[10:14] + " " + str1[15:24] # appends new strings together
print("")
print(str2)
print()

#question 3d
lst = ["a", "e","i","o","u","y", " "]
str1 = "Hello, have a good day"
str1 = str1.lower()
for i in str1: # for loop that goes through list to find syllables
    if i not in lst:
        str1 = str1[:str1.index(i)]+str1[str1.index(i)+1:]
print("")
print(str1)
print()

#question 4
def main():

    n = int(input("\nHow many integers would you like to enter? "))  #prompts user to enter integers

    while n <= 10: # while loop that validates
        n = int(input("Invalid input. Please enter a number greater than 10: "))

    list_part_1 = [] # created list
    list_1_sum = 0

    for num in range(0,n):
        int_input = int(input("Enter an integer from 0 to 100: "))
        while int_input < 0 or int_input > 100:
            int_input = int(input("Invalid input. Please enter a integer from 0 to 100: "))
        list_part_1.append(int_input)
        list_1_sum += int_input

    list_avg = list_1_sum/n # average

    for temp in range(0, n): # for loop that sorts
        for temp2 in range(temp + 1, n):
            if list_part_1[temp] > list_part_1[temp2]:
                list_part_1[temp], list_part_1[temp2] = list_part_1[temp2], list_part_1[temp]


    if n % 2 == 0:     #subjects the median
        median_left = list_part_1[n//2]
        median_right = list_part_1[n//2 - 1]
        median = (median_left + median_right)/2
    else:
        median = list_part_1[n//2]

    temp2 = 0 # searches deviation
    for temp in list_part_1:
        temp2 += (temp-list_avg)**2
    variance = temp2 / n
    standard_dev = variance**0.5

    print("\nOrdered List:", list_part_1)
    print("List Average:", list_avg)
    print("Median:", median)
    print("Standard Deviation:", standard_dev)
    print()

    list_part_2 = [] #new list

    for num in range(0,n-1): # for loop
        try:
            list_part_2.append(list_part_1[num] / list_part_1[num+1])
        except:
            list_part_2.append("N/A")

    print("Division of elements:")
    print(list_part_2, "\n")

if __name__ == '__main__': # runs main
    main()
