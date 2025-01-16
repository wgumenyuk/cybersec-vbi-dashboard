import csv
import json

csv_file_path = "data/original/cybersecurity_attacks.csv"
json_file_path = "data/transformed/cybersecurity_attacks.json"

with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = []

    for row in csv_reader:
        for key, value in row.items():
            if value:
                row[key] = value.strip()
        rows.append(row)

with open(json_file_path, mode="w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(rows))
