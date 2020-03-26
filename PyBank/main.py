
#********Instructions
#In this challenge, you are tasked with creating a Python script for analyzing the financial records 
# of your company. You will give a set of financial data called budget_data.csv. The dataset is composed 
# of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting 
# so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# --The total number of months included in the dataset
# --The net total amount of "Profit/Losses" over the entire period
# --The average of the changes in "Profit/Losses" over the entire period
# --The greatest increase in profits (date and amount) over the entire period
# --The greatest decrease in losses (date and amount) over the entire period
# As an example, your analysis should look similar to the one below:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file 
# with the results.

#********Steps
#Read CSV
#Put columns into lists
#Find difference (delta) of previous month for each month, and store in a new list
#Print to terminal
#Print to file




#********import modules
import os
import csv
import statistics


#********Read CSV
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Can skip Read the header row first because DictReader method incl this
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # Read each row of data after the header into a list
    data = [row for row in csvreader]
    
    #Put columns into their own lists, dates and pl (profit loss)
    dates = [i[0] for i in data]
    pl = [int(j[1]) for j in data]

# print(data)
# print(dates)
#print(pl)
#print(datesandpl[0][0])
#*********Find difference (delta) of previous month for each month, and store in a new list

#Declare new list to store difference
difference = []

#Loop through pl and store the difference, starting with second entry...I'm not sure why this works!
prev_month = pl[0]
for i in range(len(pl)):
    difference.append(pl[i] - prev_month)
    prev_month = pl[i]

#print(difference)

#**********Print to terminal
print("\nFinancial Analysis")
print("----------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total: ${sum(pl)}")
print(f"Average  Change: ${(sum(difference)/(len(difference)-1)):.2f}")

#Get greatest increase and decrease using max/min function, and retrieving month from its index
greatest_inc = max(difference)
greatest_inc_month = dates[difference.index(greatest_inc)]
#print(greatest_inc, greatest_inc_month)
greatest_dec = min(difference)
#print(greatest_dec)
greatest_dec_month = dates[difference.index(greatest_dec)]
#print(greatest_dec_month)
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")

#**********Print to file
#********send to new file
with open('financial_analysis.txt', 'w') as outputfile:
    outputfile.write("Financial Analysis, by Ian Mac Moore, v1, 3/25/20\n")
    outputfile.write("----------------------------\n")
    outputfile.write(f"Total Months: {len(dates)}\n")
    outputfile.write(f"Total: ${sum(pl)}\n")
    outputfile.write(f"Average  Change: ${(sum(difference)/(len(difference)-1)):.2f}\n")
    outputfile.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n")
    outputfile.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n")
