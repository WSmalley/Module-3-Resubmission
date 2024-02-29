import os
import csv

votescount = 0
C1 = 0
D1 = 0
A1 = 0



csv_path = os.path.join('/Users/davidshetler/Downloads/Starter_Code 5/PyPoll/Resources/election_data.csv')

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        votes = row[0]
        candidates = row[2]
        votescount += 1


        if candidates == "Charles Casper Stockham":
            C1 += 1

            percentcharles = (int(C1)/int(votescount)) * 100

        if candidates == 'Diana DeGette':
            D1 += 1

            percentdiana = (int(D1) / int(votescount)) * 100

        if candidates == 'Raymon Anthony Doane':
            A1 += 1

            percentanthony = (int(A1) / int(votescount)) * 100


    if percentcharles > (percentanthony and percentdiana):
        print('Winner = Charles Casper Stockham')
    if percentdiana > (percentanthony and percentcharles):
        print('Winner = Diana DeGette')
    if percentanthony > (percentdiana and percentcharles):
        print('Winner = Raymon Anthony Doan')


print(f'Total votes: {votescount}')
print(f'percent Charles Casper Stockham : {percentcharles}% ( {C1} )')
print(f'percent Diana DeGette : {percentdiana}% ( {D1} )')
print(f'percent Raymon Anthony Doan : {percentanthony}% ( {A1} )')








print(f'Total votes: {votescount}')
print(f'percent Charles Casper Stockham : {percentcharles}% ( {C1} )')
print(f'percent Diana DeGette : {percentdiana}% ( {D1} )')
print(f'percent Raymon Anthony Doan : {percentanthony}% ( {A1} )')






