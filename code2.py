import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    icecreamSales=[]
    temperature=[]
    with open (data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            icecreamSales.append(float(row['Ice-cream Sales'])) 
            temperature.append(float(row['Temperature']))
    return{'x': icecreamSales,'y': temperature}
def find_correlation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print('correlation between temperature v/s icecreamsales',correlation[0,1])
def setup():
    data_path='ice.csv'
    data_source=getdatasource(data_path)
    find_correlation(data_source)
setup()
