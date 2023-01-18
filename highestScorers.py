import requests
from bs4 import BeautifulSoup
import pandas as pd     #dataframe

def get_highest_scorer(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml') 
    player = { 
        'Player name': sp.select_one('td.who').text.strip().replace('\n', ' '), 
        'Team': sp.select_one('span.desc').text.strip().replace('\n', ' '),
        'Total points': sp.select_one('td.value').text.strip().replace('\n', ' '),
    }
    print (sp.title.string)
    return player


base_url = 'https://www.basketball-reference.com/leagues/NBA_' 
base_url2 = '_leaders.html'
nba_season = input("Enter the NBA season to view in a XXXX format. Example: 2022-23 would be 2023.")
final_url = base_url + nba_season + base_url2    

results = get_highest_scorer(final_url)
print(results)
