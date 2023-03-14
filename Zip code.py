import folium
import json
from geopy.geocoders import Nominatim
from branca.colormap import linear

# charger les données GeoJSON
with open(r"C:\Users\33782\Desktop\M2 MSI\S2\Certification\carte_OSM\NYC.geojson") as f:
    data = json.load(f)

# créer une carte centrée sur les données
center = [40.70879507039175,-74.00098833771662]
map = folium.Map(location=center, zoom_start=13)

# Définir le rayon maximal et le score maximal
max_radius =  500
max_score = 10

# Créer un objet géocodeur Nominatim
geolocator = Nominatim(user_agent="my-app")

# parcourir les features pour ajouter chaque feature à la carte selon sa géométrie
for feature in data["features"]:
    name = feature["properties"]["name"]
    if feature["geometry"]["type"] == "MultiPolygon":
        # si la géométrie est un multipolygone, créer un objet GeoJson avec les propriétés de la feature
        folium.GeoJson(feature, 
                       name=name, 
                       style_function=lambda x: {'color': 'red', 'weight': 5}).add_to(map) # Ajout de style à la géométrie

# Liste des 10 codes ZIP et scores correspondants
zip_codes = ["10025","10009","10023","11201","10011","11215","10024","10128","10029","10003"]
scores = [367.58, 305.32, 303.13, 301.14, 300.5, 274.1, 272.35, 264.95, 218.16, 214.2]

# Ajouter un marqueur et un cercle pour chaque code ZIP avec un score personnalisé
for i, code in enumerate(zip_codes):
    # Obtenir les coordonnées géographiques du code ZIP à l'aide du géocodeur
    location = geolocator.geocode(code + ", USA")
    if location is not None:
        # Ajouter un marqueur pour les coordonnées géographiques obtenues avec l'étiquette personnalisée
        folium.Marker(location=[location.latitude, location.longitude], 
                      tooltip=f"{code}, Score: {scores[i]}").add_to(map)

        # Ajouter un cercle avec une couleur et une taille en fonction du score
        radius = 2 * max_radius * scores[i] / max_score
        folium.Circle(location=[location.latitude, location.longitude], 
                      radius=radius, 
                      color='orange', 
                      fill=True, 
                      fill_opacity=0.8).add_to(map)

# Afficher la carte
map.save(r"C:\Users\33782\Desktop\M2 MSI\S2\Certification\carte_OSM\map.html")
