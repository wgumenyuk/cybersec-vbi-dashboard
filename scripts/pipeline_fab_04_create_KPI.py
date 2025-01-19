import json

# File paths
attackers_json_path = "attackers.json"
attacked_json_path = "attacked.json"
kpi_output_path = "kpi_data.json"

# Load JSON data
with open(attackers_json_path, "r", encoding="utf-8") as f:
    attackers_data = json.load(f)

with open(attacked_json_path, "r", encoding="utf-8") as f:
    attacked_data = json.load(f)

# Function to calculate the 4 core KPIs
def calculate_kpis(attackers, attacked):
    total_attacks = sum(record["Total_Attacks"] for record in attackers)
    total_countries_involved = len(set(record["Source Country"] for record in attackers).union(
        record["Destination Country"] for record in attacked
    ))
    top_attacking_country = max(attackers, key=lambda x: x["Total_Attacks"])
    top_attacked_country = max(attacked, key=lambda x: x["Total_Attacks"])

    return {
        "Total Attacks": total_attacks,
        "Total Countries Involved": total_countries_involved,
        "Top Attacking Country": {
            "Country": top_attacking_country["Source Country"],
            "Attacks": top_attacking_country["Total_Attacks"]
        },
        "Top Attacked Country": {
            "Country": top_attacked_country["Destination Country"],
            "Attacks": top_attacked_country["Total_Attacks"]
        }
    }

# Calculate KPIs
kpi_data = calculate_kpis(attackers_data, attacked_data)

# Save KPIs to a JSON file
with open(kpi_output_path, "w", encoding="utf-8") as f:
    json.dump(kpi_data, f, indent=4)

print(f"KPI data saved to {kpi_output_path}")
