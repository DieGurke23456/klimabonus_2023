from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import json

# Load your JSON data from the file
with open('nrwahl.json', 'r') as file:
    data = json.load(file)

# Define a regular expression pattern to match the desired keys
pattern = r'G[1-9][0-9][0-9][0-8][1-9]'

# Filter the keys that match the pattern
filtered_keys = [key for key in data.keys() if re.match(pattern, key)]

# Create a new dictionary with only the matching keys and their corresponding values
filtered_data = {key: data[key] for key in filtered_keys}

# Load the PLZ data
with open('plz.json', 'r', encoding='utf-8') as plz_file:
    plz_data = json.load(plz_file)
    

# Create a dictionary to map "ort" from PLZ data to "plz"
plz_mapping = {x['Name']: x['PLZ'] for x in plz_data}
total_features = len(filtered_data)

with open('plz_klima.json', 'r', encoding='utf-8') as type_data_file:
    type_data = json.load(type_data_file)

to_store = []
for idx, key in enumerate(filtered_data.keys(), start=1):
    feature = filtered_data[key]
    ort = str(feature['gebietsname'])

    # Find the best match for "ort" in PLZ data using fuzzy matching
    best_match, score = process.extractOne(ort, plz_mapping.keys(), scorer=fuzz.ratio)
    
    # add plz of best match  
    plz = plz_mapping.get(best_match, None)
    print(f"Processed {idx}/{total_features} features")
    
    type_value = type_data.get(str(plz), 0)
    if isinstance(type_value, list):
        # If the type information is a list, take the first item's type
        list_a = list(
            x for x in type_value
            if x['name'] == ort
        )
        if len(list_a) == 0:
            type_value = type_value[0]['type']
        else:
            type_value = list_a[0]['type']

    
    to_store.append(
        {
            "ort":ort,
            "matched_ort": best_match,
            "plz": plz,
            "total":feature['abgegeben'],
            "ÖVP": feature['ÖVP'],
            "FPÖ": feature['FPÖ'],
            "SPÖ": feature['SPÖ'],
            "NEOS": feature['NEOS'],
            "GRÜNE": feature['GRÜNE'],
            "klima_category":type_value
        }
    )

# Save the merged GeoJSON data with PLZ information
with open('nrwahl_plz.json', 'w', encoding='utf-8') as output_file:
    json.dump(to_store, output_file, ensure_ascii=False, indent=4)
