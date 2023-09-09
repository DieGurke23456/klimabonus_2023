import json
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Load JSON data containing information about citizens, parties, and climate_category
with open('nrwahl_plz.json', 'r') as file:
    data = json.load(file)

# List of parties to analyze
parties = ['ÖVP', 'FPÖ', 'SPÖ', 'NEOS', 'GRÜNE', 'ANDERE']

# Define custom colors for each party
party_colors = {
    'ÖVP': 'black',
    'FPÖ': 'blue',
    'SPÖ': 'red',
    'NEOS': 'pink',
    'GRÜNE': 'green',
    'ANDERE': 'grey'
}

# Initialize dictionaries to store vote counts for each party across climate categories
votes_by_party_and_category = {party: {1: 0, 2: 0, 3: 0, 4: 0} for party in parties}

# Calculate the vote counts for each party across climate categories
for area in data:
    for party in parties:
        if party == 'ANDERE':
            party_votes = int(area['total']) - sum([int(area[x]) for x in ['ÖVP', 'FPÖ', 'SPÖ', 'NEOS', 'GRÜNE']])
        else:
            party_votes = int(area[party])
        
        category = int(area['klima_category'])
        votes_by_party_and_category[party][category] += party_votes

# Create a figure with four subplots for each climate category
fig, axes = plt.subplots(1, 4, figsize=(15, 5))

# Loop through each climate category and create a pie chart for each
for category in range(1, 5):
    ax = axes[category - 1]
    party_votes = [votes_by_party_and_category[party][category] for party in parties]
    colors = [party_colors[party] for party in parties]
    textprops = {'color': 'white' if category == 'ÖVP' else 'white'}
    ax.pie(party_votes, labels=parties, colors=colors, autopct='%1.1f%%', startangle=90, textprops=textprops)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    ax.set_title(f'Kategorie {category}')

# Add a legend to explain the colors
legend_elements = [Patch(facecolor=color, label=party) for party, color in party_colors.items()]
plt.legend(handles=legend_elements, loc='upper right')

# Add a title for the entire figure
plt.suptitle('Wahlverhalten nach Klimabonus Kategorie (NR2019) ')

# Display the pie charts
plt.show()
