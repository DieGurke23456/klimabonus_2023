import json
import matplotlib.pyplot as plt
import numpy as np
# Load JSON data
with open('nrwahl_plz.json', 'r') as file:
    data = json.load(file)

# List of parties to analyze
parties = ['ÖVP', 'FPÖ', 'SPÖ', 'NEOS', 'GRÜNE']

# Define custom colors for each party
party_colors = {
    'ÖVP': 'black',
    'FPÖ': 'blue',
    'SPÖ': 'red',
    'NEOS': 'pink',
    'GRÜNE': 'green',
}

# Create a dictionary to store counts of votes for each party in each klima_category
votes_by_party_and_category = {party: {category: 0 for category in range(1, 5)} for party in parties}

# Count votes for each party in each klima_category
for area in data:
    for party in parties:
        party_votes = int(area[party])
        category = int(area['klima_category'])
        votes_by_party_and_category[party][category] += party_votes

# Extract categories and vote counts for each party
categories = list(range(1, 5))
party_vote_counts = {party: [votes_by_party_and_category[party][category] for category in categories] for party in parties}

# Create a bar chart for each party with custom colors
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.15  # Width of each bar

for i, party in enumerate(parties):
    x = np.arange(len(categories)) + i * width
    plt.bar(x, party_vote_counts[party], width=width, label=party, color=party_colors[party])

# Customize the plot
ax.set_xlabel('Klimabonus Kategorie')
ax.set_ylabel('Anzahl Stimmen')
ax.set_title('Verteilung der Klimabonus Kategorien nach Wahlverhalten (NR 2019)')
ax.set_xticks(np.arange(len(categories)) + width * (len(parties) / 2))
ax.set_xticklabels(categories)
ax.legend()

plt.show()

