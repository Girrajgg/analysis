#!/usr/bin/env python
# coding: utf-8

# In[20]:


#prints day of a week like monday
import datetime
dt = '10/03/2019'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
print(ans.strftime("%A"))


# In[ ]:


# In[ ]:




