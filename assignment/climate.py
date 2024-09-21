import requests
from lxml import html

import dotenv
import os
import json
import matplotlib.pyplot as plt
from scraping_utils import get_url, parse
dotenv.load_dotenv()

# load the environment variables

# get page
page = get_url(os.getenv('URL'), 'climate')

# parse the page to html
tree = parse(page, 'html')

data = {}

# initialize row counter
row_num = 0

for row in tree.xpath(os.getenv('ROW_XPATH')):
    columns = row.xpath(os.getenv('COL_XPATH'))
    columns = [column.text_content() for column in columns]
    columns = [column.strip() for column in columns]
    #print(columns)

    if len(columns) < 10:
        continue  # Skip rows that don't have enough columns

    country = columns[0]
    values = [float(value.replace(',', '')) if value != '—' else None for value in columns[1:-1]]
    percentage_change = columns[-1]
    
    years = [1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2021]
    year_value_pairs = [{"year": year, "value": value} for year, value in zip(years, values)]
    
    
    data[country] = {
        "year_value_pairs": year_value_pairs,
        "percentage_change": percentage_change
    }

# Print the data dict
print(json.dumps(data, indent = 4))

# Ensure the 'dist' directory exists
output_dir = 'dist'
os.makedirs(output_dir, exist_ok=True)

# Save the data dictionary to a JSON file
output_file = os.path.join(output_dir, 'data.json')
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Data saved to {output_file}")     

