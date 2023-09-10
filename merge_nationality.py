import csv
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re

# Read the CSV file and store the data in a dictionary

def read_integer(column):
    return int(column) if column and column != '-' else 0
csv_data = {}
with open('austria.csv', 'r', encoding='ISO-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        commune = row[1].split('<')[0]  # Remove ISO code
        austria_underage = 0
        austria_of_age = 0
        eu_efta_underage = 0 
        eu_efta_of_age = 0
        others_underage = 0
        others_of_age = 0
        
        austria_underage += read_integer(row[2])
        austria_underage += read_integer(row[6])
        austria_of_age += read_integer(row[4]) - read_integer(row[6]) 
        austria_of_age += read_integer(row[8]) 
        austria_of_age += read_integer(row[10])
        austria_of_age += read_integer(row[12])
        austria_of_age += read_integer(row[14])
        
        eu_efta_underage += read_integer(row[2 + 14])
        eu_efta_underage += read_integer(row[6 + 14])
        eu_efta_of_age += read_integer(row[4 + 14]) - read_integer(row[6 + 14]) 
        eu_efta_of_age += read_integer(row[8 + 14]) 
        eu_efta_of_age += read_integer(row[10 + 14])
        eu_efta_of_age += read_integer(row[12 + 14])
        eu_efta_of_age += read_integer(row[14 + 14])
        
        others_underage += read_integer(row[2 + 28])
        others_underage += read_integer(row[6 + 28])
        others_of_age += read_integer(row[4 + 28]) - read_integer(row[6 + 28]) 
        others_of_age += read_integer(row[8 + 28]) 
        others_of_age += read_integer(row[10 + 28])
        others_of_age += read_integer(row[12 + 28])
        others_of_age += read_integer(row[14 + 28])
        
        csv_data[commune] = {
            'austria_underage': austria_underage,
            'austria_adult': austria_of_age,
            'eu_efta_underage': eu_efta_underage,
            'eu_efta_adult': eu_efta_of_age,
            'others_underage': others_underage,
            'others_adult': others_of_age,
        }

with open('plz_klima.json', 'r', encoding='utf-8') as type_data_file:
    type_data = json.load(type_data_file)
    
# Read the JSON file with PLZ data
with open('output.json', 'r', encoding='utf-8') as jsonfile:
    plz_data = json.load(jsonfile)
    
plz_mapping = {x['Name']: x['PLZ'] for x in plz_data}
total_features = len(csv_data.keys())
# Create the desired JSON output
output_data = []
for idx, key in enumerate(csv_data.keys(), start=1):
    data = csv_data[key]
    best_match, score = process.extractOne(key, plz_mapping.keys(), scorer=fuzz.ratio)
    plz = plz_mapping.get(best_match, None)
    type_value = type_data.get(str(plz), 0)
    if isinstance(type_value, list):
        # If the type information is a list, take the first item's type
        list_a = list(
            x for x in type_value
            if x['name'] == key
        )
        if len(list_a) == 0:
            type_value = type_value[0]['type']
        else:
            type_value = list_a[0]['type']
    
    print(f"Processed {idx}/{total_features} features")
    output_entry = {
        'name': key,
        'PLZ': plz,
        'matched_name':data.get('matched_name', 0),
        'austria_underage':data.get('austria_underage', 0),
        'austria_adult':data.get('austria_adult', 0),
        'eu_efta_underage':data.get('eu_efta_underage', 0),
        'eu_efta_adult':data.get('eu_efta_adult', 0),
        'others_underage':data.get('others_underage', 0),
        'others_adult':data.get('others_adult', 0),
        'climate_type': type_value
    }
    output_data.append(output_entry)
    
# Write the output to a JSON file
with open('merged_nationality_with_age.json', 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, indent=4, ensure_ascii=False)

