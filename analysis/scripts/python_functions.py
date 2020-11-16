import pandas as pd
#import altair as alt
import datetime
import time
#import pdb
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling

def blue_or_red(dataframe, variable):
    df = dataframe
    df['first' + variable] = np.where(df['blueFirst' + variable] == 1, 'blue', 
                                 (np.where(df['redFirst' + variable] == 1, 'red', 'none')))
    return df

def load_and_process(url_or_path_to_csv_file):
    
    df = pd.read_csv(url_or_path_to_csv_file)
    
    count_nan = df.isnull().sum().sum()
    if count_nan > 0:
        print("There are {} NaN values in the dataset.".format(count_nan))
    
    df['winner'] = np.where(df['blueWins'] == 1, 'blue', (np.where(df['gameDuraton'] > 250, 'red', 'remake')))
    
    objectives = ['Blood', 'Tower', 'Baron', 'Dragon', 'Inhibitor']
    for objective in objectives:
        blue_or_red(df, objective)

    df['gameLength'] = np.where(df['gameDuraton'] > 2400, 'long',
                               (np.where(df['gameDuraton'] > 1200, 'medium', 'short')))
    
    df['gameTime'] = df['gameDuraton'].apply(lambda x: time.strftime("%M:%S",time.gmtime(x)))
    
    df = (df.drop(columns = ['blueWins', 
                             'blueFirstBlood', 
                             'blueFirstTower',
                             'blueFirstBaron', 
                             'blueFirstDragon', 
                             'blueFirstInhibitor',
                             'redWins', 
                             'redFirstBlood', 
                             'redFirstTower',
                             'redFirstBaron', 
                             'redFirstDragon', 
                             'redFirstInhibitor'])
          .rename(columns = {"gameId":"gameID",
                             "gameDuraton":"gameDuration",
                             "blueWardPlaced":"blueWard",
                             "blueWardkills":"blueWardKills",
                             "blueDeath":"blueDeaths",
                             "blueAssist":"blueAssists",
                             "blueChampionDamageDealt":"blueChampionDamage",
                             "blueTotalHeal":"blueTotalHealing",
                             "blueObjectDamageDealt":"blueObjectiveDamage",
                             "blueTotalMinionKills":"blueTotalCS",
                             "blueJungleMinionKills":"blueJungleCS",
                             "redWardPlaced":"redWard",
                             "redWardkills":"redWardKills",
                             "redDeath":"redDeaths",
                             "redAssist":"redAssists",
                             "redChampionDamageDealt":"redChampionDamage",
                             "redTotalHeal":"redTotalHealing",
                             "redObjectDamageDealt":"redObjectiveDamage",
                             "redTotalMinionKills":"redTotalCS",
                             "redJungleMinionKills":"redJungleCS"})
         .reindex(columns = ['gameID', 
                             'gameTime',
                             'gameDuration',
                             'gameLength',
                             'winner', 
                             'firstBlood', 
                             'firstTower', 
                             'firstDragon',
                             'firstBaron', 
                             'firstInhibitor',
                             'blueTowerKills',
                             'blueDragonKills',
                             'blueBaronKills', 
                             'blueInhibitorKills', 
                             'blueWard', 
                             'blueWardKills',
                             'blueKills', 
                             'blueDeaths', 
                             'blueAssists', 
                             'blueTotalLevel', 
                             'blueAvgLevel',
                             'blueChampionDamage', 
                             'blueObjectiveDamage',
                             'blueTotalHealing', 
                             'blueTotalGold', 
                             'blueTotalCS',
                             'blueJungleCS', 
                             'blueKillingSpree',
                             'redTowerKills',
                             'redDragonKills',
                             'redBaronKills', 
                             'redInhibitorKills', 
                             'redWard', 
                             'redWardKills',
                             'redKills', 
                             'redDeaths', 
                             'redAssists', 
                             'redTotalLevel', 
                             'redAvgLevel',
                             'redChampionDamage', 
                             'redObjectiveDamage',
                             'redTotalHealing', 
                             'redTotalGold', 
                             'redTotalCS',
                             'redJungleCS', 
                             'redKillingSpree']))
    
    df = df[df.winner != 'remake']

    return df
