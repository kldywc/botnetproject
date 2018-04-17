import csv
import re

fields = []
rows = []

# reading csv file
with open('pro4.csv', 'r+') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    
 
    # extracting each data row one by one
    i=0
    for row in csvreader:
        if(i!=0):
          row[14]=float(row[5])/float(row[4])
        i=1
'''        
fields=['Source IP','Destination IP','Protocol','Query','Reply']
with open('output7.csv', 'w') as myFile :
    writer = csv.writer(myFile)
    writer.writerow(fields)
    writer.writerows(rows)
'''
     
print("Writing complete")






