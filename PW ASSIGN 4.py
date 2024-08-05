#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Print numbers from 1 to 5 using a while loop:
i = 1
while i <= 5:
    print(i)
    i += 1


# In[2]:


# Calculate the sum of numbers from 1 to 10 using a while loop:
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print("Sum of numbers from 1 to 10:", sum)


# In[3]:


#Calculate the factorial of a number using a for loop:
num = 5  # You can change this number to calculate the factorial of another number
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num}:", factorial)


# In[4]:


# Count the number of vowels in a string using a for loop:
string = "Hello, World!"
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels in the string:", count)


# In[5]:


# Print a pattern using nested loops:
# Example pattern: Right-angled triangle
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print("")


# In[6]:


# Generate a multiplication table using nested loops:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:3}", end=" ")
    print("")


# In[ ]:




