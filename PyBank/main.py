# Import modules/libraries/dependencies
import csv
import os

# Lists to store data
date = []
profit_losses = []
profit = []
txt_file = []

def new_print(results):
    print(results)
    txt_file.append(str(results))

# Print report header
new_print("Financial Analysis")
new_print("------------------------------")

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources','budget_data.csv')

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
     
    # Read the header row first
    csv_header = next(csv_reader)  
    
    # Add into the created lists
    for row in csv_reader:
        date.append(row[0])
        profit_losses.append(int(row[1]))

    # Calculate the number of months in the dataset
    total_months = len(date)
    new_print("Total Months: " + str(total_months))

    # Calculate the net total amount of "Profit/Losses"
    total = sum(profit_losses)
    new_print("Total: $" + str(total))

    # Calculate the changes in "Profit/Losses" over the entire period
    changes = int((profit_losses[-1]) - (profit_losses[0]))
    avg_change = round(changes / (total_months - 1),2)
    new_print("Average Change: $" + str(avg_change))

    # Calculate the profit_losses difference and add into the list 'profit'
    for i in range(1,len(profit_losses)):
        profit.append(int(profit_losses[i] - profit_losses[i-1]))
     
    # Print the Gratest Increase in Profit
    max_date = date[(profit.index(max(profit))) + 1]
    new_print("Gratest Increase in Profits: " + max_date + " ($" + str(max(profit)) + ")")

    # Print the Greatest Deacrease in Profit
    min_date = date[(profit.index(min(profit))) + 1]
    new_print("Gratest Increase in Profits: " + min_date + " ($" + str(min(profit)) + ")")

# Export a text file with the results
output_file = os.path.join("Analysis", "PyBank_results.txt")
with open(output_file,"w") as results:
    results.writelines('\n'.join(txt_file))
