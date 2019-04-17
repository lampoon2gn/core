from flask import jsonify
from models import Sheet
import pandas as pd

class Search():

    def df_builder(self):
        response = Sheet.query.with_entities(Sheet.sheet_label, Sheet.effvel).all()

        master_number_data = []
        master_label_data = []

        for i in range(len(response)):
            one_sheet_number_data = []
            for data in response[i][1]:
                if data != None:
                    one_sheet_number_data.append(float(data))
                else:
                    one_sheet_number_data.append('')
            
            master_number_data.append(pd.Series(one_sheet_number_data))
            master_label_data.append(str(response[i][0]))

        df = pd.concat(master_number_data, axis=1, keys=[label for label in master_label_data])

        return str(df.shape)


    def analyze():
        search = Search()
        return search.df_builder()