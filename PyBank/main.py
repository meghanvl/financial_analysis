#import os

# Module for reading CSV files
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_months = []
total_amount = 0
average_change = []
greatest_increase = 0
greatest_decrease = 0
change_month = 0

with open(csvpath) as csv_file:
   print(csv_file)
   csv_reader = csv.reader(csv_file, delimiter=",")

   next(csv_reader)
   firstrow = next(csv_reader)
   total_amount = total_amount + int(firstrow[1])
   previous_month = int(firstrow[1])

   for row in csv_reader:
        total_months.append(row[0])
        total_amount += int(row[1])
        change = int(row[1]) - previous_month
        previous_month = int(row[1])
        average_change.append(change)

        if change > greatest_increase:
                greatest_increase = change
                increase_month = row[0]

        if change < greatest_decrease:
                greatest_decrease = change
                decrease_month = row[0]

average = round(sum(average_change) / len(average_change) , 2)     

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months) + 1 }")
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')

txtpath = os.path.join("Analysis", "analysis.summary.txt")

with open(txtpath, "w") as file:
        file.write("Financial Analysis" + "\n")
        file.write("----------------------------" + "\n")
        file.write(f"Total Months: {len(total_months) + 1 }" "\n")
        file.write(f'Total: ${total_amount}' "\n")
        file.write(f'Average Change: ${average}' "\n")
        file.write(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})' "\n")
        file.write(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')
        
