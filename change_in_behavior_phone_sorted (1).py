#!/usr/bin/env python
# coding: utf-8

# In[27]:


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

with open('/home/ajit/Desktop/sorted_updated_phone.csv', 'r') as readfile:
    filereader=csv.reader(readfile)
    dt1='2018-07-01'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ansjl1 = datetime.date(year, month, day)
    dt2='2019-08-01'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansAg1 = datetime.date(year, month, day)
    dt1='2018-09-01'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ansSe1 = datetime.date(year, month, day)
    dt2='2018-10-01'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansOc1 = datetime.date(year, month, day)
    dt1='2018-11-01'#deciding range of the time period of december:=
    year,month,day = (int(x) for x in dt1.split('-'))    
    ansNo1 = datetime.date(year, month, day)
    dt2='2018-12-01'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansDe1 = datetime.date(year, month, day)
    dt2='2018-01-01'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansJ1 = datetime.date(year, month, day)
    dt2='2018-02-01'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansF1 = datetime.date(year, month, day)
    dt2='2018-03-01'
    year,month,day = (int(x) for x in dt2.split('-'))    
    ansM1 = datetime.date(year, month, day)
    for row in filereader:
      
        if(i>=0):
            when=row[7]
            x=when.split(" ")
                
            dt=x[1]
            date=x[0]
            year,month,day = (int(x) for x in date.split('-'))    
            ans = datetime.date(year, month, day)
        
          
        
            
            if ansjl1<=ans and ans<ansAg1:
                if row[1] in d and row[3]=="1":
                    d[row[1]][0]=1+d[row[1]][0]
                else:
                    d[row[1]].append(0)
                    d[row[1]].append(0)
                    d[row[1]].append(0)
                    d[row[1]].append(0)
                    d[row[1]].append(0)
                    d[row[1]][0]=1
                    d[row[1]][1]=1
                    d[row[1]][2]=1
                    d[row[1]][3]=1
                    d[row[1]][4]=1
                    
            elif ansAg1<=ans and ans<ansSe1:
                if row[1] in d and row[3]=="1":
                    d[row[1]][1]=1+d[row[1]][1]
#                 else:
#                     d[row[1]][1]=1
            elif ansSe1<=ans and ans<ansOc1:
                if row[1] in d and row[3]=="1":
                    d[row[1]][2]=1+d[row[1]][2]
#                 else:
#                     d[row[1]][2]=1
            elif ansOc1<=ans and ans<ansNo1:
                if row[1] in d and row[3]=="1":
                    d[row[1]][3]=1+d[row[1]][3]
#                 else:
#                     d[row[1]][3]=1
            elif ansNo1<=ans and ans<ansDe1:
                if row[1] in d and row[3]=="1":
                    d[row[1]][4]=1+d[row[1]][4]
#                 else:
#                     d[row[1]][4]=1
            
                
          
                    
#                 elif 
#                     d[row[1]][1]=1+d[row[1]][1]
#                 elif 
#                     d[row[1]][2]=1+d[row[1]][2]
#                 elif 
#                     d[row[1]][3]=1+d[row[1]][3]
#                 elif 
#                     d[row[1]][4]=1+d[row[1]][4]
#                 elif ansDe1<=ans and ans<ansJ1:
#                     d[row[1]][5]=1+d[row[1]][5]
#                 elif ansJ1<=ans and ans<ansF1:
#                     d[row[1]][6]=1+d[row[1]][6]
#                 elif ansF1<=ans and ans<ansM1:
#                     d[row[1]][7]=1+d[row[1]][7]
                    
#             elif row[3]=="1":
#                 d[row[1]].append(0)
#                 d[row[1]].append(0)
#                 d[row[1]].append(0)
#                 d[row[1]].append(0)
#                 d[row[1]].append(0)
#                 d[row[1]].append(0)
#                 d[row[1]].append(0)
#                 d[row[1]].append(0)
                
                
#                 if ansjl1<=ans and ans<ansAg1:
#                     d[row[1]][0]=1
#                 elif ansAg1<=ans and ans<ansSe1:
#                     d[row[1]][1]=1
#                 elif ansSe1<=ans and ans<ansOc1:
#                     d[row[1]][2]=1
#                 elif ansOc1<=ans and ans<ansNo1:
#                     d[row[1]][3]=1
#                 elif ansNo1<=ans and ans<ansDe1:
#                     d[row[1]][4]=1
#                 elif ansDe1<=ans and ans<ansJ1:
#                     d[row[1]][5]=1
#                 elif ansJ1<=ans and ans<ansF1:
#                     d[row[1]][6]=1
#                 elif ansF1<=ans and ans<ansM1:
#                     d[row[1]][7]=1
                    
    data=d
    print(d)

    
  
    i=0
    with open('/home/ajit/Desktop/Chang_in_be_graph.csv','w') as outFile:
        fileWriter=csv.writer(outFile)
        for k in keys:
            i=i+1 
            if i<=l:
                arr.append(k)
                arr.append(data[k][0])
                arr.append(data[k][1])
                arr.append(data[k][2])
                arr.append(data[k][3])
                arr.append(data[k][4])
                #print(arr)
                fileWriter.writerow(arr)
                arr=[]
#             elif l<=i and i<=m:
       
            
                


# In[ ]:





    
            
            
        
                
        
        
                
            


# In[25]:


from collections import defaultdict
d = defaultdict(list)
d={'i':[1,2,3]}
d['i'].append(0)


# In[33]:


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

with open('/home/ajit/Desktop/sorted_updated_phone.csv', 'r') as readfile:
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
        
          
            if ansjl1<=ans and ans<ansDe1:
            
                if row[1] in d and row[3]=='1':
                    if ansjl1<=ans and ans<ansAg1:
                        d[row[1]][0]=1+d[row[1]][0]
                    if ansAg1<=ans and ans<ansSe1:
                        d[row[1]][1]=1+d[row[1]][1]
                    if ansSe1<=ans and ans<ansOc1:
                        d[row[1]][2]=1+d[row[1]][2]
                    if ansOc1<=ans and ans<ansNo1:
                        d[row[1]][3]=1+d[row[1]][3]
                    if ansNo1<=ans and ans<ansDe1:
                        d[row[1]][4]=1+d[row[1]][4]
                
                    
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
                print(data)

x=data.keys()
# array=[]
# for z in x:
#     array.append(z)
#     array.append(d[z][0])
# print(array)
    
            
            
        
                
        
        
                
            


# In[48]:




# In[ ]:





# In[18]:





# In[ ]:




# In[45]:


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

with open('/home/ajit/Desktop/sorted_updated_phone.csv', 'r') as readfile:
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
                    d[row[1]][1]=1+d[row[1]][1]
                if ansSe1<=ans and ans<ansOc1:
                    d[row[1]][2]=1+d[row[1]][2]
                if ansOc1<=ans and ans<ansNo1:
                    d[row[1]][3]=1+d[row[1]][3]
                if ansNo1<=ans and ans<ansDe1:
                    d[row[1]][4]=1+d[row[1]][4]
                
                    
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
l=len(data)
l=l/2
x=data.keys()
i=0
array=[]
with open('/home/ajit/Desktop/change_graph_31.csv','w') as newFile:
    with open('/home/ajit/Desktop/change_graph_32.csv','w') as newFile1:
    
        FileReader=csv.writer(newFile)
        FileReader1=csv.writer(newFile1)
        
        for z in x:
            if i <l:
                i=i+1
                array.append(z)
                array.append(d[z][0])
                array.append(d[z][2])
                array.append(d[z][3])
                print(array)
                FileReader.writerow(array)
                array=[]
            else:
                array.append(z)
                array.append(d[z][0])
                array.append(d[z][2])
                array.append(d[z][3])
                print(array)
                FileReader1.writerow(array)
                array=[]
                


            
            
        
                
        
        
                
            


# In[48]:




# In[ ]:





# In[18]:





# In[ ]:





# In[ ]:




