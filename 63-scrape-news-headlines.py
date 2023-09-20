#!/usr/bin/env python3
# Day 63

import requests
from bs4 import BeautifulSoup

# if needed install requests and beautifulsoup4
# pip install requests beautifulsoup4

# Define the URL of the BBC News website
url = "https://www.bbc.com/news"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the headlines on the page (specific to the BBC News website structure)
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

    # Print the latest headlines
    print("Latest BBC News Headlines:")
    for headline in headlines:
        print(headline.get_text())

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

