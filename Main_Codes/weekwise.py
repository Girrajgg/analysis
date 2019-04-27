#!/usr/bin/env python
# coding: utf-8

# In[52]:


import numpy as np
import pandas as pd
import datetime
import operator


# In[53]:


e=pd.read_csv("D:\cop\cmps_trfc_mon1\cmps_trfc_mon\Data\head.csv")


# In[15]:


print(e.head(20))


# In[16]:


import datetime
dt = '1/12/2018'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
print(ans.strftime("%A"))


# In[ ]:





# In[81]:


import csv
i=0
#days
dict={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0,
      "Mondayj":0,"Tuesdayj":0,"Wednesdayj":0,"Thursdayj":0,"Fridayj":0,"Saturdayj":0,"Sundayj":0,
     "Mondayf":0,"Tuesdayf":0,"Wednesdayf":0,"Thursdayf":0,"Fridayf":0,"Saturdayf":0,"Sundayf":0}
dict1={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0,
          "Mondayj":0,"Tuesdayj":0,"Wednesdayj":0,"Thursdayj":0,"Fridayj":0,"Saturdayj":0,"Sundayj":0,
         "Mondayf":0,"Tuesdayf":0,"Wednesdayf":0,"Thursdayf":0,"Fridayf":0,"Saturdayf":0,"Sundayf":0}
dict2={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0,
          "Mondayj":0,"Tuesdayj":0,"Wednesdayj":0,"Thursdayj":0,"Fridayj":0,"Saturdayj":0,"Sundayj":0,
         "Mondayf":0,"Tuesdayf":0,"Wednesdayf":0,"Thursdayf":0,"Fridayf":0,"Saturdayf":0,"Sundayf":0}
fraction={"d11":0,"d22":0,"d33":0,"d44":0,"d55":0,"d66":0,"d77":0,
          "j11":0,"22":0,"j33":0,"j44":0,"j55":0,"j66":0,"j77":0,
          "f11":0,"f22":0,"f33":0,"f44":0,"f55":0,"f66":0,"f77":0}
#workingdays
fraction1={"d11":0,"d22":0,"d33":0,"d44":0,"d55":0,"j11":0,"22":0,"j33":0,"j44":0,"j55":0,
            "f11":0,"f22":0,"f33":0,"f44":0,"f55":0}
#weekends
fraction2={"d66":0,"d77":0,"j66":0,"j77":0,"f66":0,"f77":0}



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
            dt=x[0]
            year,month,day = (int(x) for x in dt.split('-'))    
            ans = datetime.date(year, month, day)
           
            if ans1<=ans and ans<=ans2: #and row[4]=='1':
                if ans.strftime("%A")=="Monday":
                    dict["Monday"]=dict["Monday"]+1
                    dict1["Monday"]=dict1["Monday"]+1
                    if row[8]== '1':
                        dict2["Monday"]=dict2["Monday"]+1 
                elif ans.strftime("%A")=="Tuesday":
                    dict["Tuesday"]=dict["Tuesday"]+1
                    dict1["Tuesday"]=dict1["Tuesday"]+1
                    if row[8]== '1':
                         dict2["Tuesday"]=dict2["Tuesday"]+1
                elif ans.strftime("%A")=="Wednesday":
                    dict["Wednesday"]=dict["Wednesday"]+1
                    dict1["Wednesday"]=dict1["Wednesday"]+1
                    if row[8]== '1':
                        dict2["Wednesday"]=dict2["Wednesday"]+1
                elif ans.strftime("%A")=="Thursday": 
                    dict["Thursday"]=dict["Thursday"]+1
                    dict1["Thursday"]=dict1["Thursday"]+1
                    if row[8]== '1':
                        dict2["Thursday"]=dict2["Thursday"]+1
                elif ans.strftime("%A")=="Friday": 
                    dict["Friday"]=dict["Friday"]+1
                    dict1["Friday"]=dict1["Friday"]+1
                    if row[8]== '1':
                        dict2["Friday"]=dict2["Friday"]+1
                elif ans.strftime("%A")=="Saturday": 
                    dict["Saturday"]=dict["Saturday"]+1
                    dict1["Saturday"]=dict1["Saturday"]+1
                    if row[8]== '1':
                        dict2["Saturday"]=dict2["Saturday"]+1
                else: 
                    dict["Sunday"]=dict["Sunday"]+1
                    dict1["Sunday"]=dict1["Sunday"]+1
                    if row[8]== '1':
                        dict2["Sunday"]=dict2["Sunday"]+1
            elif ansj1<=ans and ans<=ansj2:# and row[4]=='1':
                if ans.strftime("%A")=="Monday":
                    dict["Mondayj"]=dict["Mondayj"]+1
                    dict1["Mondayj"]=dict1["Mondayj"]+1
                    if row[8]== '1':
                        dict2["Mondayj"]=dict2["Mondayj"]+1 
                elif ans.strftime("%A")=="Tuesday":
                    dict["Tuesdayj"]=dict["Tuesdayj"]+1
                    dict1["Tuesdayj"]=dict1["Tuesdayj"]+1
                    if row[8]== '1':
                         dict2["Tuesdayj"]=dict2["Tuesdayj"]+1
                elif ans.strftime("%A")=="Wednesday":
                    dict["Wednesdayj"]=dict["Wednesdayj"]+1
                    dict1["Wednesdayj"]=dict1["Wednesdayj"]+1
                    if row[8]== '1':
                        dict2["Wednesdayj"]=dict2["Wednesdayj"]+1
                elif ans.strftime("%A")=="Thursday": 
                    dict["Thursdayj"]=dict["Thursdayj"]+1
                    dict1["Thursdayj"]=dict1["Thursdayj"]+1
                    if row[8]== '1':
                        dict2["Thursdayj"]=dict2["Thursdayj"]+1
                elif ans.strftime("%A")=="Friday": 
                    dict["Fridayj"]=dict["Fridayj"]+1
                    dict1["Fridayj"]=dict1["Fridayj"]+1
                    if row[8]== '1':
                        dict2["Fridayj"]=dict2["Fridayj"]+1
                elif ans.strftime("%A")=="Saturday": 
                    dict["Saturdayj"]=dict["Saturdayj"]+1
                    dict1["Saturdayj"]=dict1["Saturdayj"]+1
                    if row[8]== '1':
                        dict2["Saturdayj"]=dict2["Saturdayj"]+1
                else: 
                    dict["Sundayj"]=dict["Sundayj"]+1
                    dict1["Sundayj"]=dict1["Sundayj"]+1
                    if row[8]== '1':
                        dict2["Sundayj"]=dict2["Sundayj"]+1
            elif ansf1<=ans and ans<=ansf2:#and row[4]=='1':
                if ans.strftime("%A")=="Monday":
                    dict["Mondayf"]=dict["Mondayf"]+1
                    dict1["Mondayf"]=dict1["Mondayf"]+1
                    if row[8]== '1':
                        dict2["Mondayf"]=dict2["Mondayf"]+1 
                elif ans.strftime("%A")=="Tuesday":
                    dict["Tuesdayf"]=dict["Tuesdayf"]+1
                    dict1["Tuesdayf"]=dict1["Tuesdayf"]+1
                    if row[8]== '1':
                         dict2["Tuesdayf"]=dict2["Tuesdayf"]+1
                elif ans.strftime("%A")=="Wednesday":
                    dict["Wednesdayf"]=dict["Wednesdayf"]+1
                    dict1["Wednesdayf"]=dict1["Wednesdayf"]+1
                    if row[8]== '1':
                        dict2["Wednesdayf"]=dict2["Wednesdayf"]+1
                elif ans.strftime("%A")=="Thursday": 
                    dict["Thursdayf"]=dict["Thursdayf"]+1
                    dict1["Thursdayf"]=dict1["Thursdayf"]+1
                    if row[8]== '1':
                        dict2["Thursdayf"]=dict2["Thursdayf"]+1
                elif ans.strftime("%A")=="Friday": 
                    dict["Fridayf"]=dict["Fridayf"]+1
                    dict1["Fridayf"]=dict1["Fridayf"]+1
                    if row[8]== '1':
                        dict2["Fridayf"]=dict2["Fridayf"]+1
                elif ans.strftime("%A")=="Saturday": 
                    dict["Saturdayf"]=dict["Saturdayf"]+1
                    dict1["Saturdayf"]=dict1["Saturdayf"]+1
                    if row[8]== '1':
                        dict2["Saturdayf"]=dict2["Saturdayf"]+1
                else: 
                    dict["Sundayf"]=dict["Sundayf"]+1
                    dict1["Sundayf"]=dict1["Sundayf"]+1
                    if row[8]== '1':
                        dict2["Sundayf"]=dict2["Sundayf"]+1
                
    print(dict) 


# In[82]:


print(ans)


# In[5]:


print(dict1)


# In[6]:


print(dict2)


# In[17]:


ee=pd.read_csv("D:\cop\cmps_trfc_mon1\cmps_trfc_mon\Data\Smartevent.csv")


# In[ ]:


print(ee)


# In[93]:


#deciding range of the time period of holidays(Dec):=
ii=0
fractionholiday2={"may1":0,"may2":0,"may3":0,"jun1":0,"jun2":0,"jun3":0,"jun4":0,
           "july1":0,"july2":0,"dec1":0,"dec2":0,"dec3":0}
holiday1={"may1":0,"may2":0,"may3":0,"jun1":0,"jun2":0,"jun3":0,"jun4":0,
           "july1":0,"july2":0,"dec1":0,"dec2":0,"dec3":0}     
holiday2={"may1":0,"may2":0,"may3":0,"jun1":0,"jun2":0,"jun3":0,"jun4":0,
           "july1":0,"july2":0,"dec1":0,"dec2":0,"dec3":0} 
#holiday   2019-01-14 2019-01-26 2018-08-15 2018-08-22 2018-09-03
# 2018-09-21 2018-10-02 2018-10-19 2019-11-07 2018-11-09 2018-11-23
#2018-05-10  to 2018-07-18


with open('D:\cop\cmps_trfc_mon1\cmps_trfc_mon\Data\Smartevent.csv','r') as newFile:
    dec11='2019-01-03'#deciding range of the time period
    year,month,day = (int(x) for x in dec11.split('-'))    
    ansdec11 = datetime.date(year, month, day)
    dec12='2019-01-10'
    year,month,day = (int(x) for x in dec12.split('-'))    
    ansdec12 = datetime.date(year, month, day)
    
    dec21='2019-01-11'#deciding range of the time period
    year,month,day = (int(x) for x in dec21.split('-'))    
    ansdec21 = datetime.date(year, month, day)
    dec22='2019-01-18'
    year,month,day = (int(x) for x in dec22.split('-'))    
    ansdec22 = datetime.date(year, month, day)
    
    dec31='2019-01-19'#deciding range of the time period
    year,month,day = (int(x) for x in dec31.split('-'))    
    ansdec31 = datetime.date(year, month, day)
    dec32='2019-01-28'
    year,month,day = (int(x) for x in dec32.split('-'))    
    ansdec32 = datetime.date(year, month, day)
    
    may11='2018-05-10'#deciding range of the time period
    year,month,day = (int(x) for x in may11.split('-'))    
    ansmay11 = datetime.date(year, month, day)
    may12='2018-05-17'
    year,month,day = (int(x) for x in may12.split('-'))    
    ansmay12 = datetime.date(year, month, day)
    
    may21='2018-05-18'#deciding range of the time period
    year,month,day = (int(x) for x in may21.split('-'))    
    ansmay21 = datetime.date(year, month, day)
    may22='2018-05-25'
    year,month,day = (int(x) for x in may22.split('-'))    
    ansmay22 = datetime.date(year, month, day)
    
    may31='2018-05-26'#deciding range of the time period
    year,month,day = (int(x) for x in may31.split('-'))    
    ansmay31 = datetime.date(year, month, day)
    may32='2018-05-31'
    year,month,day = (int(x) for x in may32.split('-'))    
    ansmay32 = datetime.date(year, month, day)
    
    jun11='2018-06-01'#deciding range of the time period
    year,month,day = (int(x) for x in jun11.split('-'))    
    ansjun11 = datetime.date(year, month, day)
    jun12='2018-06-08'
    year,month,day = (int(x) for x in jun12.split('-'))    
    ansjun12 = datetime.date(year, month, day)
    
    jun21='2018-06-09'#deciding range of the time period
    year,month,day = (int(x) for x in jun21.split('-'))    
    ansjun21 = datetime.date(year, month, day)
    jun22='2018-06-15'
    year,month,day = (int(x) for x in jun22.split('-'))    
    ansjun22 = datetime.date(year, month, day)
    
    jun31='2018-06-16'#deciding range of the time period
    year,month,day = (int(x) for x in jun31.split('-'))    
    ansjun31 = datetime.date(year, month, day)
    jun32='2018-06-22'
    year,month,day = (int(x) for x in jun32.split('-'))    
    ansjun32 = datetime.date(year, month, day)
    
    jun41='2018-06-23'#deciding range of the time period
    year,month,day = (int(x) for x in jun41.split('-'))    
    ansjun41 = datetime.date(year, month, day)
    jun42='2018-06-30'
    year,month,day = (int(x) for x in jun42.split('-'))    
    ansjun42 = datetime.date(year, month, day)
    
    july11='2018-07-01'#deciding range of the time period
    year,month,day = (int(x) for x in july11.split('-'))    
    ansjuly11 = datetime.date(year, month, day)
    july12='2018-07-09'
    year,month,day = (int(x) for x in july12.split('-'))    
    ansjuly12 = datetime.date(year, month, day)
    
    july21='2018-07-10'#deciding range of the time period
    year,month,day = (int(x) for x in july21.split('-'))    
    ansjuly21 = datetime.date(year, month, day)
    july22='2018-07-18'
    year,month,day = (int(x) for x in july22.split('-'))    
    ansjuly22 = datetime.date(year, month, day)
  
    FileReader=csv.reader(newFile)
    
    for row in FileReader:
        if ii==0:
             ii=ii+1  
        else: 
             #print(ii)
            when=row[2]
            #print(when)
            xX=when.split("+")
            #print(xX[0])
            x=xX[0].split(" ")
            dt1=x[0]
            year,month,day = (int(x) for x in dt1.split('-'))    
            ans = datetime.date(year, month, day)
            #print(ans)
            if ansmay11<=ans and ans<=ansmay12: #and row[4]=='1':
                    holiday1["may1"]=holiday1["may1"]+1
                     #print(ans)
                    if row[4]== '1':
                        holiday2["may1"]=holiday2["may1"]+1
            elif ansmay21<=ans and ans<=ansmay22: #and row[4]=='1':
                    holiday1["may2"]=holiday1["may2"]+1
                    if row[4]== '1':
                        holiday2["may2"]=holiday2["may2"]+1
            elif ansmay31<=ans and ans<=ansmay32: #and row[4]=='1':
                    holiday1["may3"]=holiday1["may3"]+1
                    if row[4]== '1':
                        holiday2["may3"]=holiday2["may3"]+1
            elif ansjun11<=ans and ans<=ansjun12: #and row[4]=='1':
                    holiday1["jun1"]=holiday1["jun1"]+1
                    if row[4]== '1':
                        holiday2["jun1"]=holiday2["jun1"]+1
            elif ansjun21<=ans and ans<=ansjun22: #and row[4]=='1':
                    holiday1["jun2"]=holiday1["jun2"]+1
                    if row[4]== '1':
                        holiday2["jun2"]=holiday2["jun2"]+1 
            elif ansjun31<=ans and ans<=ansjun32: #and row[4]=='1':
                    holiday1["jun3"]=holiday1["jun3"]+1
                    if row[4]== '1':
                        holiday2["jun3"]=holiday2["jun3"]+1
            elif ansjun41<=ans and ans<=ansjun42: #and row[4]=='1':
                    holiday1["jun4"]=holiday1["jun4"]+1
                    if row[4]== '1':
                        holiday2["jun4"]=holiday2["jun4"]+1
            elif ansjuly11<=ans and ans<=ansjuly12: #and row[4]=='1':
                    holiday1["july1"]=holiday1["july1"]+1
                    if row[4]== '1':
                        holiday2["july1"]=holiday2["july1"]+1
            elif ansjuly21<=ans and ans<=ansjuly22: #and row[4]=='1':
                    holiday1["july2"]=holiday1["july2"]+1
                    if row[4]== '1':
                        holiday2["july2"]=holiday2["july2"]+1
            elif ansdec11<=ans and ans<=ansdec12: #and row[4]=='1':
                    holiday1["dec1"]=holiday1["dec1"]+1
                    if row[4]== '1':
                        holiday2["dec1"]=holiday2["dec1"]+1   
            elif ansdec21<=ans and ans<=ansdec22: #and row[4]=='1':
                    holiday1["dec2"]=holiday1["dec2"]+1
                    if row[4]== '1':
                        holiday2["dec2"]=holiday2["dec2"]+1
            elif ansdec31<=ans and ans<=ansdec32: #and row[4]=='1':
                    holiday1["dec3"]=holiday1["dec3"]+1
                    if row[4]== '1':
                        holiday2["dec3"]=holiday2["dec3"]+1            
                        
                        
                        
print(holiday1)                        
                
                


# In[94]:


print(holiday2)


# In[95]:


fractionholiday2["dec1"]=holiday2["dec1"]/holiday1["dec1"]
fractionholiday2["dec2"]=holiday2["dec2"]/holiday1["dec2"]
fractionholiday2["dec3"]=holiday2["dec3"]/holiday1["dec3"]
fractionholiday2["may1"]=holiday2["may1"]/holiday1["may1"]
fractionholiday2["may2"]=holiday2["may2"]/holiday1["may2"]
fractionholiday2["may3"]=holiday2["may3"]/holiday1["may3"]
fractionholiday2["jun1"]=holiday2["jun1"]/holiday1["jun1"]
fractionholiday2["jun2"]=holiday2["jun2"]/holiday1["jun2"]
fractionholiday2["jun3"]=holiday2["jun3"]/holiday1["jun3"]
fractionholiday2["jun4"]=holiday2["jun4"]/holiday1["jun4"]
fractionholiday2["july1"]=holiday2["july1"]/holiday1["july1"]
fractionholiday2["july2"]=holiday2["july2"]/holiday1["july2"]





# In[96]:


print(fractionholiday2)


# In[68]:


fraction["d11"]=dict2["Monday"]/dict1["Monday"]
fraction["d22"]=dict2["Tuesday"]/dict1["Tuesday"]
fraction["d33"]=dict2["Wednesday"]/dict1["Wednesday"]
fraction["d44"]=dict2["Thursday"]/dict1["Thursday"]
fraction["d55"]=dict2["Friday"]/dict1["Friday"]
fraction["d66"]=dict2["Saturday"]/dict1["Saturday"]
fraction["d77"]=dict2["Sunday"]/dict1["Sunday"]

fraction["j11"]=dict2["Mondayj"]/dict1["Mondayj"]
fraction["j22"]=dict2["Tuesdayj"]/dict1["Tuesdayj"]
fraction["j33"]=dict2["Wednesdayj"]/dict1["Wednesdayj"]
fraction["j44"]=dict2["Thursdayj"]/dict1["Thursdayj"]
fraction["j55"]=dict2["Fridayj"]/dict1["Fridayj"]
fraction["j66"]=dict2["Saturdayj"]/dict1["Saturdayj"]
fraction["j77"]=dict2["Sundayj"]/dict1["Sundayj"]

fraction["f11"]=dict2["Mondayf"]/dict1["Mondayf"]
fraction["f22"]=dict2["Tuesdayf"]/dict1["Tuesdayf"]
fraction["f33"]=dict2["Wednesdayf"]/dict1["Wednesdayf"]
fraction["f44"]=dict2["Thursdayf"]/dict1["Thursdayf"]
fraction["f55"]=dict2["Fridayf"]/dict1["Fridayf"]
fraction["f66"]=dict2["Saturdayf"]/dict1["Saturdayf"]
fraction["f77"]=dict2["Sundayf"]/dict1["Sundayf"]

print(fraction)
# In[52]:


fraction1["d11"]=dict2["Monday"]/dict1["Monday"]
fraction1["d22"]=dict2["Tuesday"]/dict1["Tuesday"]
fraction1["d33"]=dict2["Wednesday"]/dict1["Wednesday"]
fraction1["d44"]=dict2["Thursday"]/dict1["Thursday"]
fraction1["d55"]=dict2["Friday"]/dict1["Friday"]

fraction1["j11"]=dict2["Mondayj"]/dict1["Mondayj"]
fraction1["j22"]=dict2["Tuesdayj"]/dict1["Tuesdayj"]
fraction1["j33"]=dict2["Wednesdayj"]/dict1["Wednesdayj"]
fraction1["j44"]=dict2["Thursdayj"]/dict1["Thursdayj"]
fraction1["j55"]=dict2["Fridayj"]/dict1["Fridayj"]

fraction1["f11"]=dict2["Mondayf"]/dict1["Mondayf"]
fraction1["f22"]=dict2["Tuesdayf"]/dict1["Tuesdayf"]
fraction1["f33"]=dict2["Wednesdayf"]/dict1["Wednesdayf"]
fraction1["f44"]=dict2["Thursdayf"]/dict1["Thursdayf"]
fraction1["f55"]=dict2["Fridayf"]/dict1["Fridayf"]


# In[97]:


print(fractionholiday2)


# In[103]:


#holidays
import matplotlib.pyplot as plt

data = fractionholiday2
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\holidaysfraction.png")
plt.show()


# In[99]:


import matplotlib.pyplot as plt

data = holiday1
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\trafficvariation.png")
plt.show()


# In[100]:


import matplotlib.pyplot as plt

data = holiday2
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\traficviolation.png")
plt.show()


# In[57]:


import matplotlib.pyplot as plt

data = fraction1
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\violationvstraffic.png")
plt.show()


# In[53]:


fraction2["d66"]=dict2["Saturday"]/dict1["Saturday"]
fraction2["d77"]=dict2["Sunday"]/dict1["Sunday"]

fraction2["j66"]=dict2["Saturdayj"]/dict1["Saturdayj"]
fraction2["j77"]=dict2["Sundayj"]/dict1["Sundayj"]

fraction2["f66"]=dict2["Saturdayf"]/dict1["Saturdayf"]
fraction2["f77"]=dict2["Sundayf"]/dict1["Sundayf"]


# In[58]:


import matplotlib.pyplot as plt

data = fraction2
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\violationvstraffic.png")
plt.show()


# In[56]:


print(fraction2)


# In[54]:


import matplotlib.pyplot as plt

data = fraction
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\violationvstraffic.png")
plt.show()


# In[25]:


import matplotlib.pyplot as plt

data = dict
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\trafficandviolation.png")
plt.show()


# In[43]:


import matplotlib.pyplot as plt

data = dict1
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\traffic.png")
plt.show()


# In[44]:


import matplotlib.pyplot as plt

data = dict2
weekdays = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=weekdays)
plt.savefig("D:\\cop\\cmps_trfc_mon1\\cmps_trfc_mon\\Data\\violation.png")
plt.show()


# In[7]:


dict={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}

dict["Monday"]=dict["Monday"]+1
print(dict["Monday"])


# In[8]:


#to comapre the date
import datetime
dt='2018-11-6'
year,month,day = (int(x) for x in dt.split('-'))    
ans = datetime.date(year, month, day)
dt1='2018-11-7'
year,month,day = (int(x) for x in dt1.split('-'))    
ans1 = datetime.date(year, month, day)
print(ans1.strftime("%A"))


# In[ ]:





# In[118]:





# In[ ]:




