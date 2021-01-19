
import os
import csv

number_months = 0
tolal_profilt_losses = 0
sum_change = 0 
previous = 0
change = 0 
change_values = []
greatest_increas = 0
greatest_decrease = 0



csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        number_months += 1
        tolal_profilt_losses += int(row[1])
        if number_months > 1:
            
            change = int(row[1]) - previous

            sum_change += change 
             
            change_values.append(change)
        
            
        previous = int(row[1])
        


average = sum_change / (number_months-1)
print (number_months)
print ("$"+str(tolal_profilt_losses))
print(average)


print(max(change_values))
print(min(change_values))






with open("Pybank.txt","w") as txt_file:

    txt_file.write("Summary:\n")
    txt_file.write("------------------------------\n")
    txt_file.write("Total Months : " + str(number_months)+"\n")
    txt_file.write ("Total : "+ "$"+str(tolal_profilt_losses)+"\n")
    txt_file.write ("Greatest Increase in Profits: "+"$"+str(max(change_values))  + "\n")
    txt_file.write ("Greatest Decrease in Profits: "+"$"+str(min(change_values))  + "\n")

