#!/usr/bin/env python
# coding: utf-8

# In[81]:


#copying one file to new file according to the condition
import csv
i=0
with open('/home/ajit/Desktop/onlysat.csv','w') as outFile:
    fileWriter=csv.writer(outFile)
    with open('/home/ajit/Desktop/data-1552593056171 (copy).csv','r') as newFile:
        FileReader=csv.reader(newFile)
        for row in FileReader:
            if i==0:
                i=i+1
                pass
            else:   
                when=row[2]
                x=when.split(" ")
                dt=x[0]
                year,month,day = (int(x) for x in dt.split('-'))    
                ans = datetime.date(year, month, day)
                print(ans)
                if ans.strftime("%A")=="Sunday"or ans.strftime("%A")=="Saturday":
                    fileWriter.writerow(row)
                


# In[72]:


#date time split
import datetime
with open('/home/ajit/Desktop/out3.csv','r') as outFile:
    fileWriter=csv.reader(outFile)
    #for row in fileWriter:
        
       
        when = row[2]
        x=when.split(" ")
        print(x[0])
      
        dt = 2019-03-10
        
        year,month,day = (int(x) for x in dt.split('-'))    
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))
      


# In[83]:



#sorting csv algo
import sys
import csv
i=0
reader = csv.reader(open('/home/ajit/Desktop/onlysat.csv'), delimiter=',')


sortedlist = sorted(reader, key=operator.itemgetter(2))
with open('/home/ajit/Desktop/sortedSunSat.csv', 'w') as f:
          fileWriter = csv.writer(f, delimiter=',')
          for row in sortedlist:
            fileWriter.writerow(row)
        #    '''to write in new file'''

#sortedlist = sorted(reader, key=lambda reader: reader[3], reverse=True)
#print(sortedlist)


# In[76]:


#prints day of a week like monday
import datetime
dt = '10/03/2019'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
print(ans.strftime("%A"))


# In[ ]:




