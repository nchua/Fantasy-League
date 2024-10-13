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

# Example: Find the divs for both teams
teams_data = soup.find_all('div', class_='col-12 col-sm-6')

# Initialize a list to hold stats for both teams
team_stats = []

# Loop over the team divs and extract stats for each team
for team_div in teams_data:
    # Extract the team name from the appropriate header (blue-line-header or red-line-header)
    team_name_raw = team_div.find('div', class_=['blue-line-header', 'red-line-header']).get_text(strip=True)
    
    # Remove the '- WIN' or '- LOSS' part by splitting at ' - ' and keeping the first part
    team_name = team_name_raw.split(' - ')[0]

    # Find the rows for the stats within each team div
    stat_rows = team_div.find_all('span', class_=['score-box blue_line', 'score-box red_line'])

    # Loop through the rows and capture the stats for the current team
    for row in stat_rows:
        stat_type = row.find('img')['alt']  # e.g., Kills, Towers
        stat_value = row.get_text(strip=True)  # Extract the stat value (e.g., '25')

        # Append the data based on stat type and team
        team_stats.append({
            'team': team_name,  # Use the extracted and cleaned team name
            'stat_type': stat_type,
            'value': stat_value
        })

# Print the scraped data for both teams
for stat in team_stats:
    print(stat)