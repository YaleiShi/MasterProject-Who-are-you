import numpy as np
import pandas as pd

a = np.zeros((2,3))
print(a)

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'super'],
        'Age':[27, 24, 22, 32, 54],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', "abc"],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd', 'Msc']}
df = pd.DataFrame(data)
print(len(df))
# print ("hello world")
# name = input("your name? ")
# print("your name is " + name)