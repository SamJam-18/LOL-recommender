import pandas as pd

import numpy as np

#import User data
df = pd.read_csv('/Users/samanthajamwal/Desktop/LOL/Master/User_data_1.csv')
df = df.drop_duplicates('User Name')
df = df.set_index(df['User Name'])

#Clean the user data so that the champs line up with Champ_data
df['Champs'] = df['Champs'].str.replace('{', '').str.replace('}', '').str.replace('\'','').str.replace(': ', '').str.replace('7', '').str.replace('6', '').str.replace('5', '').str.replace('4', '').str.replace('3', '').str.replace('2', '').str.replace('1', '').str.replace(' ', '')
df['Champs'] = df['Champs'].str.replace('Dr.Mundo', 'DrMundo').str.replace('\"', '').str.replace('&Willump', '').str.replace('LeBlanc', 'Leblanc').str.replace('KhaZix', 'Khazix').str.replace('ChoGath', 'Chogath').str.replace('KaiSa', 'Kaisa').str.replace('Wukong', 'MonkeyKing').str.replace('VelKoz', 'Velkoz')


df['Champs'] = df['Champs'].str.split(',')



df.to_csv('/Users/samanthajamwal/Desktop/LOL/Master/User_data_Clean.csv')