import json
import folium
from folium.plugins import HeatMap, MiniMap, Fullscreen, MeasureControl
from geopy.geocoders import Nominatim
import branca.colormap as cm

# Path to the JSON file
attackers_json_path = "attackers.json"

# Load JSON data
with open(attackers_json_path, "r", encoding="utf-8") as f:
    attackers_data = json.load(f)

# Initialize geolocator
geolocator = Nominatim(user_agent="geo_mapping")

def get_coordinates(country_name: str):
    """Fetch latitude and longitude for a given country name."""
    try:
        loc = geolocator.geocode(country_name)
        if loc:
            return (loc.latitude, loc.longitude)
    except Exception:
        pass
    return None

# Create the Folium map
attacker_map = folium.Map(location=[20, 0], zoom_start=2, control_scale=True)

# Add tile layers
folium.TileLayer("OpenStreetMap", attr="© OpenStreetMap contributors").add_to(attacker_map)
folium.TileLayer("Stamen Terrain", attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.").add_to(attacker_map)
folium.TileLayer("cartodbpositron", attr="© OpenStreetMap contributors, © CartoDB").add_to(attacker_map)
folium.TileLayer("cartodbdark_matter", attr="© OpenStreetMap contributors, © CartoDB").add_to(attacker_map)

# Add map controls
MiniMap(toggle_display=True, position="topleft").add_to(attacker_map)
Fullscreen(position="topleft").add_to(attacker_map)
MeasureControl(position="topleft", primary_length_unit="kilometers").add_to(attacker_map)

# Create a list for HeatMap data and add circles for attack points
heat_data = []
max_count = max(record["Total_Attacks"] for record in attackers_data)

# Define a colormap
colormap = cm.LinearColormap(
    colors=["#d4f4dd", "#addc91", "#fdae61", "#d73027"],
    vmin=1,
    vmax=max_count,
    caption="Attack Count"
)
colormap.add_to(attacker_map)

for record in attackers_data:
    country = record["Source Country"]
    total_attacks = record["Total_Attacks"]
    coords = get_coordinates(country)
    
    if coords:
        # Add to heatmap data
        heat_data.append([coords[0], coords[1], total_attacks])

        # Tooltip content
        tooltip_html = (
            f"<b>Source Country: {country}</b><br>"
            f"Total Attacks: {total_attacks}<br>"
        )

        # Add a circle marker
        folium.Circle(
            location=coords,
            radius=total_attacks * 500,  # Increased scale for radius
            color=colormap(total_attacks),
            fill=True,
            fill_color=colormap(total_attacks),
            fill_opacity=0.7,
            tooltip=tooltip_html
        ).add_to(attacker_map)

# Add HeatMap to the map with a wider blur and adjusted radius
HeatMap(heat_data, min_opacity=0.3, radius=25, blur=20, max_zoom=1).add_to(attacker_map)

# Save the map to an HTML file
map_path = "attacker_heatmap.html"
attacker_map.save(map_path)
print(f"Attacker map saved to {map_path}")
