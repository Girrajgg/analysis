#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import datetime

import operator


# In[2]:



#head
e=pd.read_csv("D:\cop\cmps_trfc_mon1\cmps_trfc_mon\Data\head.csv")


# In[3]:


print(e.head(20))


# In[ ]:





# In[18]:


import csv

i=0
#time1="0to6",time2="6to9",time3="9t012",time4="12to15",time5="15to18",time6="18to21",time7="21to12"
dict={"timed1":0,"timed2":0,"timed3":0,"timed4":0,"timed5":0,"timed6":0,"timed7":0,
      "timej1":0,"timej2":0,"timej3":0,"timej4":0,"timej5":0,"timej6":0,"timej7":0,
     "timef1":0,"timef2":0,"timef3":0,"timef4":0,"timef5":0,"timef6":0,"timef7":0,
     "timed11":0,"timed22":0,"timed33":0,"timed44":0,"timed55":0,"timed66":0,"timed77":0,
      "timej11":0,"timej22":0,"timej33":0,"timej44":0,"timej55":0,"timej66":0,"timej77":0,
     "timef11":0,"timef22":0,"timef33":0,"timef44":0,"timef55":0,"timef66":0,"timef77":0}
dict1={"timed1":0,"timed2":0,"timed3":0,"timed4":0,"timed5":0,"timed6":0,"timed7":0,
        "timej1":0,"timej2":0,"timej3":0,"timej4":0,"timej5":0,"timej6":0,"timej7":0,
      "timef1":0,"timef2":0,"timef3":0,"timef4":0,"timef5":0,"timef6":0,"timef7":0}
 
dict2={"timed11":0,"timed22":0,"timed33":0,"timed44":0,"timed55":0,"timed66":0,"timed77":0,
        "timej11":0,"timej22":0,"timej33":0,"timej44":0,"timej55":0,"timej66":0,"timej77":0,
        "timef11":0,"timef22":0,"timef33":0,"timef44":0,"timef55":0,"timef66":0,"timef77":0}

fraction={"d11":0,"d22":0,"d33":0,"d44":0,"d55":0,"d66":0,"d77":0,
          "j11":0,"j22":0,"j33":0,"j44":0,"j55":0,"j66":0,"j77":0,
          "f11":0,"f22":0,"f33":0,"f44":0,"f55":0,"f66":0,"f77":0}
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
            if ans1<=ans and ans<=ans2:
                if dt>='00:00:00' and dt<'06:00:00':
                    dict["timed1"]=dict["timed1"]+1
                    dict1["timed1"]=dict["timed1"]+1
                    if row[8]== '1':
                        dict["timed11"]=dict["timed11"]+1
                        dict2["timed11"]=dict2["timed11"]+1
                elif dt>='06:00:00' and dt<'08:00:00':
                    dict["timed2"]=dict["timed2"]+1
                    dict1["timed2"]=dict1["timed2"]+1
                    if row[8]== '1' :
                        dict["timed22"]=dict["timed22"]+1
                        dict2["timed22"]=dict2["timed22"]+1
                elif dt>='08:00:00' and dt<'10:00:00':
                    dict["timed3"]=dict["timed3"]+1
                    dict1["timed3"]=dict1["timed3"]+1
                    if row[8]== '1' :
                        dict["timed33"]=dict["timed33"]+1
                        dict2["timed33"]=dict2["timed33"]+1
                elif dt>='10:00:00' and dt<'14:00:00':
                    dict["timed4"]=dict["timed4"]+1
                    dict1["timed4"]=dict1["timed4"]+1
                    if row[8]== '1' :
                        dict["timed44"]=dict["timed44"]+1
                        dict2["timed44"]=dict2["timed44"]+1
                elif dt>='14:00:00' and dt<'18:00:00':
                    dict["timed5"]=dict["timed5"]+1
                    dict1["timed5"]=dict1["timed5"]+1
                    if(row[8]== '1' ):  
                        dict["timed55"] = dict["timed55"]+1
                        dict2["timed55"] = dict2["timed55"]+1
                    #rint(True)
                elif dt>='18:00:00' and dt<'21:00:00':
                    dict["timed6"]=dict["timed6"]+1
                    dict1["timed6"]=dict1["timed6"]+1
                    if row[8]== '1' :
                        dict["timed66"]=dict["timed66"]+1
                        dict2["timed66"]=dict2["timed66"]+1
                else :
                    dict["timed7"]=dict["timed7"]+1
                    dict1["timed7"]=dict1["timed7"]+1
                    if row[8]== '1' :
                        dict["timed77"]=dict["timed77"]+1
                        dict2["timed77"]=dict2["timed77"]+1
               
            elif ansj1<=ans and ans<=ansj2:
                #rint('true')
                if dt>='00:00:00' and dt<'06:00:00':
                    dict["timej1"]=dict["timej1"]+1
                    dict1["timej1"]=dict["timej1"]+1
                    if row[8]== '1':
                        dict["timej11"]=dict["timej11"]+1
                        dict2["timej11"]=dict2["timej11"]+1
                elif dt>='06:00:00' and dt<'08:00:00':
                    dict["timej2"]=dict["timej2"]+1
                    dict1["timej2"]=dict1["timej2"]+1
                    if row[8]== '1' :
                        dict["timej22"]=dict["timej22"]+1
                        dict2["timej22"]=dict2["timej22"]+1
                elif dt>='08:00:00' and dt<'10:00:00':
                    dict["timej3"]=dict["timej3"]+1
                    dict1["timej3"]=dict1["timej3"]+1
                    if row[8]== '1' :
                        dict["timej33"]=dict["timej33"]+1
                        dict2["timej33"]=dict2["timej33"]+1
                elif dt>='10:00:00' and dt<'14:00:00':
                    dict["timej4"]=dict["timej4"]+1
                    dict1["timej4"]=dict1["timej4"]+1
                    if row[8]== '1' :
                        dict["timej44"]=dict["timej44"]+1
                        dict2["timej44"]=dict2["timej44"]+1
                elif dt>='14:00:00' and dt<'18:00:00':
                    dict["timej5"]=dict["timej5"]+1
                    dict1["timej5"]=dict1["timej5"]+1
                    if(row[8]== '1' ):  
                        dict["timej55"] = dict["timej55"]+1
                        dict2["timej55"] = dict2["timej55"]+1
                    #rint(True)
                elif dt>='18:00:00' and dt<'21:00:00':
                    dict["timej6"]=dict["timej6"]+1
                    dict1["timej6"]=dict1["timej6"]+1
                    if row[8]== '1' :
                        dict["timej66"]=dict["timej66"]+1
                        dict2["timej66"]=dict2["timej66"]+1
                else :
                    dict["timej7"]=dict["timej7"]+1
                    dict1["timej7"]=dict1["timej7"]+1
                    if row[8]== '1' :
                        dict["timej77"]=dict["timej77"]+1
                        dict2["timej77"]=dict2["timej77"]+1


                #print(dict)
            elif ansf1<=ans and ans<=ansf2:
                if dt>='00:00:00' and dt<'06:00:00':
                    dict["timef1"]=dict["timef1"]+1
                    dict1["timef1"]=dict["timef1"]+1
                    if row[8]== '1':
                        dict["timef11"]=dict["timef11"]+1
                        dict2["timef11"]=dict2["timef11"]+1
                elif dt>='06:00:00' and dt<'08:00:00':
                    dict["timef2"]=dict["timef2"]+1
                    dict1["timef2"]=dict1["timef2"]+1
                    if row[8]== '1' :
                        dict["timef22"]=dict["timef22"]+1
                        dict2["timef22"]=dict2["timef22"]+1
                elif dt>='08:00:00' and dt<'10:00:00':
                    dict["timef3"]=dict["timef3"]+1
                    dict1["timef3"]=dict1["timef3"]+1
                    if row[8]== '1' :
                        dict["timef33"]=dict["timef33"]+1
                        dict2["timef33"]=dict2["timef33"]+1
                elif dt>='10:00:00' and dt<'14:00:00':
                    dict["timef4"]=dict["timef4"]+1
                    dict1["timef4"]=dict1["timef4"]+1
                    if row[8]== '1' :
                        dict["timef44"]=dict["timef44"]+1
                        dict2["timef44"]=dict2["timef44"]+1
                elif dt>='14:00:00' and dt<'18:00:00':
                    dict["timef5"]=dict["timef5"]+1
                    dict1["timef5"]=dict1["timef5"]+1
                    if(row[8]== '1' ):  
                        dict["timef55"] = dict["timef55"]+1
                        dict2["timef55"] = dict2["timef55"]+1
                    #rint(True)
                elif dt>='18:00:00' and dt<'21:00:00':
                    dict["timef6"]=dict["timef6"]+1
                    dict1["timef6"]=dict1["timef6"]+1
                    if row[8]== '1' :
                        dict["timef66"]=dict["timef66"]+1
                        dict2["timef66"]=dict2["timef66"]+1
                else :
                    dict["timef7"]=dict["timef7"]+1
                    dict1["timef7"]=dict1["timef7"]+1
                    if row[8]== '1' :
                        dict["timef77"]=dict["timef77"]+1
                        dict2["timef77"]=dict2["timef77"]+1
                        

    print(dict)


# In[19]:


fraction["d11"]=dict2["timed11"]/dict1["timed1"]
fraction["d22"]=dict2["timed22"]/dict1["timed2"]
fraction["d33"]=dict2["timed33"]/dict1["timed3"]
fraction["d44"]=dict2["timed44"]/dict1["timed4"]
fraction["d55"]=dict2["timed55"]/dict1["timed5"]
fraction["d66"]=dict2["timed66"]/dict1["timed6"]
fraction["d77"]=dict2["timed77"]/dict1["timed7"]

fraction["j11"]=dict2["timej11"]/dict1["timej1"]
fraction["j22"]=dict2["timej22"]/dict1["timej2"]
fraction["j33"]=dict2["timej33"]/dict1["timej3"]
fraction["j44"]=dict2["timej44"]/dict1["timej4"]
fraction["j55"]=dict2["timej55"]/dict1["timej5"]
fraction["j66"]=dict2["timej66"]/dict1["timej6"]
fraction["j77"]=dict2["timej77"]/dict1["timej7"]

fraction["f11"]=dict2["timef11"]/dict1["timef1"]
fraction["f22"]=dict2["timef22"]/dict1["timef2"]
fraction["f33"]=dict2["timef33"]/dict1["timef3"]
fraction["f44"]=dict2["timef44"]/dict1["timef4"]
fraction["f55"]=dict2["timef55"]/dict1["timef5"]
fraction["f66"]=dict2["timef66"]/dict1["timef6"]
fraction["f77"]=dict2["timef77"]/dict1["timef7"]


# In[32]:


# dict1={"timed1":0,"timed2":0,"timed3":0,"timed4":0,"timed5":0,"timed6":0,"timed7":0,
#       "timej1":0,"timej2":0,"timej3":0,"timej4":0,"timej5":0,"timej6":0,"timej7":0,
#      "timef1":0,"timef2":0,"timef3":0,"timef4":0,"timef5":0,"timef6":0,"timef7":0}

# dict2={"timed11":0,"timed22":0,"timed33":0,"timed44":0,"timed55":0,"timed66":0,"timed77":0,
#       "timej11":0,"timej22":0,"timej33":0,"timej44":0,"timej55":0,"timej66":0,"timej77":0,
#      "timef11":0,"timef22":0,"timef33":0,"timef44":0,"timef55":0,"timef66":0,"timef77":0}


# In[20]:


print(fraction)


# In[21]:


print(dict2)


# In[10]:


import matplotlib.pyplot as plt

data = dict2
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\timewise_violators.png")
plt.show()


# In[15]:


import matplotlib.pyplot as plt

data = dict1
time = list(data.keys())
violations= list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\timewise_traffic.png")
plt.show()


# In[16]:


import matplotlib.pyplot as plt

data = dict2
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\timewise_violation.png")

plt.show()


# In[22]:


import matplotlib.pyplot as plt

data = fraction
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\violatorsvstraffictimewise.png")
plt.show()


# In[40]:


print(row[8])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




