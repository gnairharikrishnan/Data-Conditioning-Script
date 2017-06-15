# Author:      Harikrishnan G Nair
# Date:        06/13/17
# Description: This script can be used to condition the raw MetaData received from the MongoDB server. 
#              For instructions on using the script refer to the readme file attached.
########################################################################################################

import csv
import time
import math

#Isolate rows to be conditioned
with open("test.csv","rb") as source:
    rdr= csv.reader( source )
    with open("result.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[1], r[2], r[3], r[4]) ) #If you want to analyze additional rows add row number here


ifile = open('result.csv', 'rb')
reader = csv.reader(ifile,delimiter='\t')
ofile = open('cond_test.csv', 'wb')
writer = csv.writer(ofile, delimiter='\t')

s = ifile.read()
i=0
for row in s:
    s = s.replace('"','')
    s = s.replace('dateTime', '')
    s = s.replace(':{$numberLong:', '')
    s = s.replace('}', '')
    s = s.replace('batteryVoltage', '')
    s = s.replace('batteryPercentage', '')
    s = s.replace(':', '') 
    i = i + 1

print i

ofile.write(s)
ifile.close()
ofile.close() 

#Calculate Unix time and save in the final format
with open("cond_test.csv","rb") as source:
    rdr= csv.reader( source )
    with open("result.csv","wb") as result:
        wtr= csv.writer( result )
        wtr.writerow(('Time', 'Unix Time', 'Battery Voltage', 'Percentage', '', r[4]))
        for r in rdr:
            a = ((float(r[0])/1000)/86400)+25569
            wtr.writerow( (a, r[0], r[1], r[2]) )
