#Import dependencies - OS, Csv
import os
import csv

#import files from the PyBoss folder



def pyBank(filepath):
    #Declare variables and lists
    revenue = 0
    firstLine = True
    maxRevenue = 0
    minRevenue = 0
    diffList = []
    rows = []

    #open file and read data
    with open(filepath, newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        #calculate number of months in the list of csv file
        num_months = len(list(csv.reader(open(filepath))))-1
        
        #Set indexes
        index = 0
        previous_revenue = 0

        #Loop through rows in csv file from the second row forward
        for row in csvreader:
            index +=1
            if firstLine:
                firstLine = False
                continue

            # append the row to the rows
            rows.append(row)
            #Start calculations after first row of data since there is no prior data to compare
            revenue += int(row[1])
            #perform calculations to identify differences month by month and add to the diff list
            diffList.append((int(row[1]) - previous_revenue))
            #if the index reference is not the first row of data then it is then set the previous row of data to calculate differences
            if index != 1:
                previous_revenue = int(row[1])
            
    #Set real differences list by compiling all differences from calculations above
    realDiffList = [0]+diffList[1:]
    #sum all differences
    sumDiffList = sum(realDiffList)
    #calculate average differences in revenue
    averageRevenue = round(sumDiffList/num_months,2)
    #identify highest difference in revenue
    maxDiff = max(realDiffList)
    #identify lowest difference in revenue
    minDiff = min(realDiffList)
    #pick up dates by referencing the columns associated with the least/greatest revenue
    index = realDiffList.index(maxDiff)
    index2 = realDiffList.index(minDiff)
    dateOfMaxDiff = rows[index][0]
    dateOfMinDiff = rows[index2][0]

    #print data
    print("Financial Analysis")
    print("------------------------------------------------------")   
    print("Total number of months: " +str(num_months))
    print("Total revenue: " +"$" +str(revenue))
    print("Average Revenue Change: " +"$" + str(averageRevenue))
    print("Greatest Increase in Revenue: "+ str(dateOfMaxDiff) + " " +"("+"$"+ str(maxDiff)+")")
    print("Greatest Decrease in Revenue: "+ str(dateOfMinDiff) + " " +"("+"$"+ str(minDiff)+")")

    financial_analysis = filepath.split('.')[0]+"_financial_analysis.txt"

    # Write results to txt file
    f = open(financial_analysis, 'w')
    f.write("Financial Analysis\n")  
    f.write("--------------------------------\n")    
    f.write("Total number of months: "+ str(num_months)+ "\n")     
    f.write("Total revenue: " + "$" +str(revenue)+ "\n")
    f.write("Average Revenue Change: " +"$" + str(averageRevenue)+ "\n")  
    f.write("Greatest Increase in Revenue: "+ str(dateOfMaxDiff) + " " +"("+"$"+ str(maxDiff)+")"+"\n")
    f.write("Greatest Decrease in Revenue: "+ str(dateOfMinDiff) + " " +"("+"$"+ str(minDiff)+")"+ "\n")

filepath = os.path.join("budget_data_1.csv")
filepath2 = os.path.join("budget_data_2.csv")

pyBank(filepath)
pyBank(filepath2)