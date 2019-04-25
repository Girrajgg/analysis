#!/usr/bin/env python
# coding: utf-8

# In[69]:


#weekwise analysis
import csv
i=0
dict={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0,
      "Mondayj":0,"Tuesdayj":0,"Wednesdayj":0,"Thursdayj":0,"Fridayj":0,"Saturdayj":0,"Sundayj":0,
     "Mondayf":0,"Tuesdayf":0,"Wednesdayf":0,"Thursdayf":0,"Fridayf":0,"Saturdayf":0,"Sundayf":0}
with open('/home/ajit/Desktop/data-1552593056171 (copy).csv','r') as newFile:
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
            dt=x[0]
            year,month,day = (int(x) for x in dt.split('-'))    
            ans = datetime.date(year, month, day)
           
            if ans1<=ans and ans<=ans2: #and row[4]=='1':
                if ans.strftime("%A")=="Monday":
                    dict["Monday"]=dict["Monday"]+1
                elif ans.strftime("%A")=="Tuesday":
                    dict["Tuesday"]=dict["Tuesday"]+1
                elif ans.strftime("%A")=="Wednesday":
                    dict["Wednesday"]=dict["Wednesday"]+1 
                    
                elif ans.strftime("%A")=="Thursday": 
                    dict["Thursday"]=dict["Thursday"]+1 
                    
                elif ans.strftime("%A")=="Friday": 
                    
                    dict["Friday"]=dict["Friday"]+1 
                elif ans.strftime("%A")=="Saturday": 
                    dict["Saturday"]=dict["Saturday"]+1 
                else: 
                    dict["Sunday"]=dict["Sunday"]+1 
            elif ansj1<=ans and ans<=ansj2:# and row[4]=='1':
                if ans.strftime("%A")=="Monday":
                    dict["Mondayj"]=dict["Mondayj"]+1
                elif ans.strftime("%A")=="Tuesday":
                    dict["Tuesdayj"]=dict["Tuesdayj"]+1
                elif ans.strftime("%A")=="Wednesday":
                    dict["Wednesdayj"]=dict["Wednesdayj"]+1 
                    
                elif ans.strftime("%A")=="Thursday": 
                    dict["Thursdayj"]=dict["Thursdayj"]+1 
                    
                elif ans.strftime("%A")=="Friday": 
                    
                    dict["Fridayj"]=dict["Fridayj"]+1 
                elif ans.strftime("%A")=="Saturday": 
                    dict["Saturdayj"]=dict["Saturdayj"]+1 
                else: 
                    dict["Sundayj"]=dict["Sundayj"]+1 
            elif ansf1<=ans and ans<=ansf2:#and row[4]=='1':
                if ans.strftime("%A")=="Monday":
                    dict["Mondayf"]=dict["Mondayf"]+1
                elif ans.strftime("%A")=="Tuesday":
                    dict["Tuesdayf"]=dict["Tuesdayf"]+1
                elif ans.strftime("%A")=="Wednesday":
                    dict["Wednesdayf"]=dict["Wednesdayf"]+1 
                    
                elif ans.strftime("%A")=="Thursday": 
                    dict["Thursdayf"]=dict["Thursdayf"]+1 
                    
                elif ans.strftime("%A")=="Friday": 
                    
                    dict["Fridayf"]=dict["Fridayf"]+1 
                elif ans.strftime("%A")=="Saturday": 
                    dict["Saturdayf"]=dict["Saturdayf"]+1 
                else: 
                    dict["Sundayf"]=dict["Sundayf"]+1 
                
    print(dict)      
import matplotlib.pyplot as plt

data = dict
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig('bar.png')
plt.show()
                
                
        
                    
                    
                
                
                
                


# In[12]:


dict={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}

dict["Monday"]=dict["Monday"]+1
print(dict["Monday"])


# In[32]:


#to comapre the date
import datetime
dt='2018-11-6'
year,month,day = (int(x) for x in dt.split('-'))    
ans = datetime.date(year, month, day)
dt1='2018-11-7'
year,month,day = (int(x) for x in dt1.split('-'))    
ans1 = datetime.date(year, month, day)
print(ans1.strftime("%A"))


# In[56]:


import matplotlib.pyplot as plt

D = {u'Label1':26, u'Label2': 17, u'Label3':30}

plt.scatter(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.savefig('plot.png')
plt.show()


# In[54]:


import numpy as np
import matplotlib.pyplot as plt

data = {'apple': 67, 'mango': 60, 'lichi': 58}
names = list(data.keys())
values = list(data.values())


#tick_label does the some work as plt.xticks()
plt.(range(len(data)),values,tick_label=names)
plt.savefig('plot.png')
plt.show()


# In[62]:


import csv
i=0
dict={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0,
      "Mondayj":0,"Tuesdayj":0,"Wednesdayj":0,"Thursdayj":0,"Fridayj":0,"Saturdayj":0,"Sundayj":0,
     "Mondayf":0,"Tuesdayf":0,"Wednesdayf":0,"Thursdayf":0,"Fridayf":0,"Saturdayf":0,"Sundayf":0}
with open('/home/ajit/Desktop/data-1552593056171 (copy).csv','r') as newFile:
    dt1='2018-12-1'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ans1 = datetime.date(year, month, day)
    dt2='2018-12-31'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ans2 = datetime.date(year, month, day)
    FileReader=csv.reader(newFile)
    for row in FileReader:
        if i==0:
            i=i+1
            
        else:   
            when=row[2]
            x=when.split(" ")
            dt=x[0]
            year,month,day = (int(x) for x in dt.split('-'))    
            ans = datetime.date(year, month, day)
           
            if ans1<=ans and ans<=ans2:
                if ans.strftime("%A")=="Monday":
                    dict["Monday"]=dict["Monday"]+1
                elif ans.strftime("%A")=="Tuesday":
                    dict["Tuesday"]=dict["Tuesday"]+1
                elif ans.strftime("%A")=="Wednesday":
                    dict["Wednesday"]=dict["Wednesday"]+1 
                    
                elif ans.strftime("%A")=="Thursday": 
                    dict["Thursday"]=dict["Thursday"]+1 
                    
                elif ans.strftime("%A")=="Friday": 
                    
                    dict["Friday"]=dict["Friday"]+1 
                elif ans.strftime("%A")=="Saturday": 
                    dict["Saturday"]=dict["Saturday"]+1 
                else: 
                    dict["Sunday"]=dict["Sunday"]+1 
print(dict)   
import matplotlib.pyplot as plt

data = dict
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig('bar.png')
plt.show()    
    
    #deciding range of the time period of janeuary:=


# In[ ]:




