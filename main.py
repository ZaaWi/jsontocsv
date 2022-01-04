import csv
import json

rowOneHeader = "row one"
rowTwoHeader = "row two"

with open('data.json', encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)

with open('output.csv', 'w', encoding="utf-8") as output:
    writer = csv.writer(output)
    writer.writerow([rowOneHeader, rowTwoHeader])
    for item in data:
        writer.writerow([item, data[item]])