
#********Steps:
# Read CSV
# Count total votes, and store 
# Create dict of candidates 
# Add entries to dict as CSV is read
#   --check for existing candidate
#   --if yes, increment vote for candidate
#   --if no, update candidate dict with new entry
# Print output to term + file in for loop through dict

#Notes: does dataset have any null lines?

#********import modules
import os
import csv

#********Read CSV
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header, to get entire csv
    #get just Candidates column into a list
    candidatedata = [row[2] for row in csvreader]

#********Count total votes, and store 
# Create dict of candidates 


#Declare dict var
#will take form 'Candidate' : votes, where votes is int
candidate_votes = {} 

# Add entries to dict from list created in CSV read
#   --check for existing candidate
#   --if yes, increment vote for candidate
#   --if no, update candidate dict with new entry
for row in candidatedata:
    if row in candidate_votes:
        candidate_votes[row] = candidate_votes[row] + 1
    else:    
        candidate_votes[row] = 1


#********Print output to term + file in for loop through dict
#use this format per readme:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

#check on csv read in to dict
#print(candidate_votes)

#Tally total votes
totalvotes = len(candidatedata)

print("Election Results")
print("______________________")
print(f"Total Votes: {totalvotes}")
print("______________________")

#Loop through dict to display results
for cand in candidate_votes:
    print(f"{cand}: {candidate_votes[cand]/totalvotes*100:.3f}% ({candidate_votes[cand]})")

print("______________________")

#Determine winner and print
#use format: max_key = max(a_dictionary, key=a_dictionary.get)
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")


    