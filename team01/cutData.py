import pandas as pd
import webbrowser
import os

dataTable = pd.read_csv("./data/training.csv")
del dataTable['name']
dataTable['pros'].to_csv('./data/noName_training_Y.csv')
del dataTable['pros']
dataTable.to_csv('./data/noName_training_X.csv')