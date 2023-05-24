import pandas as pd
import json
import numpy as np
import math
import os
import argparse
import re

class DataHandler:
    def __init__(self, file_path, data_type):
        
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.data = {data_type: []}
        self.data_type = data_type

    def read_excel_file(self):
        print(self.file_name)
        return pd.read_excel(f'{self.file_path}')

    def process_rows(self, row):
        data_r = {'dateRange': row['period']}

        parameters = ['control', 'rcp2.6', 'rcp4.5', 'rcp8.5']

        for param in parameters:
            if not math.isnan(row[param]):
                data_r[param] = row[param]

        return data_r

    def process_data(self, data_frame):
        for _, row in data_frame.iterrows():
            self.data[self.data_type].append(self.process_rows(row))

    def get_data(self):
        return self.data


def process_file(file_path):
    if os.path.basename(file_path).startswith('Pre'):
        data_type = 'rain'
    else:
        data_type = 'temp'
    
    data_handler = DataHandler(file_path, data_type)
    excel_data_df = data_handler.read_excel_file()
    data_handler.process_data(excel_data_df)
    return data_handler.get_data()

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--folder', help='Folder location ')
    
    args = parser.parse_args()

    if args.folder:
        folder_path = args.folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    else:
        folder_path = ''
        files = [input("File name:")]
        
    for file in files:
        # or
        if not re.match(r'^(Pre|Tmean)_', file) or not re.search(r'\.xls$', file):
            print(f"Skipping file: {file}. Invalid file name format.")
            continue
            
        file_path = os.path.join(folder_path, file)
        data = process_file(file_path)
        file = file.replace('.xls', '')
        with open(f'{folder_path}/{file}.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)
        
    print("Finished!")

if __name__ == "__main__":
    main()
