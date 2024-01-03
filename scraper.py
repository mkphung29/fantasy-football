import requests
from bs4 import BeautifulSoup
import csv

def scrape_quarterback_stats():
    url = 'https://www.fantasypros.com/nfl/stats/qb.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the header row
    header_row = soup.find('thead').find_all('tr')[-1]

    new_columns = ['RANK', 'PLAYER', 'CMP', 'PASS_ATT', 'PCT', 'PASS_YDS', 'Y/A', 'PASS_TD', 'INT', 
                   'SACKS', 'RUSH_ATT', 'RUSH_YDS', 'RUSH_TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'ROST']

    # Find the tbody section
    tbody = soup.find('tbody')

    # Create a CSV file and write the header
    with open('data/quarterback_stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new_columns)  # Combine passing and rushing columns

        # Iterate through each player row
        for player_row in tbody.find_all('tr', class_=lambda x: x and 'mpb-player' in x):
            # Iterate through each column and write the data to CSV
            player_data = [col.get_text(strip=True) for col in player_row.find_all('td')]
            csv_writer.writerow(player_data)


def scrape_runningback_stats():
    url = 'https://www.fantasypros.com/nfl/stats/rb.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the header row
    header_row = soup.find('thead').find_all('tr')[-1]

    columns = ['RANK', 'PLAYER', 'ATT', 'RUSH_YDS', 'Y/A', 'LG', '20+', 
                   'RUSH_TD', 'REC', 'TGT', 'REC_YDS', 'Y/R', 'REC_TD', 'FL', 
                   'G', 'FPTS', 'FPTS/G', 'ROST']

    # Find the tbody section
    tbody = soup.find('tbody')

     # Create a CSV file and write the header
    with open('data/runningback_stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(columns)

        # Iterate through each player row
        for player_row in tbody.find_all('tr', class_=lambda x: x and 'mpb-player' in x):
            # Iterate through each column and write the data to CSV
            player_data = [col.get_text(strip=True) for col in player_row.find_all('td')]
            csv_writer.writerow(player_data)


def scrape_wide_receiver_stats():
    url = 'https://www.fantasypros.com/nfl/stats/wr.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the header row
    header_row = soup.find('thead').find_all('tr')[-1]

    # Set column names
    columns = ['RANK', 'PLAYER', 'REC', 'TGT', 'REC_YDS', 'Y/R',
               'LG', '20+', 'REC_TD', 'ATT', 'RUSH_YDS', 'RUSH_TD',
               'FL', 'G', 'FPTS', 'FPTS/G', 'ROST']

    # Find the tbody section
    tbody = soup.find('tbody')

    # Create a CSV file and write the header
    with open('data/wide_receiver_stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(columns)

        # Iterate through each player row
        for player_row in tbody.find_all('tr', class_=lambda x: x and 'mpb-player' in x):
            # Iterate through each column and write the data to CSV
            player_data = [col.get_text(strip=True) for col in player_row.find_all('td')]

            # Remove commas if the value is a string
            for i, value in enumerate(player_data):
                if isinstance(value, str):
                    if ',' in value:
                        value = int(value.replace(',', ''))
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            pass  # Handle non-integer values if needed

                    player_data[i] = value

            csv_writer.writerow(player_data)


def scrape_tight_end_stats():
    url = 'https://www.fantasypros.com/nfl/stats/te.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the header row
    header_row = soup.find('thead').find_all('tr')[-1]

    # Extract column names from th tags only
    columns = ['RANK', 'PLAYER', 'REC', 'TGT', 'REC_YDS', 'Y/R', 'LG','20+', 'REC_TD', 'ATT', 'RUSH_YDS', 'RUSH_TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'ROST']

    # Find the tbody section
    tbody = soup.find('tbody')

    # Create a CSV file and write the header
    with open('data/tight_end_stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(columns)

        # Iterate through each player row
        for player_row in tbody.find_all('tr', class_=lambda x: x and 'mpb-player' in x):
            # Iterate through each column and write the data to CSV
            player_data = [col.get_text(strip=True) for col in player_row.find_all('td')]

            # Remove commas if the value is a string
            for i, value in enumerate(player_data):
                if isinstance(value, str):
                    if ',' in value:
                        value = int(value.replace(',', ''))
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            pass  # Handle non-integer values if needed

                    player_data[i] = value

            csv_writer.writerow(player_data)


def scrape_defense_stats():
    url = 'https://www.fantasypros.com/nfl/stats/dst.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the header row
    header_row = soup.find('thead').find_all('tr')[-1]

    # Extract column names from th tags only
    columns = [col.get_text(strip=True) for col in header_row.find_all('th')]

    # Find the tbody section
    tbody = soup.find('tbody')

    # Create a CSV file and write the header
    with open('data/defense_stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(columns)

        # Iterate through each player row
        for player_row in tbody.find_all('tr', class_=lambda x: x and 'mpb-player' in x):
            # Iterate through each column and write the data to CSV
            player_data = [col.get_text(strip=True) for col in player_row.find_all('td')]
            csv_writer.writerow(player_data)


def scrape_kicker_stats():
    url = 'https://www.fantasypros.com/nfl/stats/k.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the header row
    header_row = soup.find('thead').find_all('tr')[-1]

    # Extract column names from th tags only
    columns = [col.get_text(strip=True) for col in header_row.find_all('th')]

    # Find the tbody section
    tbody = soup.find('tbody')

    # Create a CSV file and write the header
    with open('data/kicker_stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(columns)

        # Iterate through each player row
        for player_row in tbody.find_all('tr', class_=lambda x: x and 'mpb-player' in x):
            # Iterate through each column and write the data to CSV
            player_data = [col.get_text(strip=True) for col in player_row.find_all('td')]
            csv_writer.writerow(player_data)
