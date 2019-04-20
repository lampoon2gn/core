import os
import pandas as pd
from numpy import nan
from models import Sheet
from flask import jsonify
from decimal import Decimal
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


class Search():

    def df_builder(self, feature_name):
        dict_of_features = {'avgmoe': Sheet.avgmoe, 'avgsg': Sheet.avgsg, 'avgmc': Sheet.avgsg, 'avgvel': Sheet.avgvel, 
        'avgupt': Sheet.avgupt, 'pkdensity': Sheet.pkdensity, 'effvel': Sheet.effvel, 'lvel': Sheet.lvel, 'rvel': Sheet.rvel,
        'lupt': Sheet.lupt, 'rupt': Sheet.rupt, 'sg': Sheet.sg, 'mc': Sheet.mc}

        response = Sheet.query.with_entities(Sheet.sheet_label, dict_of_features[feature_name.lower()]).all()

        master_number_data = []
        master_label_data = []

        for i in range(len(response)):
            one_sheet_number_data = []
            for data in response[i][1]:
                if data != None:
                    one_sheet_number_data.append(float(data))
                else:
                    one_sheet_number_data.append(nan)
            
            master_number_data.append(pd.Series(one_sheet_number_data))
            master_label_data.append(str(response[i][0]))

        df = pd.concat(master_number_data, axis=1, keys=[label for label in master_label_data])

        return df


    #return wheel feature_of_interest for input sheet 
    def wheel_feature_compiler(self, in_filename,feature_of_interest):
        columns = ["pos","EffVel","effUPT","LeftVel","LeftUPT","RightVel","RightUPT"]
        df = pd.DataFrame(columns=columns)
        input_file = open(in_filename)
        write_status = False

        for line in input_file:
            if line == '"Avg Vel","stdev Vel.","avg UPT","stdev UPT"\n':
                break
            if write_status:
                if(len(line.split(','))==len(df.columns)):
                    df.loc[len(df)]=[nan if (x=='""' or x == ''or x==None) else float(x) for x in line.replace('\n','').split(',')]
            if line == '"pos","EffVel","effUPT","LeftVel","LeftUPT","RightVel","RightUPT"\n':
                write_status = True
        
        return df[feature_of_interest]


    #return cavity feature_of_interest for input sheet 
    def cavity_feature_compiler(self, in_filename,feature_of_interest):
        columns = ["Row#","Position1","MC1","SG1","X1","dF1","ddB1","dQ1","Position2","MC2","SG2","X2","dF2","ddB2","dQ2","Position3","MC3","SG3","X3","dF3","ddB3","dQ3","Position4","MC4","SG4","X4","dF4","ddB4","dQ4","Position5","MC5","SG5","X5","dF5","ddB5","dQ5","Position6","MC6","SG6","X6","dF6","ddB6","dQ6","Position7","MC7","SG7","X7","dF7","ddB7","dQ7"]
        df = pd.DataFrame(columns =columns)
        input_file = open(in_filename)
        write_status = False

        for line in input_file:
            if line.split(',')[0] == '"avg MC"':
                break
            if write_status:
                if(len(line.split(','))==len(df.columns)):
                    df.loc[len(df)]=[nan if (x=='""' or x == '' or x==None) else float(x) for x in line.replace('\n','').split(',')]
            if line.split(',')[0] == '"Row#"':
                write_status = True
        
        return df[feature_of_interest]


    #produce complete_df with the input sheet as the last column
    def input_preprocess(self, in_filename,feature_of_interest):
        db_df = self.df_builder(feature_of_interest)

        if feature_of_interest == "EffVel":
            input_df = self.wheel_feature_compiler(in_filename,feature_of_interest)
            #input_df = input_df.dropna(thresh=int(0.95*(input_df.shape[0]))).reset_index()
            if input_df.shape[0]>len(db_df):
                input_df = input_df.drop(range(len(db_df),len(input_df)))
            complete_df = pd.concat((db_df,input_df),axis=1,sort=False)
            complete_df = complete_df.fillna(value = complete_df.mean(axis=0))
            complete_df = complete_df.sub(complete_df.mean(axis=0),axis=1)
            
        else:
            input_df = self.cavity_feature_compiler(in_filename,feature_of_interest)
            if input_df.shape[0]>len(db_df):
                input_df = input_df.drop(range(len(db_df),len(input_df)))
            complete_df = pd.concat((db_df,input_df),axis=1,sort=False)
            complete_df = complete_df.dropna(thresh=0.95*len(complete_df.columns)).reset_index(drop=True).drop(range(0,20)).reset_index(drop=True)
            complete_df = complete_df.fillna(value = complete_df.mean(axis=0))
            complete_df = complete_df.sub(complete_df.mean(axis=0),axis=1)
        
        return complete_df


    #use cos_similarity to compare
    def compare_input_with_db(self, complete_df,feature_of_interest,top_x):
        ratings={}
        result_dic={}
        for sheet in complete_df:
            if sheet != feature_of_interest:
                rating = cosine_similarity(complete_df[feature_of_interest].values.reshape(1, -1),complete_df[sheet].values.reshape(1, -1))
                ratings[sheet] = rating
        sorted_ratings = [{k: ratings[k][0][0]} for k in sorted(ratings, key=ratings.get, reverse=True)]
        result = sorted_ratings[0:top_x]
        for d in result:
            result_dic.update(d)
        
        return result_dic


    def identify(self, in_filename,feature_of_interest,top_x):
        complete_df = self.input_preprocess(in_filename,feature_of_interest)
        result = self.compare_input_with_db(complete_df,feature_of_interest,top_x)
        
        return result


    def analyze(input_file):
        search = Search()
        
        return search.identify(input_file,"EffVel",5)