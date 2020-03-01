import pandas as pd
import numpy as numpy

def cleanData(input_name, outputname):

    csvFile = input_name
    csv_output_file = outputname

    # csvFile = 'data.csv'
    dataLoad = pd.read_csv(csvFile)

    # dataLoad.head()
    # datos que queremos
    cleanData = dataLoad[['Name', 'Last Name', 'City']]
    
    # cleanData.to_csv('cleandata.csv')
    cleanData.to_csv(csv_output_file)