import joblib
import numpy as np

def reverseFeatures(x):
	x = np.sort(x)
	x= x[::-1]

	for i in range(0, 100):
		print(x[i])


model = joblib.load("./model/featureSelect.pkl")
# print(model.feature_importances_)
reverseFeatures(model.feature_importances_)


# important_features_dict = {}
# for x,i in enumerate(model.feature_importances_):
#     important_features_dict[x]=i


# important_features_list = sorted(important_features_dict,
#                                  key=important_features_dict.get,
#                                  reverse=True)

# for i in range (0, 100):
# 	print(important_features_list[i], ",")