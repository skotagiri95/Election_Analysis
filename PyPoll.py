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

#Create a filename variable toa direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")
