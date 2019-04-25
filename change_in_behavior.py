#!/usr/bin/env python
# coding: utf-8

# In[52]:


import numpy as np
import datetime
import operator

import csv
i=0
from collections import defaultdict
d = defaultdict(list)
# d={'1':[1, 2, 3]}
# d['1'].append(4)
# print(d['1'][3])

with open('/home/ajit/Desktop/phone_messages.csv', 'r') as readfile:
    filereader=csv.reader(readfile)
    dt1='2018-07-01'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ansjl1 = datetime.date(year, month, day)
    dt2='2019-08-01'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansAg1 = datetime.date(year, month, day)
    dt1='2018-09-1'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ansSe1 = datetime.date(year, month, day)
    dt2='2018-10-1'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansOc1 = datetime.date(year, month, day)
    dt1='2018-11-1'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ansNo1 = datetime.date(year, month, day)
    dt2='2018-12-1'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansDe1 = datetime.date(year, month, day)
            
    for row in filereader:
      
        if(i>=0):
            when=row[7]
            x=when.split(" ")
                
            dt=x[1]
            date=x[0]
            year,month,day = (int(x) for x in date.split('-'))    
            ans = datetime.date(year, month, day)
        
          
        
            
            if row[1] in d and row[3]=='1':
                if ansjl1<=ans and ans<ansAg1:
                    d[row[1]][0]=1+d[row[1]][0]
                if ansAg1<=ans and ans<ansSe1:
                    d[row[1]][1]=1+d[row[1]][0]
                if ansSe1<=ans and ans<ansOc1:
                    d[row[1]][2]=1+d[row[1]][0]
                if ansOc1<=ans and ans<ansNo1:
                    d[row[1]][3]=1+d[row[1]][0]
                if ansNo1<=ans and ans<ansDe1:
                    d[row[1]][4]=1+d[row[1]][0]
                
                    
            elif row[3]=='1':
                d[row[1]].append(0)
                d[row[1]].append(0)
                d[row[1]].append(0)
                d[row[1]].append(0)
                d[row[1]].append(0)
                d[row[1]].append(0)
                if ansjl1<=ans and ans<ansAg1:
                    d[row[1]][0]=1
                if ansAg1<=ans and ans<ansSe1:
                    d[row[1]][1]=1
                if ansSe1<=ans and ans<ansOc1:
                    d[row[1]][2]=1
                if ansOc1<=ans and ans<ansNo1:
                    d[row[1]][3]=1
                if ansNo1<=ans and ans<ansDe1:
                    d[row[1]][4]=1
                
data=d
x=data.keys()
array=[]
for z in x:
    array.append(z)
    array.append(d[z][0])
print(array)
    
            
            
        
                
        
        
                
            


# In[48]:


from collections import defaultdict
d = defaultdict(list)
d={'2018'}
print(d)


# In[ ]:





# In[18]:





# In[ ]:




