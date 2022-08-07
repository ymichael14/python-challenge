import csv
import os

data =  csv.DictReader(open('../PyBank/Resources/budget_data.csv'))
months = 0
total=0
total_ch = 0
# creating list to store the increases and decreases and month/yr
inc = ['',0] 
dec = ['',0]

#stores the headers 
headers=[]
headers = data.fieldnames 
#test print(headers)

for i,row in enumerate(data):
  rev = int(row['Profit/Losses'])
  months += 1
  total += rev
  #
  if i == 0:  #first row is header so this if statement accounts for that
    pre_rev = rev 

  change = rev - pre_rev

  # Average change:
  total_ch += change
  pre_rev = rev  

  # Greatest increase:
  if change > inc[1]:
    inc[1] = change
    inc[0] = row['Date']
  #Greatest Decrease:
  if change < dec[1]:
    dec[1] = change
    dec[0] = row['Date']

#output analysis
output = f'''\n  Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: $ {total:,.2f}
  Average Change: $ {total_ch/(months-1):,.2f}
  Greatest Increase in Profits: {inc[0]} (${inc[1]:,.2f})
  Greatest Decrease in Profits: {dec[0]} (${dec[1]:,.2f}) ''' 

print(output)

with open('../PyBank/analysis/Financial_Analysis.txt', 'w') as file:
  file.write(output)