#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Mid Term Assignment

Write a program that allows the user to process the hourly payroll for any number of employees including zero. 
The user will be asked “Would you like to calculate a weekly paycheck? Enter Y or N.”  
If “Y” is entered, the user will be instructed to enter the first name, last name and date of birth of the employee. 
The program will then execute a date validation function. 
Month, day, and year variables will be passed to the date validation function from main, 
and if the date is valid, Boolean “true” will be returned. 
If the date is invalid, “false” will be returned to main, and the user will be instructed to reenter the date of birth. 
Next, the hours worked and the hourly pay rate will be entered. These figures have to be greater than zero. 
You will establish a reasonable high limit for the hours (example: 80 hours), 
and should the user enter a higher number of hours, he/she will be asked to enter a valid number of hours. 
Hours worked in excess of 40 hours will be paid time and a half. Gross pay will then be calculated. 
Gross pay will be passed to a function and federal income tax will be returned.

Federal income tax will be calculated as follows. The annual pay will be determined by multiplying gross pay by 52. 
If the annual pay is less than $15,000, the tax rate is zero. 
If the annual pay is between $15,000 and $24,999, the tax rate is 7%. . 
If the annual pay is between $25,000 and $49,999, the tax rate is 12%.  
If the annual pay is between $50,000 and $74,999, the tax rate is 15%.  
If the annual pay is greater than $75,000, the tax rate is 20%. 
The federal income tax will be calculated by multiplying the gross pay by the appropriate tax rate, 
and that figure will be returned to main where net pay will be calculated by subtracting the federal income tax from gross pay.

The employee payroll information will be presented exactly as follows:

Employee Name: Smith, John
Employee DOB: 11/15/1981
Hours Worked: 44
Pay Rate: $15.00
Gross Pay: $690
Federal Tax: $82.80
Net Pay: $607.20

Be sure you program is well documented with comments. Use good program structure as well as meaningful variable names. 
Write a welcome message and thank the user for using the program when the program is terminated.


# In[1]:


from datetime import datetime


# In[2]:


# date input validation
def validate_date_input(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


# In[3]:


# tax calculation
def calculate_tax(gross_pay):
    annual_pay = gross_pay * 52
    if annual_pay < 15000:
        tax_rate = 0
    elif 15000 <= annual_pay <= 24999:
        tax_rate = 0.07
    elif 25000 <= annual_pay <= 49999:
        tax_rate = 0.12
    elif 50000 <= annual_pay <= 74999:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
    federal_tax = gross_pay * tax_rate
    return federal_tax


# In[4]:


def weekly_paycheck():
    start = input('Would you like to calculate a weekly paycheck? Enter Y or N: ')
    while True:
        if start == 'Y' or start == 'y':
            firstname = input('Employee first name: ')
            lastname = input('Employee last name: ')
            dob_day = int(input('Enter employee date of birth - day: '))
            dob_month = int(input('Enter employee date of birth - month: '))
            dob_year = int(input('Enter employee date of birth - year: '))
            
            # Date input validation
            while not validate_date_input(dob_day, dob_month, dob_year):
                print("Invalid date. Please enter a valid date.")
                dob_day = int(input('Enter employee date of birth - day: '))
                dob_month = int(input('Enter employee date of birth - month: '))
                dob_year = int(input('Enter employee date of birth - year: '))
            
            # Work hours not more than 80 per week    
            hours_worked = float(input("Enter the hours worked (greater than 0): "))
            while hours_worked <= 0 or hours_worked > 80:
                print("Invalid input. Please enter hours between 0 and 80.")
                hours_worked = float(input("Enter the hours worked (greater than 0): "))
            hourly_pay_rate = float(input("Enter the hourly pay rate (greater than 0): "))
            
            # Pay rate not 0
            while hourly_pay_rate <= 0:
                print("Invalid input. Please enter a pay rate greater than 0.")
                hourly_pay_rate = float(input("Enter the hourly pay rate (greater than 0): "))
            
            # Over Time pay
            if hours_worked > 40:
                gross_pay = (40 * hourly_pay_rate) + ((hours_worked - 40) * 1.5 * hourly_pay_rate)
            else:
                gross_pay = hours_worked * hourly_pay_rate
            
            # Calculate fed tax
            federal_tax = calculate_tax(gross_pay)
            # Calculate net pay
            net_pay = gross_pay - federal_tax
            # Print results
            print("\nEmployee Payroll Information:")
            print(f"Employee Name: {lastname}, {firstname}")
            print(f"Employee DOB: {dob_month}/{dob_day}/{dob_year}")
            print(f"Hours Worked: {hours_worked}")
            print(f"Pay Rate: ${hourly_pay_rate:.2f}")
            print(f"Gross Pay: ${gross_pay:.2f}")
            print(f"Federal Tax: ${federal_tax:.2f}")
            print(f"Net Pay: ${net_pay:.2f}\n")
            
            # Continue?
            print('Would you like to keep going?')
            start = input('Would you like to calculate a weekly paycheck? Enter Y or N: ')
        # Break
        elif start == 'N' or start == 'n':
            print('See you later then!')
            break

weekly_paycheck()


# In[ ]:




