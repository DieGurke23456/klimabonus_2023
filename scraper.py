import requests
from bs4 import BeautifulSoup
import json

# Define a list of URLs to scrape
base_url = "https://www.gemeinden.at/gemeinden/plz/"
urls = [f"{base_url}{x}" for x in range(1, 10)]

# Initialize a list to store the extracted data from all URLs
all_data = []

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []

        rows = soup.find_all('tr')

        for row in rows:
            try:
                name = row.find('span', style='font-weight:bold;').text.strip()
                plz = row.find('a').text.strip()

                # Encode and decode special characters
                name = name.encode('utf-8').decode('utf-8')
                plz = plz.encode('utf-8').decode('utf-8')

                entry = {
                    'Name': name,
                    'PLZ': plz
                }

                data.append(entry)
            except AttributeError as e:
                print(f"Error occurred: {e}")

        # Append the data from this URL to the list of all_data
        all_data.extend(data)
    else:
        print(f"Failed to retrieve the web page at URL: {url}. Status code:", response.status_code)

# Store all the data in a single JSON file
with open('plz.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)

print("Data extracted and saved to 'plz.json'")
