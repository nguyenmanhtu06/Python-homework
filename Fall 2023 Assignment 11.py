#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 11
Write a program in Python that will compute the date of Easter Sunday. 
Easter Sunday is the first Sunday after the first full moon of spring. 
To find Easter’s date, use an algorithm developed by the mathematician Carl Friedrich Gauss in 1800.  
1. Let y be the year; e.g.  1800, 1975 or 2014. 
2. Divide y by 19 and call the remainder a. Ignore the quotient.  
3. Divide y by 100 to get a quotient b and remainder c. 
4. Divide b by 4 to get a quotient d and remainder e 
5. Divide (8 * b + 13) by 25 to get quotient g. Ignore the remainder. 
6. Divide (19 * a + b – d – g + 15) by 30 to get remainder h. Ignore the quotient. 
7. Divide c by 4 to get the quotient j and remainder k. 
8. Divide (a + 11 * h) by 319 to get quotient m. Ignore the remainder. 
9. Divide (2 * e + 2 * j – k – h + m + 32) by 7 to get remainder r. Ignore the quotient. 
10. Divide (h – m + r + 90) by 25 to get quotient n. Ignore the remainder. 
11. Divide (h – m + r + n + 19) by 32 to get remainder p.  Ignore the quotient. 
The result is that Easter falls on day p of month n in the given year. 
For example, if y is 2001: a = 6 b = 20 c = 1 d = 5, e = 0 g = 6 h = 18 j = 0, k = 1 m = 0 r = 6 n = 4 p = 15 
Therefore, in 2001, Easter Sunday falls on April 15 (n = 4 and p = 15). 
 Be sure your program is very user friendly and well documented.


# In[1]:


# convert numeric month to alphabetic using index of list. e.g: month number = 1, return 1 - 1 = index 0 of list
def convert_to_alphabetic(month):
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    return months[month - 1]


# In[2]:


def find_easter():
    # Let y be the year
    y = int(input("Enter the year: "))
    # Divide y by 19 and call the remainder a. Ignore the quotient
    a = y % 19
    # Divide y by 100 to get a quotient b and remainder c
    b, c = divmod(y,100)
    # Divide b by 4 to get a quotient d and remainder e
    d, e = divmod(b,4)
    # Divide (8 * b + 13) by 25 to get quotient g. Ignore the remainder
    g = (8 * b + 13) // 25
    # Divide (19 * a + b – d – g + 15) by 30 to get remainder h. Ignore the quotient.
    h = (19 * a + b - d - g + 15) % 30
    # Divide c by 4 to get the quotient j and remainder k
    j, k = divmod(c,4)
    # Divide (a + 11 * h) by 319 to get quotient m. Ignore the remainder.
    m = (a + 11 * h) // 319
    # Divide (2 * e + 2 * j – k – h + m + 32) by 7 to get remainder r. Ignore the quotient.
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    # Divide (h – m + r + 90) by 25 to get quotient n. Ignore the remainder.
    n = (h - m + r + 90) // 25
    # Divide (h – m + r + n + 19) by 32 to get remainder p.  Ignore the quotient.
    p = (h - m + r + n + 19) % 32
    # The result is that Easter falls on day p of month n in the given year
    # Convert month num to month name
    n_name = convert_to_alphabetic(n)
    return print(f"In {y}, Easter Sunday falls on {n_name} {p}.")
find_easter()

