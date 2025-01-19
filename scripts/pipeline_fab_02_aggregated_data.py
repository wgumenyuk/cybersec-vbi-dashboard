import pandas as pd
import geoip2.database
from tqdm import tqdm
import json

# Paths to files
csv_path = 'cybersecurity_attacks.csv'
mmdb_path = 'GeoLite2-Country.mmdb'

# Load the cybersecurity dataset
traffic_df = pd.read_csv(csv_path)

# Use the first 1000 entries for testing
traffic_df = traffic_df.head(1000)

# Initialize the GeoLite2 database reader
reader = geoip2.database.Reader(mmdb_path)

# Function to get country from IP
def get_country(ip):
    try:
        response = reader.country(ip)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return None  # If the IP address isn't found in the database

# Add country information to the dataframe
tqdm.pandas()
traffic_df['Source Country'] = traffic_df['Source IP Address'].progress_apply(get_country)
traffic_df['Destination Country'] = traffic_df['Destination IP Address'].progress_apply(get_country)

# Function to create JSON for attackers
def create_attackers_json(df):
    grouped = df.groupby('Source Country')
    attacker_list = []
    for country, group in grouped:
        if pd.notna(country):
            total_attacks = len(group)
            malware_attacks = len(group[group['Attack Type'] == 'Malware'])
            ddos_attacks = len(group[group['Attack Type'] == 'DDoS'])
            intrusion_attacks = len(group[group['Attack Type'] == 'Intrusion'])
            
            attacker_list.append({
                "Source Country": country,
                "Total_Attacks": total_attacks,
                "Malware_Attacks": malware_attacks,
                "DDoS_Attacks": ddos_attacks,
                "Intrusion_Attacks": intrusion_attacks
            })
    return attacker_list

# Function to create JSON for attacked
def create_attacked_json(df):
    grouped = df.groupby('Destination Country')
    attacked_list = []
    for country, group in grouped:
        if pd.notna(country):
            total_attacks = len(group)
            malware_attacks = len(group[group['Attack Type'] == 'Malware'])
            ddos_attacks = len(group[group['Attack Type'] == 'DDoS'])
            intrusion_attacks = len(group[group['Attack Type'] == 'Intrusion'])
            
            attacked_list.append({
                "Destination Country": country,
                "Total_Attacks": total_attacks,
                "Malware_Attacks": malware_attacks,
                "DDoS_Attacks": ddos_attacks,
                "Intrusion_Attacks": intrusion_attacks
            })
    return attacked_list

# Create the JSON outputs
attackers_json = create_attackers_json(traffic_df)
attacked_json = create_attacked_json(traffic_df)

# Save the JSON files
with open('attackers.json', 'w') as f:
    json.dump(attackers_json, f, indent=4)

with open('attacked.json', 'w') as f:
    json.dump(attacked_json, f, indent=4)

# Clean up the GeoLite2 reader
reader.close()

print("Attackers JSON saved to 'attackers.json'")
print("Attacked JSON saved to 'attacked.json'")
