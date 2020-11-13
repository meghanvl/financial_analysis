#import dependencies
import os
import csv

#create path for load
csvpath = os.path.join("Resources", "election_data.csv")

#initialize variables
vote_count = 0
candidates = []
candidate_vote = {}
winner_vote = 0
Khan_vote = 0
Correy_vote = 0
Li_vote = 0
Otooley_vote = 0

#open file for reading
with open(csvpath) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=",")

   #skip the header row 
   next(csv_reader)

   #loop through to find total vote count and if candidates name is not in candidate list add it 
   for row in csv_reader:
        vote_count += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name) 
            candidate_vote[candidate_name] = 0

        #loop through and add 1 to the candidate_vote count each time candidate's name is found    
        candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1

        #calculate total votes for each candidate
        if candidate_name == "Khan":
            Khan_vote += 1
        elif candidate_name == "Correy":
            Correy_vote += 1
        elif candidate_name == "Li":
            Li_vote += 1
        else:
            Otooley_vote += 1

            #find the average and total votes for each candidate
            Khan_percent = round(Khan_vote / vote_count * 100, 2)
            Correy_percent = round(Correy_vote / vote_count *100, 2)
            Li_percent = round(Li_vote / vote_count * 100, 2)
            Otooley_percent = round(Otooley_vote / vote_count * 100, 2)

for candidate in candidates:
    votes = candidate_vote.get(candidate)
    percent_votes = round(votes / vote_count * 100)

    #find the candidate with the most votes and assign to winner candidate variable 
    if votes > winner_vote:
        winner_vote = votes
        winner_candidate = candidate
    

print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")
print(f"Khan: {Khan_percent:.3f}% ({Khan_vote})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_vote})")
print(f"Li: {Li_percent:.3f}% ({Li_vote})")
print(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_vote})")
print("----------------------------")
print(f"Winner: {winner_candidate}")
print("----------------------------")

#output to Analysis folder
txtpath = os.path.join("Analysis", "election.summary.txt")

#send to text file
with open(txtpath, "w") as file:
    file.write("Election Results" + "\n")
    file.write("----------------------------" + "\n")
    file.write(f"Total Votes: {vote_count}" + "\n")
    file.write("----------------------------" + "\n")
    file.write(f"Khan: {Khan_percent:.3f}% ({Khan_vote})" + "\n")
    file.write(f"Correy: {Correy_percent:.3f}% ({Correy_vote})" + "\n")
    file.write(f"Li: {Li_percent:.3f}% ({Li_vote})" + "\n")
    file.write(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_vote})" + "\n")
    file.write("----------------------------" + "\n")
    file.write(f"Winner: {winner_candidate}" + "\n")
    file.write("----------------------------" + "\n")