import pandas as pd

# Path to the original CSV file
original_csv_path = "cybersecurity_attacks.csv"

# Path to save the prepared CSV file
prepared_csv_path = "prepared_attack_data.csv"

# Read the original CSV file
data = pd.read_csv(original_csv_path)

# Select relevant columns
prepared_data = data[['Source IP Address', 'Destination IP Address', 'Attack Type', 'Malware Indicators']]

# Save the prepared data to a new CSV file
prepared_data.to_csv(prepared_csv_path, index=False)

print(f"Prepared data saved to {prepared_csv_path}")
