#import os

# Module for reading CSV files
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_months = []
total_profloss = []

with open(csvpath) as csv_file:
   print(csv_file)
   csv_reader = csv.reader(csv_file, delimiter=",")

   next(csv_file)

   for row in csv_reader:
           print(row)

           total_months.append(row[0])
           total_profloss.append(row[0])

print(f"Total Months: {len(total_months)}")




        #append total month and profit
        # total_month.append(row[0])
        # total_profit.append(row[0])