from cal_elo import MultiPlayerEloGenerator
import pandas as pd



if __name__ == '__main__':

    df = pd.read_csv("1417_horse_racing_result.csv", index_col=0)
    df = df[['source', 'horse_id','finishing_position','trainer','jockey', 'year_index']]
    elogen = MultiPlayerEloGenerator( df, 16)
    elogen.generateHorseElo()
    df = elogen.getEloHorseDf()
    df.to_csv('horse_elo.csv')