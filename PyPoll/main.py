import os
import csv

csvpath = os.path.join("Resources", "election.csv")

total_count = []
candidates = []

with open(csvpath) as csv_file:
   print(csv_file)
   csv_reader = csv.reader(csv_file, delimiter=",")

   next(csv_file)

   for row in csv_reader:
           print(row)
