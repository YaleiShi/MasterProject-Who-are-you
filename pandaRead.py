import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectFromModel
import joblib

# select = [7581, 10711, 9, 11135, 3866, 8078, 9320, 1771, 11144, 2836, 7366, 10425,
#  1339, 3678, 9317, 7640, 8987, 927, 10557, 10567, 5844, 5254, 10781, 4824, 3953,
#   9572, 410, 1193, 10846, 7185, 4362, 69, 5010, 8404, 6823, 4183, 6063, 9037, 3707,
#    2223, 4833, 3189, 2566, 8105, 5289, 3517, 4259, 3910, 7255, 760, 3612, 10171,
#     111, 1782, 10502, 2927, 1809, 10614, 7915, 10419, 1602, 9100, 4371, 10070, 1706,
#      11113, 10211, 5665, 1692, 4825, 5328, 3001, 10453, 7607, 1896, 3535, 4720,
#       4944, 3640, 455, 2884, 9092, 9475, 293, 5521, 7701, 3597, 8325, 9983, 4210, 10645,
#        10113, 9791, 10874, 7333, 3446, 10656, 2017, 6631, 6289]


print("reading files ... ")
df=pd.read_csv('./data/training.csv')
m = df.values

# df2=pd.read_csv('./data/test.csv')
# m2 = df2.values

model = joblib.load("./model/featureSelect.pkl")
selection = SelectFromModel(model, threshold=0.0043, prefit=True)

select_m = selection.transform(m)
print(select_m)
# print(m[:, 1])

# train_table = np.array(m[:, 0:2])
# test_table = np.array(m2[:, 0:2])

# for i in select:
# 	add1 = m[:, i+1]
# 	print(add1)
# 	add2 = m2[:, i+1]
# 	np.append(train_table, add1)
# 	np.append(test_table, add2)

# print(train_table[0:10])
# pd.DataFrame(train_table).to_csv("./data/feature_reduced_100.csv")
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 

df = pd.DataFrame(data)
array = df.values
print(df[:2, 2])
print(array[:, 1])
# dataTable = pd.read_csv("./data/test.csv")

# html = dataTable[0:3].to_html()
# with open("data.html", "w") as f:
# 	f.write(html)

# full_filename = os.path.abspath("data.html")
# webbrowser.open("file://{}".format(full_filename))