#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 5

Write a program that asks the user if he or she would like to play Powerball. 
If the answer is yes, ask the user to enter his or her first, middle, and last names. 
Generate five random numbers (using the randint function) from 5 to 69 and one random number from 1 to 26. 
Of the first five random numbers, no two can have the same value. 
Present the information as: last name, first initial, middle initial The Winning Powerball Numbers Are: XX XX XX XX XX   XX
A function will be called from main with the six numbers being sent to the function as its argument, 
    and the function will return the sum of the six numbers, and the sum will printed with the appropriate message.
The user will be given the option to play again, otherwise go to end of job.
The program should be very user friendly and the code should be well documented. Be very thorough with your edit checks.


# In[1]:


import random


# In[12]:


def powerball():
    start = input('Welcome to Powerball! Would you like to play? (Yes/No) ')
    while True:
        if start == 'Yes' or start == 'yes':
            firstname = input('Your first name: ')
            middlename = input('Your middle name: ')
            lastname = input('Your last name: ')
            list5 = []
            for i in range(1, 6):
                if i not in list5:
                    list5.append(random.randint(5,70))
            last_num = random.randint(1,27)
            result = " ".join(str(num) for num in list5) + "   " + str(last_num)
            print(lastname + ", " + firstname[0] + ", " + middlename[0] + ", " + "The winning Powerball Numbers Are: " + result)
            list6 = []
            list6.append(last_num)
            list6 = list6+list5
            def sum_number(list6):
                return sum(list6)
            print('Your total Powerball is: ' + str(sum_number(list6)))
            start = input('Welcome to Powerball! Would you like to play? (Yes/No) ')
        elif start == 'No' or start == 'no':
            print('See you later then!')
            break


# In[ ]:




