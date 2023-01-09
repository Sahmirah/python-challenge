# Import Modules
import os
import csv

# Module for reading csv files
PyBankcsvpath = os.path.join(".."/"Resources"/"budget_data.csv")

#Lists to Store Data
Total_Months = 0
#Final Total
Profit_Total = 0 
Complete_Total = [] 
Start_PL_Number = 0 
End_PL_Number = 0 
End_PL_Total = 0
PL_Difference = 0
Profit_Loss_Net = 0
Month_Change = []
Date = []


# Open and Read CSV
with open(PyBankcsvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        # Check the total month
        Total_Months = Total_Months + 1

        # Check the final P/L total
        Complete_Total.append(row[1])
        End_PL_Total = End_PL_Total + int(row[1])

        # Append the Date
        Date.append(row[0])

        # Calculate the monthly change in profits 
        End_PL_Number = int(row[1])
        Start_PL_Number = End_PL_Number
        Month_Profit_Change = End_PL_Number - Start_PL_Number
        Month_Change.append(Month_Profit_Change)

        # Calculate the Profit and Loss Difference
        PL_Difference = PL_Difference + Month_Profit_Change

        #Calculate the average P/L change
        Average_Profit_Change = (PL_Difference/Total_Months)
        
        # Calculate the greatest increase
        Greatest_Increase = max(Month_Change)
        # Calculate the greatest decrease
        Greatest_Decrease = min(Month_Change)

        # Calculate Greatest Increase Date

        # Calculate Greatest Decrease Date
   
    # Write Print Statements
    print("Financial Analysis")
    print("------------------------------------------------")
    print("Total Months: " + str(Total_Months))
    print("Total: " + "$" + str(End_PL_Total))
    print("Average Change: " + "$" + str(Average_Profit_Change))


# Export to a file (Unsure how)

   








