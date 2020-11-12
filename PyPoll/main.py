import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

vote_count = 0
candidates = []
candidate_vote = {}

with open(csvpath) as csv_file:
   
   csv_reader = csv.reader(csv_file, delimiter=",")

   next(csv_file)

   for row in csv_reader:
    
        vote_count += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name) 
            candidate_vote[candidate_name] = 0
        candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1 #adding 1 to the candidate_vote count each time name is found
# print(candidate_vote, candidates, vote_count)

for candidate in candidates:
    votes = candidate_vote.get(candidate)
    percent_votes = round(votes / vote_count *100, 2)
    print(percent_votes)



