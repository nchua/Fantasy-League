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

# Find the divs for both teams (these contain the team names)
teams_data = soup.find_all('div', class_='col-12 col-sm-6')

# Initialize variables for team names
team_1_name = ''
team_2_name = ''

# Loop over the team divs and extract the team names from the <a> tag
for i, team_div in enumerate(teams_data):
    # Extract the team name from the <a> tag
    team_name = team_div.find('a').get_text(strip=True)
    
    # Assign to team 1 or team 2
    if i == 0:
        team_1_name = team_name
    else:
        team_2_name = team_name

# Print the team names
print(f"Team 1: {team_1_name}")
print(f"Team 2: {team_2_name}")