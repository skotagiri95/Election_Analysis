# The data we need to retrieve
#1. THe total number of votes cast
#2 A complete list of candidates who received votes
#3 The percentage of votes each candidate won 
#4 The total number of votes each candidate won 
#5 The winner of the election based on popular vote
import csv
import os
from os import path 
#path to load and save files 
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file 
with open (file_to_load) as election_data:
    #Read the file object with CSV function
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    print(headers)

#Create a filename variable to a direct or indirect path to the file 
file_to_save = os.path.join("Analysis","election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")

#1 Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
#1. Declare the empty dictionary
candidate_votes = {}

#Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the eletion results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #2 Add to the total vote count
        total_votes += 1

        Ballot_ID=row[0]
        country_name=row[1]
        candidate_name=row[2]

        # Print the candidate name from each row
        candidate_name = row[2]
 
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list 
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

        #Save the results to our text file
        with open(file_to_save, "w") as txt_file:
        
            # Print the final vote count to the terminal.
                with open= (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
                print(election_results, end="")
                # Save the final vote count to the text file.
                txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate}: {vote_percentage: 1f}% ({votes:,})\n")  

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
