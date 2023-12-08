#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 1

Modify the code below to have the program first print a welcome statement to the user. 
Next the user will enter in the employee’s first and last names. 
After the hourly rate and hours worked have been entered, the gross pay will be calculated. 
Taxes will be calculated as follows: Federal tax at 13%, state tax at 7%, and social security at 3%. 
    Net pay is gross pay minus the taxes.

The information will be presented:

The payroll information for first name last name

Hours Worked: XX
Hourly Rate: XX.XX
Gross Pay: XXX.XX
Federal Tax: XXX.XX
State Tax: XXX.XX
Social Security: XXX.XX
Net Pay: XXX.XX

Thank you for using the Payroll Program!


# In[1]:


print('Welcome to the Payroll Program')


# In[2]:


input ( 'Enter your first name: ' )


# In[3]:


input ( 'Enter your last name: ' )


# In[8]:


hrs_work = int(input('Hours worked: '))


# In[9]:


payrate = float(input('Hourly Rate: '))


# In[17]:


gross_pay = hrs_work * payrate
print("Gross Pay: $%s" % gross_pay)


# In[24]:


fed_tax = gross_pay*0.13
print("Federal Tax: $%.2f" % fed_tax)


# In[25]:


state_tax = gross_pay*0.07
print("State Tax: $%.2f" % state_tax)


# In[26]:


social_sec = gross_pay*0.03
print("Social Security: $%.2f" % social_sec)


# In[28]:


net_pay = gross_pay - (fed_tax+state_tax+social_sec)
print("Net Pay: $%.2f" % net_pay)


# In[ ]:


print('Thank you for using the Payroll Program!')

