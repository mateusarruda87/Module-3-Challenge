# Import modules/libraries/dependencies
import csv
import os
import pandas as pd

# Lists to store data
txt_file =[]
id = []
candidate = []

# Define a function to print all results on Terminal and .txt file
def new_print(results):
    print(results)
    txt_file.append(str(results))

# Print report header
new_print("Election Results")
new_print("------------------------------")

# Path to collect data from Resources folder
election_data_csv = os.path.join('Resources','election_data.csv')

# Open and read csv
with open (election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Reade the header row first
    csv_header = next(csv_reader)

    # Add into the created lists
    for row in  csv_reader:
        id.append(str(row[0]))
        candidate.append(row[2])

    # Calculate the number of votes
    total_votes = int(len(id))
    new_print("Total Votes: " + str(total_votes))
    new_print("------------------------------")

    # List of candidates and their votes
    def count_occurrence(a):
        list_candidates = {}
        for x in a:
            if x in list_candidates:
                list_candidates[x] += 1
            else:
                list_candidates[x] = 1
        return list_candidates

    candidates = list(count_occurrence(candidate).keys())
    votes = list(count_occurrence(candidate).values())
    
    # Calculate the percentage of votes and print the results
    percentage = []
    n = int(len(candidates))
    i = 0
  
    while i < n:
        percentage.append(round((votes[i] / total_votes) * 100,3))
        new_print(str(candidates[i]) + ": " + str(percentage[i]) + "% (" + str(votes[i]) + ")")
        i += 1
    new_print("------------------------------")

    # Define the winner of the election
    winner = int(votes.index(max(votes)))
    new_print("Winner: " + str(candidates[winner]))
    new_print("------------------------------")
        
# Export a text file with the results
output_file = os.path.join("Analysis", "PyPoll_results.txt")
with open(output_file,"w") as results:
    results.writelines('\n'.join(txt_file))