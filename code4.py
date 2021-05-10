import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    days_present=[]
    marks=[]
    with open (data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            days_present.append(float(row['Days Present'])) 
            marks.append(float(row['Marks In Percentage']))
    return{'x': days_present,'y': marks}
def find_correlation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print('correlation between days_present v/s marks',correlation[0,1])
def setup():
    data_path='std.csv'
    data_source=getdatasource(data_path)
    find_correlation(data_source)
setup()
