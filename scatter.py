import csv
import pandas as ps
import plotly.express as px

read = ps.read_csv('1.csv')
fig = px.scatter(read, x = "Ice-cream Sales", y = "Temperature", size_max = 40)
fig.show()
