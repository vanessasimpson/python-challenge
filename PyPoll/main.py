import os
import csv

filePath = r"C:\Users\vwsim\OneDrive\Desktop\UTSA\utsa-san-data-pt-06-2020-u-c\Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"
total_votes = 0
candidate_votes = {}
candidate_name = []

##The total number of votes cast
with open(filePath) as analysis_file: 

    reader = csv.reader(analysis_file)
    header = next(reader)
    print(header)

# row = [234567, Marsh, Khan]    
    for row in reader:
        total_votes = total_votes + 1

        name = row[2]  
        if name not in candidate_name:
            candidate_name.append(name)
            candidate_votes[name] = 1
        else:
            candidate_votes[name] += 1

for k, v in candidate_votes.items():
    percentage = v/total_votes*100 
    print(f"{k} {percentage}").format = %
    
print("Election Results")
print("------------------")

print(candidate_votes)
print(total_votes)          

##A complete list of candidates who received votes


##The percentage of votes each candidate won


##The total number of votes each candidate won


##The winner of the election based on popular votes