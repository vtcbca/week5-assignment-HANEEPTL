#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv


# In[8]:


f=open('c:\\sqlite3\\csv\\student.csv','w',newline='')


# In[9]:


w=csv.writer(f)


# In[10]:


header=["id","name","city","contact"]
w.writerow(header)


# In[11]:


row=[[1,"hanee","bardoli",8976567569],[2,"heer","tarsadi",6574321678],[3,"riya","surat",8796754678],[4,"krisha","baroda",8796543215]]
w.writerows(row)


# In[12]:


f.close()


# In[ ]:




