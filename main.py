import pandas
import json
import numpy
import math



def rain(file_name):

    file = file_name

    excel_data_df = pandas.read_excel('Pre_'+file+'.xls',  ) 

    dct = {
        'rain':[]        
    }

    for index, row in excel_data_df.iterrows():
        data_r = {}

        daterange = row['period']
        control   = row['control']
        rcp26     = row['rcp2.6']
        rcp45     = row['rcp4.5']
        rcp85     = row['rcp8.5']

        data_r['dateRange'] = daterange

        if(not math.isnan(control)):
            data_r['control'] = control
        
        if(not math.isnan(rcp26)):
            data_r['rcp26'] = rcp26
        
        if(not math.isnan(rcp45)):
            data_r['rcp45'] = rcp45
        
        if(not math.isnan(rcp85)):
            data_r['rcp85'] = rcp85
        

        dct['rain'].append(data_r)

    with open('Pre_'+file+'.json','w') as outfile:  
        outfile.write(json.dumps(dct, indent=2, ensure_ascii=False))

def temp(file_name):

    file = file_name

    excel_data_df = pandas.read_excel('Tmean_'+file+'.xls',  ) 

    dct = {
        'temp':[]        
    }

    for index, row in excel_data_df.iterrows():
        data_r = {}

        daterange = row['period']
        control   = row['control']
        rcp26     = row['rcp2.6']
        rcp45     = row['rcp4.5']
        rcp85     = row['rcp8.5']

        data_r['dateRange'] = daterange

        if(not math.isnan(control)):
            data_r['control'] = control
        
        if(not math.isnan(rcp26)):
            data_r['rcp26'] = rcp26
        
        if(not math.isnan(rcp45)):
            data_r['rcp45'] = rcp45
        
        if(not math.isnan(rcp85)):
            data_r['rcp85'] = rcp85
        

        dct['temp'].append(data_r)

    with open('Tmean_'+file+'.json','w') as outfile:  
        outfile.write(json.dumps(dct, indent=2, ensure_ascii=False))

def main():
    file_name = input("File name:")
    temp(file_name)
    rain(file_name)
    print("Finished!")

main()

