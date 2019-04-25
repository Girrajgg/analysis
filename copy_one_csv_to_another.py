#!/usr/bin/env python
# coding: utf-8

# In[30]:



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
                


# In[ ]:




