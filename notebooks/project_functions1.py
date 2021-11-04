def load_and_process():


        df1 = (
                pd.read_csv("../data/raw/player_info.csv")
                .drop('height', axis=1)
                .drop('birthCity', axis=1)
                .drop('birthDate', axis=1)
                .drop('birthStateProvince', axis=1)
        )
        
        
        
        df2 = (
                df1
                .rename(columns={"player_id": "Player ID"})
                .set_index('primaryPosition')                                       
                .rename(index={"D": "Defence"})
                .rename(index={"G": "Goalie"})
                .rename(index={"C": "Center"})
                .rename(index={"RW": "Right Wing"})
                .rename(index={"LW": "Left Wing"})
        )
        
        return df2
    
    