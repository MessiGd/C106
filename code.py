import csv
from statistics import correlation 
import plotly.express as px
import numpy as np

def plotfigure(data_path):
    with open(data_path) as a:
        read = csv.DictReader(a)
        fig = px.scatter(read, x = "Temperature", y = "Ice-cream Sales")
        fig.show()

def getdatasource(data_path):
    ice_cream_sales = []
    temp = []
    with open(data_path) as b:
        read = csv.DictReader(b) 
        for i in read:
            temp.append(float(i["Temperature"]))
            ice_cream_sales.append(int(i["Ice-cream Sales"]))
    return{"x":temp, "y":ice_cream_sales}

def findcorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source ["y"])
    print("Correlation:", correlation[0,1])

def main():
    data_path = "1.csv"
    data_source = getdatasource(data_path)
    findcorrelation(data_source)
    plotfigure(data_path)

main()