import requests
from bs4 import BeautifulSoup

def get_highest_scorer(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    player = { 
        'Player name': sp.select_one('a.Anchor_anchor__cSc3P').text.strip().replace('\n', ' '), 
        'Team': sp.select_one('a.Anchor_anchor__cSc3P').text.strip().replace('\n', ' ')
    }
    print(player)


base_url = 'https://www.nba.com/stats/leaders?SeasonType=Regular+Season&Season='
nba_season = input("Enter the NBA season to view, in a XXXX-XX format. Example: 2022-23")
final_url = base_url + nba_season

get_highest_scorer(final_url)

