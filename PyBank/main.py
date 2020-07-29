


# The total number of months included in the dataset
import os
import csv

filePath = r"C:\Users\vwsim\OneDrive\Documents\python-challenge\PyBank\Homework_PyBank_Resources_budget_data.csv"

total_months = 0 
total = 0
change_list = []
greatest_increased = ["", 0]
greatest_decreased = ["", 77777777777]
 
with open(filePath) as analysis_file: 

    reader = csv.reader(analysis_file)
    header = next(reader)
    print(header)  
    change = next(reader)
    previous_row = int(change[1])
    total = total + previous_row
    total_months = total_months + 1
    #print(first_row)
    

    for row in reader:
        total_months = total_months + 1
        #print(row)
        total = total + int(row[1])
        average_change = int(row[1]) - previous_row
        previous_row = int(row[1])
        change_list.append(average_change)

        if average_change > greatest_increased[1]: 
            greatest_increased[0] = row[0]
            greatest_increased[1] = average_change
        if average_change < greatest_decreased[1]:
            greatest_decreased[0] = row[0]
            greatest_decreased[1] = average_change

average_change = sum(change_list)/len(change_list)


print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total))
print("Average Change: " + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increased))
print("Greatest Decrease in Profits: " + str(greatest_decreased))

# The average of the changes in "Profit/Losses" over the entire period


# The greatest increase in  profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period




