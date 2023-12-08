#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 2

Write a program that asks the user to enter in the number of shares of stock that the user will buy at $43.00 per share 
and then the user will sell two months later at $37.75 per share.
The commission to be paid to the stockbroker is 3.4% when the user buys the stock and 3.7% when the user sells the stock.
Use a constant for the commission rate.
The program will calculate how much the user will pay for the stock at the time of purchase, 
    how much commission will be paid at the time of purchase, how much the stock will be sold for, 
    the amount of commission paid at the time of sale, gross profit, and the net profit the user will receive.

After printing instructions to the user, the information will be entered:

Please enter the number of shares purchased; XXXX
Cost of the purchase of the stock: XXXX.XX
Amount of commission paid: XXX.XX
Total amount to be paid to the user at time of purchase: XXXX.XX
Sale price of the stock: XXXX.XX
Amount of commission paid: XXX.XX
Amount received by the user: XXXX.XX
Net profit/loss: XXXX.XX

Thank you for using the Stock Purchase Program!

Make sure the instructions to the user are very clear, the variable names very relevant, the program description clear, 
and there are in-line comments. 

Due Sunday, September 17, 2023


# In[1]:


#Welcome
print('Welcome to the Stock Purchase Program!')


# In[2]:


#declares constant variables
purchased_price = 43.00
sold_price = 37.75
purchased_comm_rate = 0.034
sold_comm_rate = 0.037


# In[3]:


#number of shares purchased
purchased_shares = int(input('Please enter the number of shares purchased: '))


# In[4]:


#Cost of the purchase
purchased_cost = purchased_shares*purchased_price
print("Cost of the purchase of the stock: $%s" % purchased_cost)


# In[6]:


#Amount of commission
purchased_comm = purchased_cost*purchased_comm_rate
print("Amount of commission paid: $%.2f" % purchased_comm)


# In[7]:


#Total amount to be paid to the user at time of purchase
total_purchased = purchased_cost+purchased_comm
print("Total amount to be paid to the user at time of purchase: $%.2f" % total_purchased)


# In[8]:


#Sale price
sold_rev = purchased_shares*sold_price
print("Sale price of the stock: $%.2f" % sold_rev)


# In[9]:


#Amount of commission paid
sold_comm = sold_rev*sold_comm_rate
print("Amount of commission paid: $%.2f" % sold_comm)


# In[11]:


#Amount received by the user
received = sold_rev - sold_comm
print("Amount received by the user: $%.2f" % received)


# In[14]:


#Net profit/loss
net = received - total_purchased
if net < 0.00:
    print("Net loss: $%.2f" % net)
elif net > 0.00:
    print("Net profit: $%.2f" % net)
elif net == 0.00:
    print("Break even")


# In[15]:


#Farewell
print('Thank you for using the Stock Purchase Program!')


# In[ ]:




