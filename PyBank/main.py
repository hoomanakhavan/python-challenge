#hello

import os
import csv


csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


with open(csvpath, newline = '') as csvfile:

     csvreader = csv.reader(csvfile, delimiter =',')
     #print(csvreader)
     csv_header = next(csvreader)
     #print(f"CSV Header: {csv_header}")

x = 0
total = 0
maxvalue = 0
minvalue = 0

     for row in csvreader:
         x = x + 1
         total = total + int(row[1])

         if int(row[1]) > maxvalue:
            maxvalue = int(row[1])
            d = str(row[0])
         elif int(row[1]) < minvalue:
            minvalue = int(row[1])  
            dd = str(row[0])

print("Financial Analysis")
print("--------------------------------------")

print(f"Total Months: {x}")
print(f"Total: {total}")
print(f"Greatest Increase in Profits: {d} ({maxvalue})")
print(f"Greatest Decrease in Profits: {dd} ({minvalue})")


        
