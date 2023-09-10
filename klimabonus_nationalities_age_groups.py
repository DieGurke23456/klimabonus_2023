import json
import matplotlib.pyplot as plt
import numpy as np

# Read the JSON data from the file
with open('merged_nationality_with_age.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Initialize counters for each climate type and category
num_climates = 4  # There are 4 climate types
climate_labels = ['Kategorie 1', 'Kategorie 2', 'Kategorie 3', 'Kategorie 4']

austria_adult_counts = np.zeros(num_climates)
eu_efta_adult_counts = np.zeros(num_climates)
others_adult_counts = np.zeros(num_climates)

austria_underage_counts = np.zeros(num_climates)
eu_efta_underage_counts = np.zeros(num_climates)
others_underage_counts = np.zeros(num_climates)

# Iterate through the data and count the climate types for each category
for entry in data:
    climate_type = entry['climate_type'] - 1  # Climate types are 1-based
    
    austria_adult_counts[climate_type] += entry['austria_adult']
    eu_efta_adult_counts[climate_type] += entry['eu_efta_adult']
    others_adult_counts[climate_type] += entry['others_adult']
    
    austria_underage_counts[climate_type] += entry['austria_underage']
    eu_efta_underage_counts[climate_type] += entry['eu_efta_underage']
    others_underage_counts[climate_type] += entry['others_underage']

# Create pie charts for climate type distribution for each age and nationality combination
age_nationality_combinations = ['Österreich (Erwachsene)', 'EU/EFTA (Erwachsene)', 'Andere (Erwachsene)',
                                'Österreich (Unter 18)', 'EU/EFTA (Unter 18)', 'Andere (Unter 18)']

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Klimabonus Kategorie nach Altersgruppe und Staatsangehörigkeit')

# Plot pie charts for each combination
for i, ax in enumerate(axes.flat):
    counts = None
    title = age_nationality_combinations[i]

    if i == 0:
        counts = austria_adult_counts
    elif i == 1:
        counts = eu_efta_adult_counts
    elif i == 2:
        counts = others_adult_counts
    elif i == 3:
        counts = austria_underage_counts
    elif i == 4:
        counts = eu_efta_underage_counts
    elif i == 5:
        counts = others_underage_counts

    ax.pie(counts, labels=climate_labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(title)

plt.tight_layout()

plt.savefig('klimabonus_nationalities_age_groups.png')

plt.show()
