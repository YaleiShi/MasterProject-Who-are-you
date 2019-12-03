import os
import json
# from flask import Flask, request, redirect, url_for, jsonify

from data_process import *
import random
import joblib
from MFCC_gen import *
import tensorflow as tf
from tensorflow import keras

UPLOAD_FOLDER = 'uploads/'
MODEL_PATH = "./model/cnn_model.h5"

ALLOWED_EXTENSIONS = set(['m4a'])

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.debug = True

# cnn = create_cnn_model()
# cnn = joblib.load(MODEL_PATH)
cnn = tf.keras.models.load_model(MODEL_PATH)
cnt = 0
#
# @app.route('/')
# def hello():
#     return "Hello, who are you team"
#
# @app.route("/predict/gender", methods=['GET','POST'])
# def index():
#     global cnt
#     data = {"gender": "female", "prob": 0}
#     if request.method == 'POST':
#         file = request.files['sound']
#         cnt += 1
#         filename = file.filename
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         print(filename)
#
#         # use src to convert src file into a wav file, and return path - dst
#         src = UPLOAD_FOLDER + filename
#         dst = convert_m4a(src)
#         print(dst)
#
#         # use dst to load target wav file and convert it into a mfcc file
dst = "wavs/tool.wav"
X = generate_mfcc(dst)
print(np.shape(X))

        # force align
# force_align_mfcc = force_align(raw_mfcc)

        # read final mfcc array
# X = get_numpy_mfcc(force_align_mfcc)
#
out = cnn.predict(X, verbose=1)
print(out)
#         result = out[0][0]
#
#         # result = 1
#         print(result)
#         if result == 1:
#             data["gender"] = "male"
#             data["prob"] = 50 + random.randint(1, 49)
#         else:
#             data["gender"] = "female"
#             data["prob"] = 50 + random.randint(1, 49)
#     return jsonify(data)
#
#
#
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)
