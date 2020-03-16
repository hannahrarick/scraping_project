
"""get info about MLS soccer players"""

from bs4 import BeautifulSoup
import requests

def get_player_details(player):
    page_url = "https://www.mlssoccer.com" + player
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # scrape 6 separate details from one page
    title = soup.find( "div", class_="title" )
    team = soup.find( "div", class_="club" )
    position = soup.find( "span", class_="position" )
    birthday = soup.find( "div", class_="age" )
    birthplace = soup.find( "div", class_="hometown" )
    twitter = soup.find( "div", class_="twitter_handle" )

    player_details = [title, team, position, birthday, birthplace,
        twitter]

    for detail in player_details:
        try:
            print( detail.text )
        except AttributeError:
            print( "None" )


# run function for ONE player URL
get_player_details('/players/carlos-vela')

players_list = [
    '/players/carlos-vela',
    '/players/zlatan-ibrahimovic',
    '/players/josef-martinez',
    '/players/maximiliano-moralez',
    '/players/ike-opara'
]
def scrape_all_players(list):
    for player in list:
        get_player_details(player)
        print() # blank line
# run function for ALL players in a list
scrape_all_players(players_list)
