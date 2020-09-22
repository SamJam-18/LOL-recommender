import pandas as pd
import logging
import numpy as np
from sklearn.metrics import pairwise_distances, mean_squared_error

#import User data and clean it
df = pd.read_csv('/Users/samanthajamwal/Desktop/LOL/Master/User_data_1.csv')
df = df.set_index(df['User Name'])
df = df.drop(['Unnamed: 0'], axis = 1)

#
df['Champs'] = df['Champs'].str.replace('{', '').str.replace('}', '').str.replace('\'','').str.replace(': ', '').str.replace('7', '').str.replace('6', '').str.replace('5', '').str.replace('4', '').str.replace('3', '').str.replace('2', '').str.replace('1', '').str.replace(' ', '')
df['Champs'] = df['Champs'].str.replace('Dr.Mundo', 'DrMundo').str.replace('\"', '').str.replace('&Willump', '').str.replace('LeBlanc', 'Leblanc').str.replace('KhaZix', 'Khazix').str.replace('ChoGath', 'Chogath').str.replace('KaiSa', 'Kaisa').str.replace('Wukong', 'MonkeyKing').str.replace('VelKoz', 'Velkoz')

df['Champs'] = df['Champs'].str.split(',')

#want users that have chmpions
df = df[df['Champs'].map(lambda d: len(d)) > 1]

df_champ = pd.read_csv('/Users/samanthajamwal/Desktop/LOL/Master/Champ_data.csv')
champ_data = df_champ.drop(['Unnamed: 0', 'Key', 'Image', 'Lore', 'Ally Tips', 'Enemy Tips'], axis =1)
champ_data = champ_data.set_index(champ_data['Champion'], drop = True)
champ_data = champ_data.drop(['Champion'], axis =1)
champ_data['Tags'] = champ_data['Tags'].str.replace('[', '').str.replace(']', '').str.replace('\'', '').str.replace(' ', '')
champ_data['Tags'] = champ_data['Tags'].str.split(',')

champ_data = df_champ.drop(['Unnamed: 0', 'Key', 'Image', 'Lore', 'Ally Tips', 'Enemy Tips'], axis =1)
champ_data = champ_data.set_index(champ_data['Champion'], drop = True)
champ_data = champ_data.drop(['Champion'], axis =1)
champ_data['Tags'] = champ_data['Tags'].str.replace('[', '').str.replace(']', '').str.replace('\'', '').str.replace(' ', '')
champ_data['Tags'] = champ_data['Tags'].str.split(',')

actual = df.drop(['Champs', 'Avg. Assists', 'Avg. Kills', 'Avg. Deaths', 'Win Rate'], axis = 1)

def sort(sim_data):
    similarity = 1-pairwise_distances(sim_data.to_numpy(), metric='jaccard')
    y_pred = pd.DataFrame({'User Name':[], 'Champs': []})
    
    
    for nums, row in enumerate(similarity):
        #get users with greater than .95 
        
        row = np.argwhere(row > .50)

        #for x in rows:
        #create a list to store the recommended champs
        champ_rec = {}
        
        drop_champ = []
        
        #create list of champs the user is already using 
        user_= sim_data.iloc[nums]
        user_champ = user_.where(user_ == 1)
        user_champs = user_champ.dropna()
        
        for x in user_champs.index:
            drop_champ.append(x)
        # iterate through the similarity matrix to get users 
        for num in row:
            num = (num[0])
            user = sim_data.iloc[num]
            champs = user.where(user ==1)
            champs = champs.dropna()
            #iterate through the champ list and collect all the champs found
            for x in champs.index:
                if x in drop_champ:
                    continue
                else:
                    if x in champ_rec.keys():
                        champ_rec[x] = (champ_rec[x] +1)
                    else:
                        champ_rec[x] = 1 
        
        champ_rec = sorted(champ_rec, key=champ_rec.get, reverse=True)[:5]
        
        # make new row with user and recommended champions
        new_row = {'User Name': (sim_data.iloc[nums].name), 'Champs' : champ_rec}
        y_pred = y_pred.append(new_row, ignore_index = True)
    y_pred =y_pred.set_index('User Name', drop = True)
    return (y_pred)

def comp(df):
    lst_t = ['Tank', 'Fighter', 'Mage', 'Assassin', 'Support','Marksman']

    for x in lst_t:
        df[x] = 0
    for x in df.index:
        Champ = (df.loc[x]['Champs'])
        for char in Champ:
            tags = champ_data.loc[char]['Tags']
            for tag in tags:
                df[tag][x] = (df[tag][x] + 1)
    
            

            
        

    df['num of Champs'] = df['Champs'].map(lambda d: len(d))

    df['Tank'] = df['Tank'].div(df['num of Champs'])
    df['Fighter'] = df['Fighter'].div(df['num of Champs'])
    df['Mage'] = df['Mage'].div(df['num of Champs'])
    df['Assassin'] = df['Assassin'].div(df['num of Champs'])
    df['Support'] = df['Support'].div(df['num of Champs'])
    df['Marksman'] = df['Marksman'].div(df['num of Champs'])

    df = df.drop(['num of Champs', 'Champs'], axis = 1)
    
    return (df)


def MSE(orginal, predict):
    
    tank1 = orginal['Tank'].to_list()
    tank2 = predict['Tank'].to_list()
    
    fight1 = orginal['Fighter'].to_list()
    fight2 = predict['Fighter'].to_list()
    
    mage1 = orginal['Mage'].to_list()
    mage2 = predict['Mage'].to_list()
    
    ass1 = orginal['Assassin'].to_list()
    ass2 = predict['Assassin'].to_list()
    
    sup1 = orginal['Support'].to_list()
    sup2 = predict['Support'].to_list()
    
    mark1 = orginal['Marksman'].to_list()
    mark2 = predict['Marksman'].to_list()
    

    
    
    mse_tank = mean_squared_error(tank1, tank2, squared=False)
    mse_fight = mean_squared_error(fight1, fight2, squared=False)
    mse_mage = mean_squared_error(mage1, mage2, squared=False)
    mse_ass = mean_squared_error(ass1, ass2, squared=False)
    mse_sup = mean_squared_error(sup1, sup2, squared=False)
    mse_mark = mean_squared_error(mark1, mark2, squared=False)
    total = (mse_tank + mse_fight + mse_mage + mse_ass + mse_sup + mse_mark) / 6
    
    print (f'RMSE of tank {mse_tank}')
    print (f'RMSE of fight {mse_fight}')
    print (f'RMSE of mage {mse_mage}')
    print (f'RMSE of assasin {mse_ass}')
    print (f'RMSE of support {mse_sup}')
    print (f'RMSE of marksman {mse_mark}')
    
    print (f'RMSE Mean Total {total}')
    
    
def run(df):
    
    df_fixed = comp(df)
    recom = recommender(df_fixed, df)
    pred = comp(recom)
    
    MSE(df, pred)
    