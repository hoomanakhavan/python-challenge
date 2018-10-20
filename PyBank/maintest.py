#hello

import os
import csv


csvpath = 'budget_data.csv'


with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    row = next(csvreader)
    print(f"CSV Header: {row}")
    print(row)
    print(row)



