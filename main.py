import os
import csv
from operator import attrgetter


class Candidate: 
    def __init__(self, name, votePercentage=0, totalVotes=0): 
        self.name = name 
        self.votePercentage = votePercentage
        self.totalVotes = totalVotes
    def addTotalVotes(self, totalVotes='nil'):
        if totalVotes != 'nil':
            self.totalVotes = self.totalVotes + totalVotes
    def calcVotePercentage(self, allVotes='nil'):
        if allVotes != 'nil':
            self.votePercentage = round((self.totalVotes/allVotes)*100,3)
        


os.chdir(os.path.dirname(__file__))

print("This program is running from: " + os.getcwd())

election_data_csv = os.path.join("..", "resources", "election_data.csv")
    
listOfCandidates = [] 

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    rowNum = 0


    for row in csv_reader:
        rowNum = rowNum+1
        candidate = next((person for person in listOfCandidates if person.name == row[2]),None,)
        if candidate == None: 
            candidate = Candidate(row[2])
            candidate.addTotalVotes(1)
            listOfCandidates.append(candidate)
        else:
            candidate.addTotalVotes(1)

with open('Poll_Analysis.txt', 'w') as f:
    print("")
    f.write('\n')
    print("---------------------------------------------------------------")
    f.write("---------------------------------------------------------------")
    print("")
    f.write('\n')
    print("Election Results")
    f.write("Election Results")
    print("")
    f.write('\n')
    print("---------------------------------------------------------------")
    f.write("---------------------------------------------------------------")
    print("")
    f.write('\n')
    print("Total Votes: "+ str(rowNum))
    f.write("Total Votes: "+ str(rowNum))
    print("")
    f.write('\n')
    if len(listOfCandidates) > 0:
        for x in listOfCandidates:
            x.calcVotePercentage(rowNum)
            print(x.name + ": "+ str(x.votePercentage) + "% ("+ str(x.totalVotes) + ")")
            f.write(x.name + ": "+ str(x.votePercentage) + "% ("+ str(x.totalVotes) + ")")
            print("")
            f.write('\n')
        print("---------------------------------------------------------------")
        f.write("---------------------------------------------------------------")
        print("")
        f.write('\n')
        winner = max(listOfCandidates, key=attrgetter('totalVotes'))
        print("Winner: "+ winner.name )
        f.write("Winner: "+ winner.name )
        print("")
        f.write('\n')
        print("---------------------------------------------------------------")
        f.write("---------------------------------------------------------------")