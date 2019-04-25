#!/usr/bin/env python
# coding: utf-8

# In[39]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

            

import csv

i=0
#time1="0to6",time2="6to9",time3="9t012",time4="12to15",time5="15to18",time6="18to21",time7="21to12"
dict={"type1d":0,"type2d":0,"type11d":0,"type12d":0,"type-1d":0,
     "type1j":0,"type2j":0,"type11j":0,"type12j":0,"type-1j":0,
     "type1f":0,"type2f":0,"type11f":0,"type12f":0,"type-1f":0}
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
            #11,1,-1,12,2
            if ans1<=ans and ans<=ans2 and row[4]=='1':
                
                
                if row[11]=='1':
                    dict["type1d"]=dict["type1d"]+1
                         
                elif row[11]=='2':
                    dict["type2d"]=dict["type2d"]+1
                elif row[11]=='11':
                    dict["type11d"]=dict["type11d"]+1
                elif row[11]=='-1':
                    dict["type-1d"]=dict["type-1d"]+1
                elif row[11]=='12':
                    dict["type12d"]=dict["type12d"]+1
                    #rint(True)
              
               
            elif ansj1<=ans and ans<=ansj2 and row[4]=='1':
                
                if row[11]=='1':
                    dict["type1j"]=dict["type1j"]+1
                         
                elif row[11]=='2':
                    dict["type2j"]=dict["type2j"]+1
                elif row[11]=='11':
                    dict["type11j"]=dict["type11j"]+1
                elif row[11]=='-1':
                    dict["type-1j"]=dict["type-1j"]+1
                elif row[11]=='12':
                    dict["type12j"]=dict["type12j"]+1
                    #rint(True)
               #
            elif ansf1<=ans and ans<=ansf2 and row[4]=='1':
                
                if row[11]=='1':
                    dict["type1f"]=dict["type1f"]+1
                         
                elif row[11]=='2':
                    dict["type2f"]=dict["type2f"]+1
                elif row[11]=='11':
                    dict["type11f"]=dict["type11f"]+1
                elif row[11]=='-1':
                    dict["type-1f"]=dict["type-1f"]+1
                elif row[11]=='12':
                    dict["type12f"]=dict["type12f"]+1
                    #rint(True)
               # elif dt>='18:00:00' and dt<'21:00:00':
               
    print(dict)
import matplotlib.pyplot as plt

data = dict
time = list(data.keys())
violations = list(data.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),violations,tick_label=time)
plt.savefig('bar.png')
print(plt.show())


# In[ ]:




# In[ ]:




