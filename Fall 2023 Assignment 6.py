#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 6

Write a program in Python that prompts the user to enter in an amount of money in a savings account 
    that earns compound monthly interest, and the program will calculate the amount that you will have 
        after a specific number of months. The formula is as follows:

F = P * (1 + i)^t

The terms in the formula are:

•	F is the future value of the account after the specified time period
•	P is the present value of the account
•	i is the monthly interest rate
•	t is the number of months

The program will prompt the user to enter in the account’s present value, monthly interest rate, 
    and the number of months that the money will be left in the account. 
The program should pass these values to a function that returns the future value of the account, 
    after the specified number of months. 
The program will display the account’s future value.

The user can rune the program as often as he/she wants.

Be sure your program is well documented and is user friendly with very clear instructions to the user.


# In[13]:


def future_account():
    print('Welcome to Monthly Single Payment Compound Interest Program!')
    P = float(input('Enter your account value at present: '))
    interest_percent = float(input('Enter the monthly interest rate: '))
    i = interest_percent/100
    t = float(input('Enter the number of months: '))
    F = None
    def future_value(P,i,t):
        F = P * (1 + i)**t
        return print('Your account’s future value is: $%.2f'%F)
    future_value(P,i,t)


# In[14]:


future_account()


# In[ ]:




