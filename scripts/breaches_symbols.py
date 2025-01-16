import csv, json, re

csv_file_path = "data/original/breaches_symbols.csv"
json_file_path = "data/transformed/breaches_symbols.json"

with open(csv_file_path) as csv_file:
	csv_reader = csv.DictReader(csv_file)
	rows = []

	for i, row in enumerate(csv_reader):
		item = {
			"ID": i + 1,
			"Company": row["Company"],
			"Symbol": row["Symbol"],
			"Industry": row["Industry"],
			"Date": row["Date"],
			"Type": re.split(",\\s*", row["Type"]),
			"Pre": row["Pre"],
			"During": row["During"],
			"Post": row["Post"]
		}

		try:
			item["Affected"] = int(row["Affected"].replace(".", ""))
		except ValueError:
			item["Affected"] = "Unknown"

		for key in ("Pre", "During", "Post"):
			try:
				item[key] = float(row[key].replace(",", "."))
			except ValueError:
				item[key] = None
			
		rows.append(item)

	with open(json_file_path, "w") as json_file:
		json_file.write(json.dumps(rows))
