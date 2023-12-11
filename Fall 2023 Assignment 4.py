#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 4

Write a program asking the user to enter as many grades as he or she wants. 
Complete the edit check to ensure that the grade is valid – between 0 and 100. 
If an invalid grade has been entered, the user will be asked to re-enter the grade. 
The user will enter 999 to end the program. Be sure to give very explicit instructions to the user.

When a valid grade has been entered, the program will determine the letter grade 
with 90 – 100 being an A, 80 – 89 a B, 70 – 79 a C, 60 – 69 a D, and anything below 60 a F. 
The letter grade will be printed with the appropriate message. 

When the program is terminated by the user entering 999, 
the average grade, number of entries, highest grade, and lowest grade will be printed.

The user will be allowed to terminate the program without entering any grades.


# In[1]:


def grade():
    print('Welcome to Grade Calculate Program!')
    list_grade = []

    while True:
        user_input = input('Please enter your grade number in integer (enter 999 to end): ')
        
        if user_input == '999':
            if list_grade:
                avg_grade = sum(list_grade) / len(list_grade)
                no_entries = len(list_grade)
                max_grade = max(list_grade)
                min_grade = min(list_grade)
                print(f'The average grade is: {avg_grade}, number of entries is {no_entries}, highest grade is {max_grade}, lowest grade is {min_grade}')
            print('Thank you for using our Program. Bye!')
            break
        else:
            try:
                grade = int(user_input)
                if 0 <= grade <= 100:
                    list_grade.append(grade)
                    if grade > 89:
                        print('Your grade letter is A! Excellent!')
                    elif grade > 79:
                        print('Your grade letter is B! Good!')
                    elif grade > 69:
                        print('Your grade letter is C! Better luck next time!')
                    elif grade > 59:
                        print('Your grade letter is D! That is pretty bad!')
                    else:
                        print('Your grade letter is F! You failed!')
                else:
                    print('Invalid input. Please enter a grade between 0 and 100.')
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
grade()


# In[ ]:




