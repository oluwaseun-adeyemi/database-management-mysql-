#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector


# In[2]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hebron2022",
  database="pop_proj_09"
)


# In[3]:


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[4]:


mycursor.execute("SELECT * FROM pop_proj_09")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# In[5]:


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pop_proj_09 WHERE id='3'")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# In[6]:


import ipywidgets as wg


# In[7]:


from IPython.display import display


# In[8]:


IPython.display import display
states = wg.Text(value='states')
male = wg.IntSlider(description='male:')
display(State,Population)


# In[10]:


states = wg.Text(value='states')
male = wg.IntSlider(description='male:')
display(states,male)


# In[ ]:




