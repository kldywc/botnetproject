import csv
import re

fields = []
rows = []

# reading csv file
with open('dns.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        temp=[]
        temp.append(row[2])
        temp.append(row[3])
        temp.append(row[4])
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', row[6] )
        for i in ip:
            temp.append(i)
        if ip:
            rows.append(temp)

fields=['Source IP','Destination IP','Protocol','Reply']
with open('output5.csv', 'w') as myFile :
    writer = csv.writer(myFile)
    writer.writerow(fields)
    writer.writerows(rows)

     
print("Writing complete")






