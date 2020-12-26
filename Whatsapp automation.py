#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pywhatkit


# In[5]:


import pywhatkit
number=input()
msg=input()
hr=int(input())
mn=int(input())

pywhatkit.sendwhatmsg(number, msg , hr , mn)


# In[ ]:




