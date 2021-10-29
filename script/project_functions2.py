import pandas as pd
import numpy as np
def load_and_process():

    df1 = (
        pd.read_csv("/Users/noahandrew/school/year3/Data301/project-group31-project/player_info.csv")
        .drop('birthCity', axis=1)
        .drop('birthDate', axis=1)
        .drop('birthStateProvince', axis=1)
        .drop('primaryPosition', axis=1)
        .drop('weight', axis=1)
        .drop('height_cm', axis=1)
        .drop('height', axis=1)
    )
    
    df2 = (
            df1
            .rename(columns={'shootsCatches': 'Shooting / Catching Hand'})
            .rename(columns={'player_id': 'Player ID'})
            .set_index('Shooting / Catching Hand')                                       
            .rename(index={'L': 'Left'})
            .rename(index={'R': 'Right'})
       
    )
    
    return df2