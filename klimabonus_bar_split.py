import json
import matplotlib.pyplot as plt
import numpy as np

# Load JSON data
with open('nrwahl_plz.json', 'r') as file:
    data = json.load(file)

# List of parties to analyze
parties = ['ÖVP', 'FPÖ', 'SPÖ', 'NEOS', 'GRÜNE']

categories = list(range(1, 5))

votes_by_party_and_category = {party: {category: 0 for category in range(1, 5)} for party in parties}

# Define custom colors for each party
party_colors = {
    'ÖVP': 'black',
    'FPÖ': 'blue',
    'SPÖ': 'red',
    'NEOS': 'pink',
    'GRÜNE': 'green',
}

# Count votes for each party in each climate category
for area in data:
    for party in parties:
        party_votes = int(area[party])
        category = int(area['klima_category'])
        votes_by_party_and_category[party][category] += party_votes

# Find the maximum y-axis value across all subplots
max_y = 800000

# Create separate bar charts for each party in the same window with custom colors and equal y-axis scale
fig, axes = plt.subplots(1, len(parties), figsize=(15, 5), sharey=True)

for i, party in enumerate(parties):
    vote_counts = [votes_by_party_and_category[party][category] for category in categories]
    ax = axes[i]
    ax.bar(categories, vote_counts, tick_label=categories, color=party_colors[party])
    ax.set_xlabel('Klimabonus Kategory')
    ax.set_ylabel('Abgegebne Stimmen (NR2019)')
    ax.set_title(f'Stimmen pro Kategory {party}')
    ax.set_ylim(0, max_y)  # Set the same y-axis limits for all subplots

# Adjust spacing between subplots
plt.tight_layout()
plt.savefig('klimabonus_bar_split.png')

plt.show()
