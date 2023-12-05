#!/usr/bin/env python3
# Day 99

import requests
from bs4 import BeautifulSoup

def scrape_current_table():
    url = 'https://www.footballwebpages.co.uk/premier-league'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'league-table'})

        current_table = []
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 4:
                position = columns[0].text.strip()
                team_name = columns[1].text.strip()
                games_played = columns[2].text.strip()
                points = columns[10].text.strip()  # Updated to index 8 for points

                team_data = {
                    'Position': position,
                    'Team': team_name,
                    'Games Played': games_played,
                    'Points': points
                }
                current_table.append(team_data)

        return current_table
    else:
        print("Failed to fetch data.")
        return None

def display_current_table(table_data):
    if table_data:
        print("Current Premier League Table:")
        print("{:<10} {:<30} {:<15} {:<10}".format('Position', 'Team', 'Games Played', 'Points'))
        for team in table_data:
            print("{:<10} {:<30} {:<15} {:<10}".format(team['Position'], team['Team'], team['Games Played'], team['Points']))
    else:
        print("Scraping failed.")

# Get the current Premier League table data and display it
current_table = scrape_current_table()
display_current_table(current_table)

