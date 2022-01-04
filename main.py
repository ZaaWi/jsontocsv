import csv
import json

with open('data.json', encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)

with open('output.csv', 'w', encoding="utf-8") as output:
    print(output)
    writer = csv.writer(output)
    writer.writerow(['key', 'translation'])
    for item in data:
        print(item + data[item])
        writer.writerow([item, data[item]])