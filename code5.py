import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    cof=[]
    sleep=[]
    with open (data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            cof.append(float(row['Coffee in ml'])) 
            sleep.append(float(row['sleep in hours']))
    return{'x': cof,'y': sleep}
def find_correlation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print('correlation between cof v/s sleep',correlation[0,1])
def setup():
    data_path='coffee.csv'
    data_source=getdatasource(data_path)
    find_correlation(data_source)
setup()
