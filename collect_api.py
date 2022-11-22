import numpy as np
import pandas as pd
import opendota as od
import json

path = f'R:\0\'
df_leagues = pd.read_json(path + 'leagues.json')
df_teams = pd.read_json(path + 'teams.json')
df_heroes = pd.read_json(path + 'heroes.json')
