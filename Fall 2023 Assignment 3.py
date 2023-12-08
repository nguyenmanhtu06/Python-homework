#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 3

Write a program asking the user to enter in the weight of a package to be shipped. 
If the package weighs two pounds or less, the rate is $1.50 per pound. 
If the package is over 2 pounds, but not more than 6 pounds, the rate is $3.00 per pound. 
If the package is over six pounds, but less than 10 pounds, the rate is $4.00 per pound. 
If the package is 10 pounds or more, the rate $4.75. The program will display the shipping charges. 
When the program is first initiated, very explicit instructions will be given to the user.

Be sure your program is well documented.


# In[5]:


#Welcome
print('Welcome to Shipping Charge Program! Please enter the required information')


# In[1]:


#Package weight input
package_weight = float(input('Package weight in lbs: '))


# In[2]:


#Calculate the rate
rate = None
if package_weight <= 2.00:
    rate = 1.50
elif package_weight > 2.00 and package_weight <= 6.00:
    rate = 3.00
elif package_weight > 6.00 and package_weight < 10.00:
    rate = 4.00
else:
    rate = 4.75


# In[6]:


#Final output
shipping = package_weight*rate
print("Your shipping charge: $%.2f" % shipping)


# In[7]:


print('Thank you for using the Shipping Charge Program!')


# In[ ]:




