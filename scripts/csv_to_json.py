import sys, csv, json

def csv_to_json(csv_file_path: str, json_file_path: str, exclude: list[str] = []) -> None:
	rows = []

	with open(csv_file_path) as csv_file:
		csv_reader = csv.DictReader(csv_file)

		for row in csv_reader:
			rows.append({ key: value for key, value in row.items() if key not in exclude })

	with open(json_file_path, "w") as json_file:
		json_file.write(json.dumps(rows))

if __name__ == "__main__":
	args = sys.argv[1:]

	if len(args) < 2:
		exit(1)

	csv_to_json(args[0], args[1], args[2:])
