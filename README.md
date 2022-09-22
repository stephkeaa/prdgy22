# Week 1 - CS Concepts

## 1 - variables

given the string city = 'Baltimore' write the code

to print out the 4th character in the string

to print out the last character in the string

to print out a slice of the first 4 characters in the string


## 2 - conditionals

Write a code that will ask the user to enter an integer and checks if it is even or odd. Save it in a file called is_even.py

Write a code that will ask the user to enter their annual income and returns their federal tax bracket and how much they would pay in taxes. save the script in a file called taxes.py

10% <- $0 to $9,950
12% <- $9,951 to $40,525
22% <- $40,526 to $86,375
40% <- $86,376 or above


## 3 - Loops

Write a program that will ask the user to input a password. If the password entered is correct, the code should exit with a welcome message. Otherwise, it should ask the user to enter the password again up-to 3 times, after which, it should exit with an error message. save the script in a file called password.py

Write a program that will take a word input from user then prints out the word without it's vowels. save the script in a file called vowels.py

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hint: Consider using range(#begin, #end) method


## 4 - Data Structures

Given a list of numbers. write a program to turn every item of a list into its square.

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers2 = []

for i in numbers:
numbers.append(i**2)


Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Concatenate two lists in the following order to create list3
list1 = ["Hello ", "Thank you "]
list2 = ["Dear", "Sir"]
list3 = ['Hello Dear', 'Hello Sir', 'Thank you  Dear', 'Thank you  Sir']

Edit the file wordCount.py to create a program that will take a paragraph and stores it into a dictionary with the words from the paragraph as the keys and the number of instances of the word as the values
example:
input >>> "I be flying high, shawty, I be flying high I be flying high, shawty, I be flying high I be flying high, shawty, I be flying high"
output >>> {'I': 6, 'be': 6, 'flying': 6, 'high': 6, 'shawty': 3}
