# Import Modules
import os
import csv

# Module for reading CSV file
PyPollcsvpath = os.path.join("Resources","election_data.csv")

# Set the variables and lists
Total_Votes = 0
Candidate_List = []
Vote_Count = []
Vote_Percentage = []
#Count_Winner = 0
Winner = ""

# Open and Read CSV
with open (PyPollcsvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #Total_Votes += 1
    
    # Find Voters Count
    for row in csvreader: 
        Total_Votes += 1
        Candidate_Name = row[2]
        # Get each Candidate's name
       
        if Candidate_Name not in Candidate_List:
            Candidate_List.append(Candidate_Name)
            index = Candidate_List.index(row[2])
            Vote_Count.append(1) 
        else:
            index = Candidate_List.index(row[2])
            Vote_Count[index] += 1
            # Count Votes  
        #Vote_Count[Candidate_Name] = Vote_Count[Candidate_Name] + 1

    for Vote in Vote_Count:       
        Percentage = float(Vote) / float(Total_Votes) * 100
        Percentage = round(Percentage)
        Percentage = "%.3f%%" % Percentage
        Vote_Percentage.append(Percentage)

    Winner = max(Vote_Count)
    index = Vote_Count.index(Winner)
    Candidate_Won = Candidate_List[index]


        #Final_Count = f"{Candidate_Name}: {Percentage:.3f}% ({Vote})\n"
 

# Print Statements
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: " + str(Total_Votes))
print("-----------------------------------------")
for i in range(len(Candidate_List)):
    print(f"{Candidate_List[i]}: {str(Vote_Percentage[i])} ({str(Vote_Count[i])})")
print("-----------------------------------------")
print(f"Winner: {Candidate_Won}")
print("-----------------------------------------")

output_path = os.path.join("analysis","PyPoll_Analysis.txt")
with open(output_path, "w") as text:  
    text.write("Election Results" + "\n")
    text.write("------------------------------------------\n")
    text.write(str("Total Votes: " + str(Total_Votes) + "\n"))
    text.write("------------------------------------------\n")
    for i in range(len(Candidate_List)):
        text.write(f"{Candidate_List[i]}: {str(Vote_Percentage[i])} ({str(Vote_Count[i])})" + "\n")
    text.write("------------------------------------------\n")
    text.write(str(f"Winner: {Candidate_Won}") + "\n")
    text.write("------------------------------------------\n")
    
        

