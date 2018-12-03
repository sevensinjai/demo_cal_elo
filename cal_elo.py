
import pandas as pd
from multi_elo import EloPlayer, calc_new_elos



class MultiPlayerEloGenerator():
    def __init__(self , resultDictDf, kFactor):
        self._initElo = {}
        self._initJockeyElo = {}
        self._initTrainerElo = {}
        self._resultListOfDict = {}
        self._resultDictDf = resultDictDf
        self._kFactor = kFactor
        self._output = pd.DataFrame(columns=["race_identifier", '1','2',"3","4","5","6","7","8","9","10","11","12","13","14"])

    def generateHorseElo(self, year_index=None):
        horseIdList = self._resultDictDf['horse_id'].unique()
        horseIdDict ={}
        for x in horseIdList:
            horseIdDict[x] = 1500
        self._initElo = horseIdDict

        # features engineering
        tmpDf = self._resultDictDf
        if (year_index):
            tmpDf = tmpDf[tmpDf.year_index == year_index]
        
        tmpDf['date'] = self._resultDictDf['source'].apply(lambda x : x.split("_")[0])
        tmpDf['race_no'] = self._resultDictDf['source'].apply(lambda x : x.split("_")[-1]).astype(int)
        tmpDf = self._resultDictDf.sort_values(["date","race_no"])
        tmpDf = tmpDf[['source','date','race_no','horse_id', 'finishing_position']]
        
        # transform result df into list of dict
        sourceList = tmpDf['source'].unique()
        master_list = []
        counter = 0
        for item in sourceList:
            print (" transforming df into list of dict... ",counter + 1)
            counter += 1
            resultDf = tmpDf[tmpDf.source == item]
            tmpDict = {}
            for row in resultDf.iterrows():
                tmpDict[row[1]['horse_id']] = row[1]["finishing_position"] 
            master_list.append(tmpDict)
            # if counter > 5:
                # break
        self._resultListOfDict = master_list


        #cal the new elo
        resultList = []
        for source, result in enumerate(self._resultListOfDict):
            eloPlayerList = []
            for participant in result:
                eloPlayerList.append(EloPlayer(place= result[participant], elo = self._initElo[participant]))
            list_of_player = list(result.keys())
            new_elos = calc_new_elos(eloPlayerList, self._kFactor)
            for index, item in enumerate(new_elos):
                self._initElo[list_of_player[index]] = item
                item_to_be_saved = [sourceList[source], list_of_player[index], eloPlayerList[index].elo,item]
                resultList.append(item_to_be_saved)
        header_list= ['source', 'horse_id', 'original_elo','new_elo']
        df = pd.DataFrame(data=resultList, columns=header_list)
        self._elodf = df
        #write down the elo of each horse

    def generateJockeyElo(self, year_index):

        jockeyList = self._resultDictDf['jockey'].unique()
        jockeyDict ={}
        for x in jockeyList:
            jockeyDict[x] = 1500
        self._initJockeyElo = jockeyDict

        # features engineering
        tmpDf = self._resultDictDf
        if (year_index):
            tmpDf = tmpDf[tmpDf.year_index == year_index]
        
        tmpDf = self._resultDictDf['source'].apply(lambda x : x.split("_")[0])
        tmpDf = self._resultDictDf['source'].apply(lambda x : x.split("_")[-1]).astype(int)
        tmpDf = self._resultDictDf.sort_values(["date","race_no"])
        tmpDf = tmpDf[['source','date','race_no','jockey', 'finishing_position']]
        
        # transform result df into list of dict
        sourceList = tmpDf['source'].unique()
        master_list = []
        counter = 0
        for item in sourceList:
            print (" transforming df into list of dict... ",counter + 1)
            counter += 1
            resultDf = tmpDf[tmpDf.source == item]
            tmpDict = {}
            for row in resultDf.iterrows():
                tmpDict[row[1]['jockey']] = row[1]["finishing_position"] 
            master_list.append(tmpDict)
            # if counter > 5:
                # break
        self._resultListOfDict = master_list


        #cal the new elo
        resultList = []
        for source, result in enumerate(self._resultListOfDict):
            eloPlayerList = []
            for participant in result:
                eloPlayerList.append(EloPlayer(place= result[participant], elo = self._initJockeyElo[participant]))
            list_of_player = list(result.keys())
            new_elos = calc_new_elos(eloPlayerList, self._kFactor)
            for index, item in enumerate(new_elos):
                self._initJockeyElo[list_of_player[index]] = item
                item_to_be_saved = [sourceList[source], list_of_player[index], eloPlayerList[index].elo,item]
                resultList.append(item_to_be_saved)
        header_list= ['source', 'jockey', 'original_elo','new_elo']
        df = pd.DataFrame(data=resultList, columns=header_list)
        self._eloTrainerDf = df
    
    def generateTrainerElo(self, year_index):

            jockeyList = self._resultDictDf['trainer'].unique()
            jockeyDict ={}
            for x in jockeyList:
                jockeyDict[x] = 1500
            self._initTrainerElo = jockeyDict

            # features engineering
            tmpDf = self._resultDictDf
            if (year_index):
                tmpDf = tmpDf[tmpDf.year_index == year_index]
            
            tmpDf = self._resultDictDf['source'].apply(lambda x : x.split("_")[0])
            tmpDf = self._resultDictDf['source'].apply(lambda x : x.split("_")[-1]).astype(int)
            tmpDf = self._resultDictDf.sort_values(["date","race_no"])
            tmpDf = tmpDf[['source','date','race_no','trainer', 'finishing_position']]
            
            # transform result df into list of dict
            sourceList = tmpDf['source'].unique()
            master_list = []
            counter = 0
            for item in sourceList:
                print (" transforming df into list of dict... ",counter + 1)
                counter += 1
                resultDf = tmpDf[tmpDf.source == item]
                tmpDict = {}
                for row in resultDf.iterrows():
                    tmpDict[row[1]['trainer']] = row[1]["finishing_position"] 
                master_list.append(tmpDict)
                # if counter > 5:
                    # break
            self._resultListOfDict = master_list


            #cal the new elo
            resultList = []
            for source, result in enumerate(self._resultListOfDict):
                eloPlayerList = []
                for participant in result:
                    eloPlayerList.append(EloPlayer(place= result[participant], elo = self._initTrainerElo[participant]))
                list_of_player = list(result.keys())
                new_elos = calc_new_elos(eloPlayerList, self._kFactor)
                for index, item in enumerate(new_elos):
                    self._initTrainerElo[list_of_player[index]] = item
                    item_to_be_saved = [sourceList[source], list_of_player[index], eloPlayerList[index].elo,item]
                    resultList.append(item_to_be_saved)
            header_list= ['source', 'jockey', 'original_elo','new_elo']
            df = pd.DataFrame(data=resultList, columns=header_list)
            self._eloTrainerDf = df

    def getEloHorseDf(self):
        return self._elodf

    def getEloJockeyDf(self):
        return self._eloTrainerDf
    
    def getEloTrainerDf(self):
        return self._eloTrainerDf
