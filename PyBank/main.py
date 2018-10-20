# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total = 0
    x = 0
    maxvalue = 0
    minvalue =0

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        x += 1
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

