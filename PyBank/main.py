# Import Modules
import os
import csv

# Module for reading csv files
PyBankcsvpath = os.path.join("Resources","budget_data.csv")

#Set Variables and Lists to Store Data
Total_Months = 0 
Month_Profit_Change = 0 
Final_PL_Profit = 0 
End_PL_Total = 0
Average_Profit_Change = 0
Profit_Change = []
Date = []
Month_Change = []
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 99999999999]


# Open and Read CSV
with open(PyBankcsvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    Final_PL_Profit = int(first_row[1])
    Total_Months += 1
    End_PL_Total += int(first_row[1])

    for row in csvreader:
        # Check the total month
        Total_Months = Total_Months + 1

        # Check the net total
        End_PL_Total = End_PL_Total + int(row[1])

        # Calculate the monthly change in profits and Date
        Month_Profit_Change = int(row[1]) - Final_PL_Profit
        Final_PL_Profit = int(row[1])
        Profit_Change.append(Month_Profit_Change) 
        Date.append(row[0])

        if (Month_Profit_Change > Greatest_Increase[1]): 
            Greatest_Increase[0] = row[0]
            Greatest_Increase[1] = Month_Profit_Change
        if (Month_Profit_Change < Greatest_Decrease[1]):
            Greatest_Decrease[0] = row[0]
            Greatest_Decrease[1] = Month_Profit_Change
        
        # Calculate the average P/L change
Average_Profit_Change = sum(Profit_Change) / len(Profit_Change)
        
   
    # Write Print Statements
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: " + str(Total_Months))
print(f"Total: " + "$" + str(End_PL_Total))
print(f"Average Change: ${str(round(Average_Profit_Change,2))}")
print(f"Greatest Increase in Profits: {Greatest_Increase[0]} (${str(Greatest_Increase[1])})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${str(Greatest_Decrease[1])})")


# Export it to the text file
output_path = os.path.join("analysis","PyBank_analysis.txt")
with open(output_path, "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("------------------------------------------------\n")
    text.write("Total Months: " + str(Total_Months) + "\n")
    text.write("Total: " + "$" + str(End_PL_Total) + "\n")
    text.write("Average Change: " + "$" + str(round(Average_Profit_Change,2)) + "\n")
    text.write("Greatest Increase in Profits: " + str(Greatest_Increase[0]) + "$" + str(Greatest_Increase[1]) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(Greatest_Decrease[0]) + "$" + str(Greatest_Decrease[1]) + ")\n") 
    



