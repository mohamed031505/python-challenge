
import os
import csv
from collections import defaultdict
total_votes = 0
candidates = {}
i = 0
candidate_name = []
candidate_votes = []
candidates_percentage = []

csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:

        total_votes += 1
        
        if row[2] in candidates:
            
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
    


winner = max(candidates.items(), key=lambda x: x[1])
least_votes = min(candidates.items(), key=lambda x: x[1])

highest_percentage = (int(winner[1]) / int(total_votes)) * 100
least_percentage = (int(least_votes[1]) / int(total_votes)) * 100

candidate_name = list(candidates.keys())
candidate_votes = list (candidates.values())


for i in range(len(candidate_votes)):
    
    candidates_percentage.append(((int(candidate_votes[i]) / total_votes) * 100))






print ( "Election Results")
print ( "----------------------")
print ("Total Votes : " +str(total_votes))
print ("----------------------")
for i in range(len(candidate_votes)):
    
    candidates_percentage.append(((int(candidate_votes[i]) / total_votes) * 100))

    print ( str(candidate_name[i]) + " : " + str(candidates_percentage[i]) + "% " + "("+str(candidate_votes[i])+")")
print ( "----------------------")
print ("The Winner Candidate is : " + winner[0])
print ( "----------------------")




# print (str(winner[0])+ " : " + str(highest_percentage)+"%"+" " +"(" +str(winner[1])+")")
# print (str(winner[0])+ " : " + str(highest_percentage)+"%"+" " +"(" +str(winner[1])+")")
# print (str(winner[0])+ " : " + str(highest_percentage)+"%"+" " +"(" +str(winner[1])+")")
# print (str(least_votes[0])+ " : " + str(least_percentage)+"%"+ " " +"(" +str(least_votes[1])+")")








#   Election Resultsw
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

with open("Pypoll.txt","w") as txt_file:

    txt_file.write("Election Results:\n")
    txt_file.write("------------------------------\n")
    txt_file.write("Total Votes: " + str(total_votes) +"\n")
    txt_file.write("------------------------------\n")
    txt_file.write(str(winner[0])+ " : " + str(highest_percentage)+"%"+" " +"(" +str(winner[1])+")"+"\n")
    txt_file.write(str(candidate_name[1]) + " : " + str(candidates_percentage[1]) + "% " + "("+str(candidate_votes[1])+")" + "\n")
    txt_file.write(str(candidate_name[2]) + " : " + str(candidates_percentage[2]) + "% " + "("+str(candidate_votes[2])+")" + "\n")
    txt_file.write(str(least_votes[0])+ " : " + str(least_percentage)+"%"+ " " +"(" +str(least_votes[1])+")"+"\n")
    txt_file.write("------------------------------\n")
    txt_file.write("Winner: "+ winner[0]+ "\n")
    txt_file.write("------------------------------\n")

    
