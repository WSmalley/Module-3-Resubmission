    #import peramiters
import os
import csv

# Set variables we are trying to count and set to zero
monthscount = 0
total = 0
totalchange = 0
count = 0
maxchange = 0
minchange = 0
prev_profitloss = True

csv_path = os.path.join('/Users/davidshetler/Downloads/Starter_Code 5/PyBank/Resources/budget_data.csv') #path
 #read csv minus headers
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
# run loop to count different variables etc..
    for row in csvreader:
        months = row[0]
        profitloss = int(row[1])

        if prev_profitloss is not True:
            change = profitloss - prev_profitloss
            totalchange += change
            count += 1

            if change > maxchange:
                maxchange = change
                max_month = months

            if change < minchange:
                minchange = change
                min_month = months

        prev_profitloss = profitloss  

        monthscount += 1
        total += profitloss  

if count > 0:
    average_change = totalchange / count
else:
    average_change = 0



#print all outcomes


print(f'Total months: {monthscount}')
print(f'Total profit/loss: {total}')
print(f"Average Change in Profit/Losses: {average_change}")
print(f'Max Change: {maxchange} on {str(max_month)}')
print(f'Max Change: {minchange} on {str(min_month)}')