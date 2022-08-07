import csv
import os

csv_path= '../PyPoll/Resources/election_data.csv'
candidates=[]
nondupcandidates=[]

#variables for the total votes for 
votesforStock=0
votesforDegette=0
votesforDoane=0

#Variables for percentage of votes per candidates
PercentforStock=0
PercentforDegette=0
PercentforDoane=0


#opens the csv file
with open(csv_path) as handler:
    csvreader = csv.reader(handler, delimiter=",")
    csvheader = next(csvreader)   #header of csv stored
    #makes a list containing every votes candidate selected
    for item in csvreader:      
        candidates.append(item[2]) #adds the third column to candidates[]
        if item[2] == 'Charles Casper Stockham':
            votesforStock+=1
        if item[2] == 'Diana DeGette':
            votesforDegette+=1
        if item[2] == 'Raymon Anthony Doane':
            votesforDoane+=1

#prints the name of the candidates WITH NO DUPLICATES
for item in candidates:
    if item not in nondupcandidates:
        nondupcandidates.append(item)

#----Using DictReader to get number of months----------------------------------------------------------------------------------------------------
data =csv.DictReader(open('../PyPoll/Resources/election_data.csv'))       #using dictreader instead of csv.reader
numberofvotes=0
for row in data:
    numberofvotes += 1

#calculate the Percentage per Candidate 
PercentforStock = (votesforStock/numberofvotes)*100
PercentforDegette = (votesforDegette/numberofvotes)*100
PercentforDoane = (votesforDoane/numberofvotes)*100

#Winner Calculation-------------------------------------------------------------------------------------------------

winner=""
if votesforStock > votesforDegette and votesforStock > votesforDoane:
    winner= "Charles Casper Stockham"
elif votesforDegette > votesforDoane and votesforDegette > votesforStock:
    winner = "Diana DeGette"
elif votesforDoane> votesforStock and votesforDoane > votesforDegette:
    winner="Raymon Anthony Doane"
#print(winner)--- test 


#---Outputs the result information in a f string---------------------------------------------------------------------------------------------------------
output= f'''Election Results
-------------------------
Total Votes: {numberofvotes:,.0f}
# -------------------------
{nondupcandidates[0]}: {PercentforStock:.3f}% ({votesforStock:,.0f})
{nondupcandidates[1]}: {PercentforDegette:.3f}% ({votesforDegette:,.0f})
{nondupcandidates[2]}: {PercentforDoane:.3f}% ({votesforDoane:,.0f})
-------------------------
Winner: {winner}
-------------------------'''

print(output)
with open('../PyPoll/analysis/Financial_Analysis.txt','w') as file:
    file.write(output)