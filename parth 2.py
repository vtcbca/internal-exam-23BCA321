#!/usr/bin/env python
# coding: utf-8

# # Create BCA.txt. Write 5 lines directly and 5 lines must be taken from user. Print the smallest and largest word in this file.

# In[2]:


f=open("D:\\319bca\\sqlite3\\deta\\bca.txt","w")


# In[3]:


f.write("this is a semple file,\n")


# In[4]:


f.write("it contains 5 lins directiy,\n")


# In[5]:


f.write("it contains 5 lins directiy,\n")
f.write("and 5 lins from two user,\n")


# In[6]:


f.write("it contains 5 lins directiy,\n")
f.write("and 5 lins from two user,\n")
f.write("the smellest and inrcest words will be printed,\n")
f.write("the file is created by bca student,\n")


# In[8]:


l=[]


# # take 5 input from user

# In[15]:


for i in range(5):
    s=input("entar motence from user")
    l.append(s)


# In[16]:


f=open("D:\\319bca\\sqlite3\\deta\\bca.txt","r")


# In[17]:


lines=f.readlines()


# In[5]:


words=[


# In[7]:


for line in lines:
    words.extend(line.strip().split())


# In[8]:


f=open("D:\\319bca\\sqlite3\\deta\\bca.txt","r")


# In[9]:


lines=f.readlines()


# In[10]:


words=[]


# In[13]:


lines=f.readlines()
for line in lines:
    word.extend(line.strip().split())


# ### smallest word in file

# In[15]:


smallest_word = min(words, key=len)


# In[ ]:




