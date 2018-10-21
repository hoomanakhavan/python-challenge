#election analysis

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    x=0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for row in csvreader:
        x = x + 1
        if str(row[2]) == "Khan":
            total1 = total1 + 1         
        elif str(row[2]) == "Correy":
            total2 = total2 + 1      
        elif str(row[2]) == "Li":
            total3 = total3 + 1
        elif str(row[2]) == "O'Tooley":
           total4 = total4 + 1
       
    t1 = round((total1/x)*100, 3)
    t2 = round((total2/x)*100, 3)
    t3 = round((total3/x)*100, 3)
    t4 = round((total4/x)*100, 3)

    if t1 > t2:
        a = "Khan"
    elif t1 < t2:
        a = "Correy"
        t1 = t2

    if t1 < t3:
        t1 =t3
        a = "Li"

    if t1 < t4:
        a = "O'Tooley"

print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {x}")
print("--------------------------------------")
print(f"Khan:  {t1}%  ({total1})")
print(f"Correy:  {t2}%  ({total2})")
print(f"Li:  {t3}%   ({total3})")
print(f"O'Tooley:  {t4}%  ({total4})")

print("--------------------------------------")
print(f"Winner: {a}")
print("--------------------------------------")
        
