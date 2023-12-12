#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Final Assignment

Write a program to have the user enter in his or her first names, last names, social security number, date of birth, 
gender, weight, run date, and gross annual income.
If the gross annual is less than $11,500 the user will pay no income tax. 
If the user is 65 or older and his or her annual income is less than 18,000 the user will pay no income tax. 
If the gross annual income is under $45,000 and user is male under 25 years of age, weighs less than 200 pounds 
or the user is female under 27 years of age, weighs less than 125 pounds the rate of income tax will be 21%. 
If the gross annual income is under $45,000 and user is male under 45 years of age, weighs less than 220 pounds 
or the user is female under 47 years of age, weighs less than 135 pounds the rate of income tax will be 23%. 
If the user is under 55 years and the above conditions do not apply, the income tax rate will be 19%. 
Everyone else will pay 17%
The program will display the information on the screen in the following format:
Name: Last Names, First Initial Second Initial
Social Security Number: 999-99-9999 
Date of Birth: Month Day, Year
Gender 
Weight
Run Date: Month Day, Year
Gross Annual Income
Income Tax Rate
Total Income Tax
Total Net Pay
Be sure to complete all the edit checks for SSN, Gender, Weight, Gross Annual Income, and Dates. 
Also, please use functions for the date validation and the income tax calculations. Be sure your program is well documented.


# In[1]:


from datetime import datetime


# In[2]:


# validate date input
def validate_date(month, day, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


# In[3]:


# validate ssn input
def validate_ssn(ssn):
    try:
        if len(ssn) == 9 and ssn.isdigit():
            return True
    except ValueError:
        return False


# In[4]:


# validate weight and income input
def validate_weight(weight):
    return weight > 0

def validate_income(gross_income):
    return gross_income >= 0


# In[5]:


# calculate income tax
def income_tax_calculate(gross_income, age, gender, weight):
    if gross_income < 11500:
        income_tax = 0
    elif gross_income < 18000 and age > 64:
        income_tax = 0
    elif gross_income < 45000:
        if gender == 'M':
            if age < 25 and weight < 200:
                income_tax = 0.21 * gross_income
            elif age < 45 and weight < 220:
                income_tax = 0.23 * gross_income
        elif gender == 'F':
            if age < 27 and weight < 125:
                income_tax = 0.21 * gross_income
            elif age < 47 and weight < 135:
                income_tax = 0.23 * gross_income
    elif age < 55:
        income_tax = 0.19 * gross_income
    else:
        income_tax = 0.17 * gross_income
    return income_tax


# In[6]:


def annual_net_pay():
    print('Welcome to annual net pay calculate program!')
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    # input and check valid ssn
    ssn = input("Enter your Social Security Number (XXX-XX-XXXX): ")
    while not validate_ssn(ssn):
        print('Invalid SSN. Please enter a 9-digit number!')
        ssn = input("Enter your Social Security Number (XXX-XX-XXXX): ")
        
    # input and check dob
    dob = datetime.strptime(input("Enter your Date of Birth (MM/DD/YYYY): "), "%m/%d/%Y")
    while not validate_date(dob.month, dob.day, dob.year):
        print("Invalid Date of Birth")
        dob = datetime.strptime(input("Enter your Date of Birth (MM/DD/YYYY): "), "%m/%d/%Y")
    
    # input and check gender
    gender = input("Enter your gender (F/M): ").capitalize()
    if gender not in ('F','M'):
        print('Invalid Gender')
        gender = input("Enter your gender (F/M): ").capitalize()
    
    # input and check weight
    weight = float(input("Enter your weight in pounds: "))
    while not validate_weight(weight):
        print('Invalid Weight')
        weight = float(input("Enter your weight in pounds: "))
    
    # input and check gross income
    gross_income = float(input("Enter your Gross Annual Income: $"))
    while not validate_income(gross_income):
        print('Invalid Gross Annual Income')
        gross_income = float(input("Enter your Gross Annual Income: $"))
    
    # calculate age
    age = datetime.now().year - dob.year
    # rundate
    run_date = datetime.now()
    
    # calculate net income
    income_tax = income_tax_calculate(gross_income, age, gender, weight)
    net_income = gross_income - income_tax
    
    # display result
    print(f"Name: {last_name}, {first_name[0]} {first_name[1]}")
    print(f"Social Security Number: {ssn}")
    print(f"Date of Birth: {dob.strftime('%B %d, %Y')}")
    print(f"Gender: {gender}")
    print(f"Weight: {weight} pounds")
    print(f"Run Date: {run_date.strftime('%B %d, %Y')}")
    print(f"Gross Annual Income: ${gross_income:,.2f}")
    print(f"Income Tax Rate: {income_tax / gross_income * 100:.2f}%")
    print(f"Total Income Tax: ${income_tax:,.2f}")
    print(f"Total Net Pay: ${net_income:,.2f}")


# In[7]:


annual_net_pay()

