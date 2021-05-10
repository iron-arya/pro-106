import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    size_tv=[]
    avg_time=[]
    with open (data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            size_tv.append(float(row['Size of TV'])) 
            avg_time.append(float(row['hi']))
    return{'x': size_tv,'y': avg_time}
def find_correlation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print('correlation between size_tv v/s avg_time',correlation[0,1])
def setup():
    data_path='tv.csv'
    data_source=getdatasource(data_path)
    find_correlation(data_source)
setup()
