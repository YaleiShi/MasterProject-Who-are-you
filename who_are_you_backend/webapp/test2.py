import h5py

MODEL_PATH = "./model/cnn_model.h5"
f = h5py.File(MODEL_PATH, 'r')
print(f.attrs.get('keras_version'))
