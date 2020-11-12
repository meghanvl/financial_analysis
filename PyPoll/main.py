import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

vote_count = 0
candidates = []
candidate_vote = {}
winner_vote = 0
Khan_vote = 0
Correy_vote = 0
Li_vote = 0
Otooley_vote = 0

with open(csvpath) as csv_file:
   
   csv_reader = csv.reader(csv_file, delimiter=",")

   next(csv_reader)

   for row in csv_reader:
        vote_count += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name) 
            candidate_vote[candidate_name] = 0

        #adding 1 to the candidate_vote count each time name is found    
        candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1

        if candidate_name == "Khan":
            Khan_vote += 1
        elif candidate_name == "Correy":
            Correy_vote += 1
        elif candidate_name == "Li":
            Li_vote += 1
        else:
            Otooley_vote += 1

            Khan_percent = round(Khan_vote / vote_count * 100, 2)
            # Khan_percent = "{:.3%}".format(Khan_percent)
            Correy_percent = round(Correy_vote / vote_count *100, 2)
            Li_percent = round(Li_vote / vote_count * 100, 2)
            Otooley_percent = round(Otooley_vote / vote_count * 100, 2)
    
            
       

for candidate in candidates:
    votes = candidate_vote.get(candidate)
    percent_votes = round(votes / vote_count * 100)
    
    if votes > winner_vote:
        winner_vote = votes
        winner_candidate = candidate
    




print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")
print(f"Khan: {Khan_percent}% ({Khan_vote})")
print(f"Correy: {Correy_percent}00% ({Correy_vote})")
print(f"Li: {Li_percent}00% ({Li_vote}) ")
print(f"O'Tooley: {Otooley_percent}00% ({Otooley_vote}) ")
print("----------------------------")
print(f"Winner: {winner_candidate}")
print("----------------------------")

txtpath = os.path.join("Analysis", "election.summary.txt")

with open(txtpath, "w") as file:
    file.write("Election Results" + "\n")
    file.write("----------------------------" + "\n")
    file.write("Total Votes:" + "\n")
    file.write("----------------------------" + "\n")
    file.write("Khan: " + "\n")
    file.write("Correy: " + "\n")
    file.write("Li: " + "\n")
    file.write("O'Tooley: " + "\n")
    file.write("----------------------------" + "\n")
    file.write("Winner: " + "\n")
    file.write("----------------------------" + "\n")