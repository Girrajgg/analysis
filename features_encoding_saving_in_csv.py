#!/usr/bin/env python
# coding: utf-8

# In[18]:


import csv
import numpy as np
import datetime
with open('/home/ajit/Desktop/cmps_trfc_mon/Data/head_features_for_model.csv','r') as newFile:
    with open('/home/ajit/Desktop/list_in_csv.csv', 'w',newline='') as myfile:
        
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        dt1='2018-12-1'#deciding range of the time period of december:=
        year,month,day = (int(x) for x in dt1.split('-'))    
        ans1 = datetime.date(year, month, day)
        dt2='2019-02-28'
        year,month,day = (int(x) for x in dt2.split('-'))    
        ans2 = datetime.date(year, month, day)
        FileReader=csv.reader(newFile)
        for row in FileReader:
            arr=[]
        
            if i==0:
                i=i+1
            
            else:
                
                
            
                when=row[2]
                x=when.split(" ")
            
                dt=x[1]
                date=x[0]
                year,month,day = (int(x) for x in date.split('-'))    
                ans = datetime.date(year, month, day)
                ans = datetime.date(year, month, day)
                d=ans.strftime("%A")
            
            
            #print(dt)
            #print(dt>'15:26:49')
            #print(ans)
           # print(dt>='00:00:00' and dt<'06:00:00')
            #print(dt>='15:00:00' and dt<'18:00:00')
                if ans1<=ans and ans<=ans2:
                    
                    if row[7]=="1":
                        arr.append(1)
                    elif row[7]=="0":
                        arr.append(0)
                
                    if d=="Monday":
                        arr.append(1/7)
                    elif d=="Tuesday":
                        arr.append(2/7)
                    elif d=="Wednesday":
                        arr.append(3/7)
                    elif  d=="Thursday":
                        arr.append(4/7)
                    elif d=="Friday":
                        arr.append(5/7)
                    elif d=="Saturday":
                        arr.append(6/7)
                    elif d=="Sunday":
                        arr.append(6.95/7)
                
                
                
                    if dt>'00:00:00' and dt<='02:00:00':
                        
                        
                    #dict["timed1"]=dict["timed1"]+1
                        x=np.sin(3.14/6)
                        y=np.cos(3.14/6)
                        arr.append(x)
                        arr.append(y)
                         
                    elif dt>"02:00:00" and dt<="04:00:00":
                        x=np.sin(3.14*2/3)
                        y=np.cos(3.14*2/3)
                        arr.append(x)
                        arr.append(y)
                    
                    elif dt>'04:00:00' and dt<'=06:00:00':
                        x=np.sin(3.14)
                        y=np.cos(3.14)
                        arr.append(x)
                        arr.append(y)
                  
                    elif dt>'06:00:00' and dt<='08:00:00':
                        x=np.sin(3.14*4/3)
                        y=np.cos(3.14*4/3)
                        arr.append(x)
                        arr.append(y)
                    elif dt>'08:00:00' and dt<='10:00:00':
                        x=np.sin(3.14*5/3)
                        y=np.cos(3.14*5/3)
                        arr.append(x)
                        arr.append(y)
                  
                    #rint(True)
                    elif dt>'10:00:00' and dt<='12:00:00':
                        x=np.sin(3.14*6/3)
                        y=np.cos(3.14*6/3)
                        arr.append(x)
                        arr.append(y)
                    elif dt>'12:00:00' and dt<='14:00:00':
                        x=np.sin(3.14*7/3)
                        y=np.cos(3.14*7/3)
                        arr.append(x)
                        arr.append(y)
                    elif dt>'14:00:00' and dt<='16:00:00':
                        x=np.sin(3.14*8/3)
                        y=np.cos(3.14*8/3)
                        arr.append(x)
                        arr.append(y)
                    elif dt>'16:00:00' and dt<='18:00:00':
                        x=np.sin(3.14*9/3)
                        y=np.cos(3.14*9/3)
                        arr.append(x)
                        arr.append(y)
                    elif dt>'18:00:00' and dt<='20:00:00':
                        x=np.sin(3.14*10/3)
                        y=np.cos(3.14*10/3)
                        arr.append(x)
                        arr.append(y)
                    elif dt>'20:00:00' and dt<='22:00:00':
                        x=np.sin(3.14*11/3)
                        y=np.cos(3.14*11/3)
                        arr.append(x)
                        arr.append(y)
                    elif dt>'22:00:00' and dt<='24:00:00':
                        x=np.sin(3.14*12/3)
                        y=np.cos(3.14*12/3)
                        arr.append(x)
                        arr.append(y)
                    speed=row[3]
                    speed=int(speed)/100
                    arr.append(speed)
                    vtype=row[4]
                    if vtype=='-1':
                        arr.append(1/5)
                    elif vtype=='1':
                        arr.append(2/5)
                    elif vtype=='2':
                        arr.append(3/5)
                    elif vtype=='11':
                        arr.append(4/5)
                    elif vtype=='12':
                        arr.append(4.9/5)
                    gate=row[5]
                    if gate=='C00':
                        arr.append(1/4)
                    elif gate=='C01':
                        arr.append(2/4)
                    elif gate=='C07':
                        arr.append(3/4)
                    elif gate=='C08':
                        arr.append(3.9/4)
                    entry=row[6]
                    y=entry.split(" ")
                    dtt=y[1]
                    if dtt>'00:00:00' and dtt<='02:00:00':
                        
                    #dict["timed1"]=dict["timed1"]+1
                        x=np.sin(3.14/6)
                        y=np.cos(3.14/6)
                        arr.append(x)
                        arr.append(y)
                         
                    elif dtt>'02:00:00' and dtt<='04:00:00':
                        x=np.sin(3.14*2/3)
                        y=np.cos(3.14*2/3)
                        arr.append(x)
                        arr.append(y)
                    
                    elif dtt>'04:00:00' and dtt<'=06:00:00':
                        x=np.sin(3.14)
                        y=np.cos(3.14)
                        arr.append(x)
                        arr.append(y)
                  
                    elif dtt>'06:00:00' and dtt<='08:00:00':
                        x=np.sin(3.14*4/3)
                        y=np.cos(3.14*4/3)
                        arr.append(x)
                        arr.append(y)
                    elif dtt>'08:00:00' and dtt<='10:00:00':
                        x=np.sin(3.14*5/3)
                        y=np.cos(3.14*5/3)
                        arr.append(x)
                        arr.append(y)
                  
                    #rint(True)
                    elif dtt>'10:00:00' and dtt<='12:00:00':
                        x=np.sin(3.14*6/3)
                        y=np.cos(3.14*6/3)
                        arr.append(x)
                        arr.append(y)
                    elif dtt>'12:00:00' and dtt<='14:00:00':
                        x=np.sin(3.14*7/3)
                        y=np.cos(3.14*7/3)
                        arr.append(x)
                        arr.append(y)
                    elif dtt>'14:00:00' and dtt<='16:00:00':
                        x=np.sin(3.14*8/3)
                        y=np.cos(3.14*8/3)
                        arr.append(x)
                        arr.append(y)
                    elif dtt>'16:00:00' and dtt<='18:00:00':
                        x=np.sin(3.14*9/3)
                        y=np.cos(3.14*9/3)
                        arr.append(x)
                        arr.append(y)
                    elif dtt>'18:00:00' and dtt<='20:00:00':
                        x=np.sin(3.14*10/3)
                        y=np.cos(3.14*10/3)
                        arr.append(x)
                        arr.append(y)
                    elif dtt>'20:00:00' and dtt<='22:00:00':
                        x=np.sin(3.14*11/3)
                        y=np.cos(3.14*11/3)
                        arr.append(x)
                        arr.append(y)
                    elif dtt>'22:00:00' and dtt<='24:00:00':
                        x=np.sin(3.14*12/3)
                        y=np.cos(3.14*12/3)
                        arr.append(x)
                        arr.append(y)
                    print(arr)
                    wr.writerow(arr)
    
   
    


 


# In[11]:


import csv
import numpy as np
import datetime
i=0
#time1="0to6",time2="6to9",time3="9t012",time4="12to15",time5="15to18",time6="18to21",time7="21to12"

with open('/home/ajit/Desktop/cmps_trfc_mon/Data/head_features_for_model.csv','r') as newFile:
    
    dt1='2018-12-1'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ans1 = datetime.date(year, month, day)
    dt2='2019-02-28'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ans2 = datetime.date(year, month, day)
    
    
    
    #deciding range of the time period of january:=
    dtj1='2019-01-1'#deciding range of the time period//
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
        arr=[]
        
        if i==0:
            i=i+1
            
        else: 
            
            when=row[2]
            x=when.split(" ")
            
            dt=x[1]
            date=x[0]
            year,month,day = (int(x) for x in date.split('-'))    
            ans = datetime.date(year, month, day)
            ans = datetime.date(year, month, day)
            d=ans.strftime("%A")
            
            
            #print(dt)
            #print(dt>'15:26:49')
            #print(ans)
           # print(dt>='00:00:00' and dt<'06:00:00')
            #print(dt>='15:00:00' and dt<'18:00:00')
            if ans1<=ans and ans<=ans2:
                if row[7]=="1":
                    arr.append(1)
                elif row[7]=="0":
                    arr.append(0)
                
                if d=="Monday":
                    arr.append(1/7)
                elif d=="Tuesday":
                    arr.append(2/7)
                elif d=="Wednesday":
                    arr.append(3/7)
                elif d=="Thursday":
                    arr.append(4/7)
                elif d=="Friday":
                    arr.append(5/7)
                elif d=="Saturday":
                    arr.append(6/7)
                elif d=="Sunday":
                    arr.append(6.95/7)
                
                
                
                if dt>'00:00:00' and dt<='02:00:00':
                    #dict["timed1"]=dict["timed1"]+1
                    x=np.sin(3.14/6)
                    y=np.cos(3.14/6)
                    arr.append(x)
                    arr.append(y)
                         
                elif dt>"02:00:00" and dt<="04:00:00":
                    x=np.sin(3.14*2/3)
                    y=np.cos(3.14*2/3)
                    arr.append(x)
                    arr.append(y)
                    
                elif dt>'04:00:00' and dt<'=06:00:00':
                    x=np.sin(3.14)
                    y=np.cos(3.14)
                    arr.append(x)
                    arr.append(y)
                  
                elif dt>'06:00:00' and dt<='08:00:00':
                    x=np.sin(3.14*4/3)
                    y=np.cos(3.14*4/3)
                    arr.append(x)
                    arr.append(y)
                elif dt>'08:00:00' and dt<='10:00:00':
                    x=np.sin(3.14*5/3)
                    y=np.cos(3.14*5/3)
                    arr.append(x)
                    arr.append(y)
                  
                    #rint(True)
                elif dt>'10:00:00' and dt<='12:00:00':
                    x=np.sin(3.14*6/3)
                    y=np.cos(3.14*6/3)
                    arr.append(x)
                    arr.append(y)
                elif dt>'12:00:00' and dt<='14:00:00':
                    x=np.sin(3.14*7/3)
                    y=np.cos(3.14*7/3)
                    arr.append(x)
                    arr.append(y)
                elif dt>'14:00:00' and dt<='16:00:00':
                    x=np.sin(3.14*8/3)
                    y=np.cos(3.14*8/3)
                    arr.append(x)
                    arr.append(y)
                elif dt>'16:00:00' and dt<='18:00:00':
                    x=np.sin(3.14*9/3)
                    y=np.cos(3.14*9/3)
                    arr.append(x)
                    arr.append(y)
                elif dt>'18:00:00' and dt<='20:00:00':
                    x=np.sin(3.14*10/3)
                    y=np.cos(3.14*10/3)
                    arr.append(x)
                    arr.append(y)
                elif dt>'20:00:00' and dt<='22:00:00':
                    x=np.sin(3.14*11/3)
                    y=np.cos(3.14*11/3)
                    arr.append(x)
                    arr.append(y)
                elif dt>'22:00:00' and dt<='24:00:00':
                    x=np.sin(3.14*12/3)
                    y=np.cos(3.14*12/3)
                    arr.append(x)
                    arr.append(y)
                speed=row[3]
                speed=int(speed)/100
                arr.append(speed)
                vtype=row[4]
                if vtype=='-1':
                    arr.append(1/5)
                elif vtype=='1':
                    arr.append(2/5)
                elif vtype=='2':
                    arr.append(3/5)
                elif vtype=='11':
                    arr.append(4/5)
                elif vtype=='12':
                    arr.append(4.9/5)
                gate=row[5]
                if gate=='C00':
                    arr.append(1/4)
                elif gate=='C01':
                    arr.append(2/4)
                elif gate=='C07':
                    arr.append(3/4)
                elif gate=='C08':
                    arr.append(3.9/4)
                entry=row[6]
                y=entry.split(" ")
                dtt=y[1]
                if dtt>'00:00:00' and dtt<='02:00:00':
                    #dict["timed1"]=dict["timed1"]+1
                    x=np.sin(3.14/6)
                    y=np.cos(3.14/6)
                    arr.append(x)
                    arr.append(y)
                         
                elif dtt>'02:00:00' and dtt<='04:00:00':
                    x=np.sin(3.14*2/3)
                    y=np.cos(3.14*2/3)
                    arr.append(x)
                    arr.append(y)
                    
                elif dtt>'04:00:00' and dtt<'=06:00:00':
                    x=np.sin(3.14)
                    y=np.cos(3.14)
                    arr.append(x)
                    arr.append(y)
                  
                elif dtt>'06:00:00' and dtt<='08:00:00':
                    x=np.sin(3.14*4/3)
                    y=np.cos(3.14*4/3)
                    arr.append(x)
                    arr.append(y)
                elif dtt>'08:00:00' and dtt<='10:00:00':
                    x=np.sin(3.14*5/3)
                    y=np.cos(3.14*5/3)
                    arr.append(x)
                    arr.append(y)
                  
                    #rint(True)
                elif dtt>'10:00:00' and dtt<='12:00:00':
                    x=np.sin(3.14*6/3)
                    y=np.cos(3.14*6/3)
                    arr.append(x)
                    arr.append(y)
                elif dtt>'12:00:00' and dtt<='14:00:00':
                    x=np.sin(3.14*7/3)
                    y=np.cos(3.14*7/3)
                    arr.append(x)
                    arr.append(y)
                elif dtt>'14:00:00' and dtt<='16:00:00':
                    x=np.sin(3.14*8/3)
                    y=np.cos(3.14*8/3)
                    arr.append(x)
                    arr.append(y)
                elif dtt>'16:00:00' and dtt<='18:00:00':
                    x=np.sin(3.14*9/3)
                    y=np.cos(3.14*9/3)
                    arr.append(x)
                    arr.append(y)
                elif dtt>'18:00:00' and dtt<='20:00:00':
                    x=np.sin(3.14*10/3)
                    y=np.cos(3.14*10/3)
                    arr.append(x)
                    arr.append(y)
                elif dtt>'20:00:00' and dtt<='22:00:00':
                    x=np.sin(3.14*11/3)
                    y=np.cos(3.14*11/3)
                    arr.append(x)
                    arr.append(y)
                elif dtt>'22:00:00' and dtt<='24:00:00':
                    x=np.sin(3.14*12/3)
                    y=np.cos(3.14*12/3)
                    arr.append(x)
                    arr.append(y)
                print(arr)
                    


# In[ ]:




