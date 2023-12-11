#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 10
Write a Python program to determine the number of days between two given dates. 
The user will first be asked to enter his or her social security number and after validating the format, 
    for security reasons, the SSN will be displayed on the screen in reverse order. 
The program will ask the user to enter both a start date and an end date. 
After checking that the dates are valid, the program will check to ensure that the start date is earlier than the end date. 
The dates will be entered in numeric format (i.e. October 12, 1998 would be entered 12 10 1998). 
Use an int function to determine the number of days between the dates. 
The process will be repeated until the user enters zeros for the start month.
The program will have a string function to convert the start and end months to alphabetic 
    after the number of days between the dates have been calculated. 
If the user had entered in a start date of 16 04 2002 and an end date of 19 06 2003 the program would display:
“The number of days between April 16, 2002 and June 19, 2003 is 429.”
For this assignment you can ignore leap years.
The program should use proper style and indentation, meaningful identifiers, 
and appropriate comments including name of programmer and the date. 
There will be very explicit instructions to user. 
Check for data errors such as incorrect month and a day number that is out of range.


# In[1]:


from datetime import datetime


# In[2]:


# SSN input and validation check
def reverse_ssn():
    ssn = input('Please enter your SSN: ')
    while True:
        if len(ssn) != 9 or not ssn.isdigit(): #check that SSN input has 9 digits
            print('Invalid SSN. Please enter a 9-digit number!')
            ssn = input('Please enter your SSN: ')
        else:
            return print('For security reasons, your SSN will be displayed in reverse order: ' + ssn[::-1])


# In[3]:


# date input validation
def validate_date_input(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


# In[4]:


# calculate days between input dates
def days_between_dates (start_date, end_date):
    start_datetime = datetime(*start_date)
    end_datetime = datetime(*end_date)
    daydiff = end_datetime - start_datetime
    return daydiff.days


# In[5]:


# convert numeric month to alphabetic using index of list. e.g: month number = 1, return 1 - 1 = index 0 of list
def convert_to_alphabetic(month):
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    return months[month - 1]


# In[ ]:


def days_calculate():
    print("Welcome to the Days Between Dates Calculator Program!")
    while True:
        reverse_ssn() #input SSN
        # input start date
        start_day = int(input("Enter the start day (numeric): "))
        start_month = int(input("Enter the start month (numeric): "))
        start_year = int(input("Enter the start year (numeric): "))
        # validate start date
        while not validate_date_input(start_day, start_month, start_year):
            print("Invalid start date. Please enter a valid date.")
            start_day = int(input("Enter the start day (numeric): "))
            start_month = int(input("Enter the start month (numeric): "))
            start_year = int(input("Enter the start year (numeric): "))
        # input end date
        end_day = int(input("Enter the end day (numeric): "))
        end_month = int(input("Enter the end month (numeric): "))
        end_year = int(input("Enter the end year (numeric): "))
        # validate end date
        while not validate_date_input(end_day, end_month, end_year):
            print("Invalid end date. Please enter a valid date.")
            end_day = int(input("Enter the end day (numeric): "))
            end_month = int(input("Enter the end month (numeric): "))
            end_year = int(input("Enter the end year (numeric): "))
        # check if start date is earlier than end date
        start_date = [start_year, start_month, start_day]
        end_date = [end_year, end_month, end_day]
        if start_date >= end_date:
            print("Error: Start date must be earlier than end date. Please enter valid dates.")
            continue
        # Calculate days between dates
        days_between = days_between_dates(start_date, end_date)       
        # Convert months to alphabetic
        start_month_alphabet = convert_to_alphabetic(start_month)
        end_month_alphabet = convert_to_alphabetic(end_month)
        # Display result
        print(f"The number of days between {start_month_alphabet} {start_day}, {start_year} and {end_month_alphabet} {end_day}, {end_year} is {days_between}.")
        # Ask if the user wants to continue
        continue_flag = input("Enter '0' for the start month to exit, or any other number to continue: ")
        if continue_flag == '0':
            print("Bye!")
            break

days_calculate()


# In[ ]:




