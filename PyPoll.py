# Psuedo code for completing this task
    # import data into python in forms of table
    # calculate the number of different candidates
    # calculate the number of votes cast
    # calculate the number of votes received by each candidate
    # calculete the percentage of votes received by each candidate
    # find the candidate who got the highest percentage of votes

#Dependencies
import csv
import os  

# assign a variable to read the file
file_to_load = os.path.join('Resources','election_results.csv')

# assign a variable to write the file
file_to_save = os.path.join('Analysis','election_analysis.txt')

total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    #read the opened file
    read_file = csv.reader(election_data)

    #Print the header row
    headers = next(read_file)
    

    #Iterate through the file
    for row in read_file:
        #Count the total votes
        total_votes += 1
        # Find candidates in the list
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1
    with open(file_to_save,'w') as txt_file:

        election_results = (
            f'Election Results\n'
            f'-----------------------\n'
            f'Total Votes : {total_votes:,}\n'
            f'-----------------------\n')
        print(election_results,end="")
        
        # Save the vote count to the text file
        txt_file.write(election_results)
    
        #Determine Percentage of votes for each candidate
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/float(total_votes)*100

            #Print stats for each candidate
            candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,}) \n')
            print(candidate_results)
            # Save the candidate result to the txt file
            txt_file.write(candidate_results)

            # Determine winning votes and candidiate
            if votes > winning_count and vote_percentage > winning_percentage:
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

            
        winning_candidate_summary = (
            f'-----------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'-----------------------\n')
        print(winning_candidate_summary)
        #Save the final reults in the txt file
        txt_file.write(winning_candidate_summary)