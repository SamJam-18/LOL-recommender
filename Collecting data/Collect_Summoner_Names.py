from pantheon import pantheon
import asyncio
import pandas as pd
import os
from csv import reader
import time



user_lst = pd.read_csv('/Users/samanthajamwal/Desktop/LOL/league_na1.csv')


server = "na1"
api_key = "RGAPI-64599979-4228-40ac-8fc4-51d588fa6900"

lst = []

def requestsLog(url, status, headers):
    print(url)
    print(status)
    print(headers)

panth = pantheon.Pantheon(server, api_key, errorHandling=True, requestsLoggingFunction=requestsLog, debug=True)

lst = []
async def getSummonerId(id):
    data = await panth.getLeagueById(id)
    entries = data['entries']
    for x in (entries):
        lst.append(x['summonerName'])

user_lst = user_lst['leagueId']

cur_lst = user_lst[12000:]

for x in cur_lst:
    try:


        loop = asyncio.get_event_loop()

        loop.run_until_complete(getSummonerId(x))


    except Exception as e:
        continue

def write_to_csv(list_user):
    with open('/Users/samanthajamwal/Desktop/LOL/users_2000.csv', 'a') as csvfile:
        for name in lst:
            csvfile.write(name + '\n')

write_to_csv(lst)
