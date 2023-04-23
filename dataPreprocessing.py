import csv

dataset1 = []
dataset2 = []

with open("finalOutput.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset1.append(row)

with open("archiveDataSorted1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset2.append(row)

headers1 = dataset1[0]
planetData1 = dataset1[1:]

headers2 = dataset2[0]
planetData2 = dataset2[1:]

headers = headers1 + headers2
planetData = []
for index, data_row in enumerate(planetData1):
    planetData.append(planetData1[index] + planetData2[index])

with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetData)