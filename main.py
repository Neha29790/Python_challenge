import os
import csv



os.chdir(os.path.dirname(__file__))

print("This program is running from: " + os.getcwd())

budget_data_csv = os.path.join("..", "resources", "budget_data.csv")

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    rowNum = -1
    Total = 0
    TotalChange = 0
    previousProfitLoss = 0
    greatestInc = 0
    greatestIncLable = ""
    greatestDec = 0
    greatestDecLable = ""

    for row in csv_reader:
        rowNum = rowNum+1
        change =(int(row[1])-previousProfitLoss)
        Total = Total + int(row[1])
        TotalChange=TotalChange + change
        if rowNum ==0: TotalChange=0
        previousProfitLoss = int(row[1])
        if change > greatestInc:greatestInc=change;greatestIncLable=row[0]
        if change < greatestDec:greatestDec=change;greatestDecLable=row[0]

    print("")
    print("---------------------------------------------------------------")
    print("")
    print("Financial Analysis")
    print("")
    print("---------------------------------------------------------------")
    print("")
    print("Total Months: "+ str(rowNum+1))
    print("")
    print("Total: $"+ str(Total))
    print("")
    print("Average Change: $"+ str(round((TotalChange/rowNum),2)))
    print("")
    print("Greatest Increase in Profits: "+ greatestIncLable + " ($" +str(greatestInc)+")")
    print("")
    print("Greatest Decrease in Profits: "+ greatestDecLable + " ($" +str(greatestDec)+")")

    with open('Pybank_Analysis.txt', 'w') as f:
        f.write('\n')
        f.write("---------------------------------------------------------------")
        f.write('\n')
        f.write("Financial Analysis")
        f.write('\n')
        f.write("---------------------------------------------------------------")
        f.write('\n')
        f.write("Total Months: "+ str(rowNum+1))
        f.write('\n')
        f.write("Total: $"+ str(Total))
        f.write('\n')
        f.write("Average Change: $"+ str(round((TotalChange/rowNum),2)))
        f.write('\n')
        f.write("Greatest Increase in Profits: "+ greatestIncLable + " ($" +str(greatestInc)+")")
        f.write('\n')
        f.write("Greatest Decrease in Profits: "+ greatestDecLable + " ($" +str(greatestDec)+")")
