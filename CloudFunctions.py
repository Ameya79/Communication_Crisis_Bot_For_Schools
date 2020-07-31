#!/usr/bin/env python
# coding: utf-8

# In[3]:


from googlesearch import search  
  
# to search 
query = "Public transport near me"
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 


# In[ ]:




