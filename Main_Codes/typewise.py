#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import datetime
import operator


# In[2]:


e=pd.read_csv("D:\cop\cmps_trfc_mon1\cmps_trfc_mon\Data\head.csv")


# In[3]:


print(e.head(20))


# In[36]:


import csv

i=0
#time1="0to6",time2="6to9",time3="9t012",time4="12to15",time5="15to18",time6="18to21",time7="21to12"
dict={"type1d":0,"type2d":0,"type11d":0,"type12d":0,"type-1d":0,
     "type1j":0,"type2j":0,"type11j":0,"type12j":0,"type-1j":0,
     "type1f":0,"type2f":0,"type11f":0,"type12f":0,"type-1f":0}
dict2={"type1d":0,
     "type1j":0,
     "type1f":0,}
dict1={"type1d":0,"type2d":0,"type11d":0,"type12d":0,"type-1d":0,
     "type1j":0,"type2j":0,"type11j":0,"type12j":0,"type-1j":0,
     "type1f":0,"type2f":0,"type11f":0,"type12f":0,"type-1f":0}
fraction={"d11":0,"d22":0,"d33":0,"d44":0,"d55":0,
          "j11":0,"22":0,"j33":0,"j44":0,"j55":0,
          "f11":0,"f22":0,"f33":0,"f44":0,"f55":0}
with open('D:\cop\cmps_trfc_mon1\cmps_trfc_mon\Data\head.csv','r') as newFile:
    dt1='2018-12-1'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ans1 = datetime.date(year, month, day)
    dt2='2018-12-31'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ans2 = datetime.date(year, month, day)
    
    
    
    #deciding range of the time period of january:=
    dtj1='2019-01-1'#deciding range of the time period
    year,month,day = (int(x) for x in dtj1.split('-'))    
    ansj1 = datetime.date(year, month, day)
    dtj2='2019-01-31'
    year,month,day = (int(x) for x in dtj2.split('-'))    
    ansj2 = datetime.date(year, month, day)
    
    
    #deciding range of the time period of february:=
    dtf1='2019-02-1'
    year,month,day = (int(x) for x in dtf1.split('-'))    
    ansf1 = datetime.date(year, month, day)
    dtf2='2019-02-28'
    year,month,day = (int(x) for x in dtf2.split('-'))    
    ansf2 = datetime.date(year, month, day)
   
    FileReader=csv.reader(newFile)
    for row in FileReader:
        if i==0:
            i=i+1
            
        else:   
            when=row[2]
            x=when.split(" ")
            
            dt=x[1]
            date=x[0]
            year,month,day = (int(x) for x in date.split('-'))    
            ans = datetime.date(year, month, day)
            #print(dt)
            #print(dt>'15:26:49')
            #print(ans)
           # print(dt>='00:00:00' and dt<'06:00:00')
            #print(dt>='15:00:00' and dt<'18:00:00')
            #11,1,-1,12,2
            if ans1<=ans and ans<=ans2:
                dict1["type1d"]=dict1["type1d"]+1 
                dict1["type2d"]=dict1["type2d"]+1
                dict1["type11d"]=dict1["type11d"]+1
                dict1["type-1d"]=dict1["type-1d"]+1
                dict1["type12d"]=dict1["type12d"]+1
                dict2["type1d"]=dict2["type1d"]+1
                if row[3]=='1':
                    dict["type1d"]=dict["type1d"]+1        
                elif row[3]=='2':
                    dict["type2d"]=dict["type2d"]+1
                elif row[3]=='11':
                    dict["type11d"]=dict["type11d"]+1
                elif row[3]=='-1':
                    dict["type-1d"]=dict["type-1d"]+1
                elif row[3]=='12':
                    dict["type12d"]=dict["type12d"]+1
                    #rint(True)
              
               
            elif ansj1<=ans and ans<=ansj2 and row[4]=='1':
                dict1["type1j"]=dict1["type1j"]+1 
                dict1["type2j"]=dict1["type2j"]+1
                dict1["type11j"]=dict1["type11j"]+1
                dict1["type-1j"]=dict1["type-1j"]+1
                dict1["type12j"]=dict1["type12j"]+1
                dict2["type1j"]=dict2["type1j"]+1
                if row[3]=='1':
                    dict["type1j"]=dict["type1j"]+1   
                elif row[3]=='2':
                    dict["type2j"]=dict["type2j"]+1   
                elif row[3]=='11':
                    dict["type11j"]=dict["type11j"]+1
                elif row[3]=='-1':
                    dict["type-1j"]=dict["type-1j"]+1  
                elif row[3]=='12':
                    dict["type12j"]=dict["type12j"]+1
                    
                    #rint(True)
               #
            elif ansf1<=ans and ans<=ansf2 and row[4]=='1':
                dict1["type1f"]=dict1["type1f"]+1 
                dict1["type2f"]=dict1["type2f"]+1
                dict1["type11f"]=dict1["type11f"]+1
                dict1["type-1f"]=dict1["type-1f"]+1
                dict1["type12f"]=dict1["type12f"]+1
                dict2["type1f"]=dict2["type1f"]+1
                if row[3]=='1':
                    dict["type1f"]=dict["type1f"]+1
                         
                elif row[3]=='2':
                    dict["type2f"]=dict["type2f"]+1
                elif row[3]=='11':
                    dict["type11f"]=dict["type11f"]+1
                elif row[3]=='-1':
                    dict["type-1f"]=dict["type-1f"]+1
                elif row[3]=='12':
                    dict["type12f"]=dict["type12f"]+1
                    #rint(True)
               # elif dt>='18:00:00' and dt<'21:00:00':
               
    print(dict1)


# In[37]:


print(dict)


# In[38]:


print(dict2)


# In[30]:


fraction["d11"]=dict["type1d"]/dict1["type1d"]
fraction["d22"]=dict["type2d"]/dict1["type2d"]
fraction["d33"]=dict["type11d"]/dict1["type11d"]
fraction["d44"]=dict["type12d"]/dict1["type12d"]
fraction["d55"]=dict["type-1d"]/dict1["type-1d"]

fraction["j11"]=dict["type1j"]/dict1["type1j"]
fraction["j22"]=dict["type2j"]/dict1["type2j"]
fraction["j33"]=dict["type11j"]/dict1["type11j"]
fraction["j44"]=dict["type12j"]/dict1["type12j"]
fraction["j55"]=dict["type-1j"]/dict1["type-1j"]

fraction["f11"]=dict["type1f"]/dict1["type1f"]
fraction["f22"]=dict["type2f"]/dict1["type2f"]
fraction["f33"]=dict["type11f"]/dict1["type11f"]
fraction["f44"]=dict["type12f"]/dict1["type12f"]
fraction["f55"]=dict["type-1f"]/dict1["type-1f"]


# In[31]:


print(fraction)


# In[32]:


import matplotlib.pyplot as plt

data = dict
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\typeviolation.png")
plt.show()


# In[39]:


import matplotlib.pyplot as plt

data = dict2
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\typetraffic.png")
plt.show()


# In[35]:


import matplotlib.pyplot as plt

data = fraction
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\fractiontype.png")
plt.show()


# In[ ]:




