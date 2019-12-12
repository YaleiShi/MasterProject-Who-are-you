import os
import json
from flask import Flask, request, redirect, url_for, jsonify

from data_process import *
import random
import joblib
from MFCC_gen import *
import tensorflow as tf
from tensorflow import keras

UPLOAD_FOLDER = 'uploads/'
MODEL_PATH = "./model/cnn_model.h5"

ALLOWED_EXTENSIONS = set(['m4a'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True






# cnn = create_cnn_model()
# cnn = joblib.load(MODEL_PATH)
cnn = tf.keras.models.load_model(MODEL_PATH)
#cnn._make_predict_function()
graph = tf.get_default_graph()


#
@app.route('/')
def hello():
    return "Hello, who are you team"

@app.route("/predict/nativeness", methods=['GET','POST'])
def index():
    data = {"feature": "nativness", "prob": 0}
    if request.method == 'POST':
        file = request.files['sound']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


        # use src to convert src file into a wav file, and return path - dst
        src = UPLOAD_FOLDER + filename
        dst = convert_m4a(src)


        X = generate_mfcc(dst)

        data = {}
        global graph
        with graph.as_default():
            out = cnn.predict(X, verbose=1)
            data["prob"] = out
        # print(out[0])
        data["feature"] = "nativeness"

    return jsonify(data)
#
#
#

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
