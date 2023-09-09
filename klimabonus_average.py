import json
import matplotlib.pyplot as plt

# Load JSON data containing information about citizens, parties, and climate_category
with open('nrwahl_plz.json', 'r') as file:
    data = json.load(file)

# List of parties to analyze
parties = ['ÖVP', 'FPÖ', 'SPÖ', 'NEOS', 'GRÜNE']

# Create dictionaries to store the total amount of money and the total number of citizens for each party
total_money_by_party = {party: 0 for party in parties}
total_citizens_by_party = {party: 0 for party in parties}

# Create lists to store the amount of money received by citizens for each party
money_received_by_party = {party: [] for party in parties}

# Define custom colors for each party
party_colors = {
    'ÖVP': 'black',
    'FPÖ': 'blue',
    'SPÖ': 'red',
    'NEOS': 'pink',
    'GRÜNE': 'green',
}
money_per_citizen = {1: 110, 2: 150, 3: 185, 4: 220}

# Calculate the total amount of money, the total number of citizens, and collect money data for each party
for area in data:
    for party in parties:
        party_votes = int(area[party])
        category = int(area['klima_category'])
        # Assuming you have the amount of money per citizen for each climate_category
        total_money_by_party[party] += party_votes * money_per_citizen[category]
        total_citizens_by_party[party] += party_votes
        money_received_by_party[party].extend([money_per_citizen[category]] * party_votes)

# Calculate the average amount of money per citizen for each party
average_money_by_party = {party: total_money / total_citizens for party, total_money, total_citizens in zip(parties, total_money_by_party.values(), total_citizens_by_party.values())}

# Extract average values for plotting
parties = list(average_money_by_party.keys())
average_money = list(average_money_by_party.values())

# Create a bar chart with custom colors and exact values
plt.figure(figsize=(10, 6))
bars = plt.bar(parties, average_money, color=[party_colors[party] for party in parties])
plt.xlabel('Party')
plt.ylabel('Average Amount of Money per Citizen')
plt.title('Average Amount of Money per Citizen by Party')

# Add exact values to the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', color='black', fontweight='bold')

plt.savefig('klimabonus_average.png')

plt.show()


