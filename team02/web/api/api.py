from flask import Flask, escape, request, json

import timit_data
import mdata



app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'




@app.route('/word')
def hello2():
    id = request.args.get("id", 0)
    path = mdata.getRecordPathRoot(id)

    data = timit_data.load_word(path + ".WRD")
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return  response


@app.route('/wave')
def wave():
    id = request.args.get("id", 0)
    path = mdata.getRecordPath(id)
    data = timit_data.load_wave(path)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return  response


@app.route('/phn')
def phone():
    id = request.args.get("id", 0)
    path = mdata.getRecordPathRoot(id)
    data = timit_data.load_phn(path + ".PHN")
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return  response

@app.route('/spc')
def spc():
    start = request.args.get("start", 0)
    end = request.args.get("end", 0)
    start = int(start)
    end = int(end)
    data = timit_data.load_spectrogram("", start, end)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return  response

@app.route('/record')
def record():
    region = request.args.get("region", 0)
    region = int(region)
    data = mdata.getRecords(region)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return  response

@app.route('/recordInfo')
def recordInfo():
    id = request.args.get("id", 0)
    data = mdata.getRecordInfo(id)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return  response
