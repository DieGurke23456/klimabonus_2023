import json
import matplotlib.pyplot as plt

# Read the JSON data from the file
with open('merged_nationality_with_age.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Initialize dictionaries to store the total amounts and counts for each category
nations = ['austria', 'eu_efta', 'others']

# Create dictionaries to store the total amount of money and the total number of citizens for each nation
total_money_by_nation = {nation: 0 for nation in nations}
total_citizens_by_nation = {nation: 0 for nation in nations}

# Calculate the total amounts and counts for each category and climate type
money_per_citizen = {1: 110, 2: 150, 3: 185, 4: 220}
nation_colors = {
    'austria': 'red',
    'eu_efta': 'blue',
    'others': 'grey'
}
# Calculate the total amount of money, the total number of citizens, and collect money data for each nation
for area in data:
    for nation in nations:
        nation_adults = int(area[nation + '_adult'])
        nation_underage = int(area[nation + '_underage'])
        category = int(area['climate_type'])
        # Assuming you have the amount of money per citizen for each climate_category
        total_money_by_nation[nation] += nation_adults * money_per_citizen[category]
        total_money_by_nation[nation] += nation_underage * (money_per_citizen[category] / 2)
        total_citizens_by_nation[nation] += nation_adults + nation_underage
        
# Calculate the average amount of money per citizen for each nation
average_money_by_nation = {nation: total_money / total_citizens for nation, total_money, total_citizens in zip(nations, total_money_by_nation.values(), total_citizens_by_nation.values())}

# Extract average values for plotting
nations = list(average_money_by_nation.keys())
average_money = list(average_money_by_nation.values())

# Create a bar chart with custom colors and exact values
plt.figure(figsize=(10, 6))
bars = plt.bar(nations, average_money, color=[nation_colors[nation] for nation in nations])
plt.xlabel('Staatsangehörigkeit')
plt.ylabel('Durchschnittlicher Klimabonus')
plt.title('Durchschnittlicher Klimabonus pro Person nach Staatsangehörigkeit')

# Add exact values to the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', color='black', fontweight='bold')

plt.savefig('klimabonus_average_nationality.png')

plt.show()
