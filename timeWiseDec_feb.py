#!/usr/bin/env python
# coding: utf-8

# In[ ]:


dtj1='2019-01-1'#deciding range of the time period
year,month,day = (int(x) for x in dtj1.split('-'))    
ansj1 = datetime.date(year, month, day)
dtj2='2019-01-31'
year,month,day = (int(x) for x in dtj2.split('-'))    
ansj2 = datetime.date(year, month, day)


# In[44]:


import csv
i=0
with open('/home/ajit/Desktop/10rows.csv','r') as newFile:
    
    FileReader=csv.reader(newFile)
    for row in FileReader:
        if i==0:
            i=i+1
            
        else:   
            when=row[2]
            x=when.split(" ")
           # print(x[1])
            dt=x[1]
            print(dt)
            print(dt>='15:00:00' and dt<'18:00:00')
            print('True')#and row[4]=='1':
                if dt>='00:00:00' and dt<'06:00:00':
                    dict[timed1]=dict[timed1]+1
                elif dt>='06:00:00' and dt<'09:00:00':
                    dict[timed2]=dict[timed2]+1
                elif dt>='09:00:00' and dt<'12:00:00':
                    dict[timed3]=dict[timed3]+1
                elif dt>='12:00:00' and dt<'15:00:00':
                    dict[timed4]=dict[timed4]+1
                elif dt>='15:00:00' and dt<'18:00:00':
                    dict[timed5]=dict[timed5]+1
                    print(True)
                elif dt>='18:00:00' and dt<'21:00:00':
                    dict[timed6]=dict[timed6]+1
                else :
                    dict[timed7]=dict[timed7]+1
            #year,month,day = (int(x) for x in dt.split('-'))    
            #ans = datetime.date(year, month, day)


# In[59]:


import csv

i=0
#time1="0to6",time2="6to9",time3="9t012",time4="12to15",time5="15to18",time6="18to21",time7="21to12"
dict={"timed1":0,"timed2":0,"timed3":0,"timed4":0,"timed5":0,"timed6":0,"timed7":0,
      "timej1":0,"timej2":0,"timej3":0,"timej4":0,"timej5":0,"timej6":0,"timej7":0,
     "timef1":0,"timef2":0,"timef3":0,"timef4":0,"timef5":0,"timef6":0,"timef7":0}
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
            
            dt=x[1]
            date=x[0]
            year,month,day = (int(x) for x in date.split('-'))    
            ans = datetime.date(year, month, day)
            #print(dt)
            #print(dt>'15:26:49')
            #print(ans)
           # print(dt>='00:00:00' and dt<'06:00:00')
            #print(dt>='15:00:00' and dt<'18:00:00')
            if ans1<=ans and ans<=ans2 and row[4]=='1':
                
                
                if dt>='00:00:00' and dt<'06:00:00':
                    dict["timed1"]=dict["timed1"]+1
                         
                elif dt>='06:00:00' and dt<'09:00:00':
                    dict["timed2"]=dict["timed2"]+1
                elif dt>='09:00:00' and dt<'12:00:00':
                    dict["timed3"]=dict["timed3"]+1
                elif dt>='12:00:00' and dt<'15:00:00':
                    dict["timed4"]=dict["timed4"]+1
                elif dt>='15:00:00' and dt<'18:00:00':
                    dict["timed5"]=dict["timed5"]+1
                    #rint(True)
                elif dt>='18:00:00' and dt<'21:00:00':
                    dict["timed6"]=dict["timed6"]+1
                else :
                    dict["timed7"]=dict["timed7"]+1
               
            elif ansj1<=ans and ans<=ansj2 and row[4]=='1':
                #rint('true')
                if dt>='00:00:00' and dt<'06:00:00':
                    dict["timej1"]=dict["timej1"]+1
                elif dt>='06:00:00' and dt<'09:00:00':
                    dict["timej2"]=dict["timej2"]+1
                elif dt>='09:00:00' and dt<'12:00:00':
                    dict["timej3"]=dict["timej3"]+1
                    #print(dict[timej3])
                
                elif dt>='12:00:00' and dt<'15:00:00':
                    
                    dict["timej4"]=dict["timej4"]+1
                elif dt>='15:00:00' and dt<'18:00:00':
                    dict["timej5"]=dict["timej5"]+1
                elif dt>='18:00:00' and dt<'21:00:00':
                    dict["timej6"]=dict["timej6"]+1
                else :
                    dict["timej7"]=dict["timej7"]+1
                #print(dict)
            elif ansf1<=ans and ans<=ansf2 and row[4]=='1':
                if dt>='00:00:00' and dt<'06:00:00':
                    dict["timef1"]=dict["timef1"]+1
                elif dt>='06:00:00' and dt<'09:00:00':
                    dict["timef2"]=dict["timef2"]+1
                elif dt>='09:00:00' and dt<'12:00:00':
                    dict["timef3"]=dict["timef3"]+1
                elif dt>='12:00:00' and dt<'15:00:00':
                    dict["timef4"]=dict["timef4"]+1
                elif dt>='15:00:00' and dt<'18:00:00':
                    dict["timef5"]=dict["timef5"]+1
                elif dt>='18:00:00' and dt<'21:00:00':
                    dict["timef6"]=dict["timef6"]+1
                else :
                    dict["timef7"]=dict["timef7"]+1
    print(dict)
import matplotlib.pyplot as plt

data = dict
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig('bar.png')
plt.show()  


# In[ ]:




