#!/usr/bin/env python
# coding: utf-8

# In[32]:


#date time split
import datetime
with open('/home/ajit/Desktop/out3.csv','r') as outFile:
    fileWriter=csv.reader(outFile)
    for row in fileWriter:
        
       
        when = row[2]
        x=when.split(" ")
        print(x[0])
      
        dt = x[0]
        
        year,month,day = (int(x) for x in dt.split('-'))    
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))


# In[ ]:




