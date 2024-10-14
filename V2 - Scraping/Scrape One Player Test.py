import requests
from bs4 import BeautifulSoup

# URL of the match stats page (replace with the match page you want to scrape)
url = "https://gol.gg/game/stats/62705/page-game/"

# Define a User-Agent to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Make a GET request to fetch the HTML content of the page
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raise an error if the request was unsuccessful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the second <div class="row rowbreak pb-4"> section where player stats are located
player_stats_sections = soup.find_all('div', class_='row rowbreak pb-4')

# We assume the second <div> contains player information based on your description
if len(player_stats_sections) < 2:
    print("Player stats section not found.")
else:
    player_stats_section = player_stats_sections[1]

    # Find the tables containing player statistics (each team's table)
    tables = player_stats_section.find_all('table', class_='playersInfosLine footable toggle-square-filled')

    # Check if tables are found
    if not tables or len(tables) < 2:
        print("Could not find two tables for team player stats.")
    else:
        # Initialize lists to store player names for both teams
        team_1_players = []
        team_2_players = []

        # Process Team 1's table
        team_1_table = tables[0]
        team_1_rows = team_1_table.find_all('tr')
        for row in team_1_rows:
            player_name_td = row.find('td', style="white-space:nowrap")
            if player_name_td:
                player_name_a = player_name_td.find('a', class_='link-blanc')
                if player_name_a:
                    player_name = player_name_a.get_text(strip=True)
                    team_1_players.append(player_name)

        # Process Team 2's table
        team_2_table = tables[1]
        team_2_rows = team_2_table.find_all('tr')
        for row in team_2_rows:
            player_name_td = row.find('td', style="white-space:nowrap")
            if player_name_td:
                player_name_a = player_name_td.find('a', class_='link-blanc')
                if player_name_a:
                    player_name = player_name_a.get_text(strip=True)
                    team_2_players.append(player_name)

        # Print out the results
        print(f"Team 1: {', '.join(team_1_players)}")
        print(f"Team 2: {', '.join(team_2_players)}")