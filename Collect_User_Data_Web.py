import warnings
warnings.filterwarnings('ignore')

from pymongo import MongoClient
import pprint
import numpy as np
import copy
import pandas as pd

# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup

import re

from time import sleep

#Create csv table to append into

#User_data = pd.DataFrame(columns = ["User Name", "Avg. Assists", "Avg. Kills", "Avg. Deaths", "Win Rate", "Champs"])
#User_data.to_csv('/Users/samanthajamwal/Desktop/LOL/Master/User_data_1.csv')



#import the user name list
df = pd.read_csv('/Users/samanthajamwal/Desktop/LOL/Master/CLean_Users.csv')
df = df[65279:]

df_name = df


#final script
def run (df_name):
  for name in df_name['User']:


    web = (f'https://na.op.gg/summoner/userName={name}')
    r = requests.get(web)
    client = MongoClient('localhost', 27017)
    db = client.metroid
    pages = db.pages
    pages.insert_one({'html': r.content})
    soup = (BeautifulSoup(r.content, "html.parser"))

    try:
      ass= assists(soup)
      kill_= kill_rate(soup)
      death_ = death_rate(soup)
      win_ = win_rate(soup)
      champs_ = champs(soup)

      row = pd.DataFrame([name, ass, kill_, death_, win_, champs_]).T
      row.to_csv('/Users/samanthajamwal/Desktop/LOL/Master/User_data_1.csv', mode='a', header=False)
      print ('worked')
    except:
      print ('?')
  sleep(.02)





def assists(site):
    assists =(site.find('span', class_ = "Assist"))
    avg_assists = assists.text.strip()
    return avg_assists

def kill_rate(site):
    kill =(site.find('span', class_ = "Kill"))
    kill_rate = kill.text.strip()
    return kill_rate
def death_rate(site):
    death = (site.find('span', class_ = "Death"))
    death_rate = death.text.strip()
    return death_rate


def win_rate(site):
    win_ = (site.find('span', class_ = "win"))
    lose_ = (site.find('span', class_ = "lose"))

    win = int(win_.text.strip())
    lose = int(lose_.text.strip())


    return (win/ (win + lose))

def champs(site):
    champs = {}
    value = 8
    divs = site.findAll(class_= 'ChampionBox Ranked')
    for div in divs:
        name = div.find(class_ = 'ChampionName')
        key = (name.text.strip())

        value -= 1




        champs[key] = value
    return champs


run(df_name)
#print (df_name)