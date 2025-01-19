import json
import folium
from folium.plugins import HeatMap, MiniMap, Fullscreen, MeasureControl
from geopy.geocoders import Nominatim
import branca.colormap as cm

# Path to the JSON file
attacked_json_path = "attacked.json"

# Load JSON data
with open(attacked_json_path, "r", encoding="utf-8") as f:
    attacked_data = json.load(f)

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

# Function to create the map with different themes
def create_attacked_map(theme="OpenStreetMap"):
    attacked_map = folium.Map(location=[20, 0], zoom_start=2, control_scale=True, tiles=theme)

    # Add additional tile layers for switching themes
    folium.TileLayer("OpenStreetMap", attr="© OpenStreetMap contributors").add_to(attacked_map)
    folium.TileLayer("cartodbpositron", attr="© OpenStreetMap contributors, © CartoDB").add_to(attacked_map)
    folium.TileLayer("cartodbdark_matter", attr="© OpenStreetMap contributors, © CartoDB").add_to(attacked_map)

    # Add map controls
    MiniMap(toggle_display=True, position="topleft").add_to(attacked_map)
    Fullscreen(position="topleft").add_to(attacked_map)
    MeasureControl(position="topleft", primary_length_unit="kilometers").add_to(attacked_map)

    # Create a list for HeatMap data and add circles for attacked points
    heat_data = []
    max_count = max(record["Total_Attacks"] for record in attacked_data)

    # Define a colormap with better differentiation for lower counts
    colormap = cm.LinearColormap(
        colors=["#fee5d9", "#fcae91", "#fb6a4a", "#de2d26", "#a50f15"],
        vmin=1,
        vmax=max_count,
        caption="Attack Count"
    )
    colormap.add_to(attacked_map)

    for record in attacked_data:
        country = record["Destination Country"]
        total_attacks = record["Total_Attacks"]
        coords = get_coordinates(country)

        if coords:
            # Add to heatmap data
            heat_data.append([coords[0], coords[1], total_attacks])

            # Tooltip content
            tooltip_html = (
                f"<b>Destination Country: {country}</b><br>"
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
            ).add_to(attacked_map)

    # Add HeatMap to the map with a wider blur and adjusted radius
    HeatMap(heat_data, min_opacity=0.3, radius=25, blur=20, max_zoom=1).add_to(attacked_map)

    # Add LayerControl for theme switching
    folium.LayerControl(position="topright").add_to(attacked_map)

    # Save the map to an HTML file
    map_path = "attacked_heatmap.html"
    attacked_map.save(map_path)
    print(f"Attacked map saved to {map_path}")

# Create the attacked map with the default theme
create_attacked_map()
