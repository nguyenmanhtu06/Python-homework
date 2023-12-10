#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 9
Write a Python program that asks the user to enter in his/her last name and social security number. 
If the SSN is not nine characters long or not all digits, make the user reenter it. 
The program will then ask the user to enter a number (n) from 1 to 25. 
If the entry is not numeric or out of range, the user will be asked to reenter it. 
The program will print a “user code” made up of the last letter of the name and the first, fifth, and ninth number of the SSN.

The program will contain a function that takes the integer n as a parameter. 
The method should print a pattern of 2n lines of asterisks. 
The first line contains one asterisk, the next line contains 2, and so on up to the nth line which contains n asterisks. 
Line number n+1 again contains n asterisks, the next line has n-1 asterisks, 
    and so on until line number 2n which has just one asterisk. Main should ask the user for the value of n. 

Below is an example of what would be displayed by the execution of the program.

Please enter your last name: Jones
Please enter your Social Security Number: 123456789
Please enter a digit from 1 to 25 (enter 99 to end program): 4

Your User ID is: s159

*
**
***
****
****
***
**
*

Please enter a digit from 1 to 25 (enter 99 to end program):

Be sure your program is well documented with meaningful inline comments. 
You must also provide an introduction clearly describing the program and include your name and the date.


# In[1]:


#create list of valid input numbers 
l25 = list(range(1, 26))
valid_num = []
valid_num = [i for i in valid_num] + [99] if 99 not in valid_num else valid_num
valid_num = valid_num + l25
valid_num


# In[2]:


#function to draw asterisk
def print_asterisk_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)
    for i in range(n, 0, -1):
        print('* ' * i)


# In[ ]:


#main function
def ssn_func():
    print('Welcome to the Social Security Number Program!')
    lastname = input('Please enter your last name: ')
    ssn = input('Please enter your SSN: ')
    while True:
        if len(ssn) != 9 or not ssn.isdigit(): #check that SSN input has 9 digits
            print('Invalid SSN. Please enter a 9-digit number!')
            ssn = input('Please enter your SSN: ')
        else:
            while True:
                n = int(input('Please enter a digit from 1 to 25 (enter 99 to end program): '))
                if n not in valid_num:
                    print('Invalid input. Please enter a number from 1 to 25 or 99!')
                    n = int(input('Please enter a digit from 1 to 25 (enter 99 to end program): '))
                elif n == 99:
                    print('Thank you for using our SSN Program. Goodbye!')
                    break
                else:
                    user_id = lastname[-1] + str(ssn)[0] + str(ssn)[4] + str(ssn)[-1]
                    print('Your User ID is:', user_id)
                    print_asterisk_pattern(int(n))
ssn_func()


# In[ ]:




