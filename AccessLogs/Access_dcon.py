# Author:      Harikrishnan G Nair
# Date:        06/13/17
# Description: This script can be used to condition the raw accesslogs received from the MongoDB server. 
#              For instructions on using the script refer to the readme file attached.
########################################################################################################

import csv
import time

#Isolate rows to be conditioned
with open("test.csv","rb") as source:
    rdr= csv.reader( source )
    with open("result.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[2], r[3], r[5], r[6], r[7]) ) #If you want to analyze additional rows


ifile = open('result.csv', 'rb')
reader = csv.reader(ifile,delimiter='\t')
ofile = open('cond_test.csv', 'wb')
writer = csv.writer(ofile, delimiter='\t')

s = ifile.read()
i = 0

#For loop to selectively find and replace unnecessary terms
for row in s:
    s = s.replace('"', '')
    s = s.replace('entryTime', '')
    s = s.replace(':{$numberLong:', '')
    s = s.replace('}', '') 
    s = s.replace('method:', '') 
    s = s.replace('result:', '')
    s = s.replace('eventImageLocation:', '')
    s = s.replace('fullName:', '')
    i=i+1

print i #reference number to check number of loops

ofile.write(s)
ifile.close()
ofile.close() 

#Calculate Unix time and save in the final format
with open("cond_test.csv","rb") as source:
    rdr= csv.reader( source )
    with open("result.csv","wb") as result:
        wtr= csv.writer( result )
        wtr.writerow(('Unlock Type', 'Status', 'Time', 'Unix Time', 'Image Location', 'Name'))
        for r in rdr:
            a = (float(r[2])/86400)+25569
            wtr.writerow( (r[0], r[1], a, r[2], r[3], r[4]) )
