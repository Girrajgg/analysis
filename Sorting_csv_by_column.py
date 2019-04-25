#!/usr/bin/env python
# coding: utf-8

# In[21]:



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


# In[ ]:




