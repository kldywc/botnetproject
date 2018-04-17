import csv
import re

fields = []
rows = []

# reading csv file
with open('pro3.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)

    fields.append("avg.pkt length")
    fields.append("ipkt/opkt")
    fields.append("ibytes/obytes")
 
    # extracting each data row one by one
    for row in csvreader:
        temp=[]
        temp.append(row[0])
        temp.append(row[1])
        temp.append(row[2])
        temp.append(row[3])
        temp.append(row[4])
        temp.append(row[5])
        temp.append(row[6])
        temp.append(row[7])
        temp.append(row[8])
        temp.append(row[9])
        temp.append(row[10])
        temp.append(row[11])
        temp.append(row[12])
        temp.append(row[13])
        val= float(row[5])/ float(row[4])
        temp.append(val)
        rows.append(temp)
        val= float(row[8])/float(row[6])
        temp.append(val)
        val=float(row[9])/float(row[7])
        temp.append(val)

       
with open('features.csv', 'w') as myFile :
    writer = csv.writer(myFile)
    writer.writerow(fields)
    writer.writerows(rows)
    print("Writing complete")






