from BiRNN import BiRNN
from BiRNN import BiRNN3
import torch
from keras import layers
from keras.models import Model

input_size = 235
hidden_size = 128
num_layers = 2
num_classes = 2  # TODO: Determine this from the data

def create_model():
    rnn = BiRNN3(input_size, hidden_size, num_layers, num_classes)
    # todo yousong zhang
    #rnn.load_state_dict(torch.load('webapp/GRU.pkl', map_location='cpu'))
    rnn.eval()
    return rnn

def create_cnn_model():
	print('... construct network')

    inputs = layers.Input((20, 1241, 1))
    x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    x = layers.Conv2D(32, (3, 3), activation='relu')(x)
    x = layers.MaxPool2D((2, 2))(x)
    x = layers.Dropout(0.25)(x)
    x = layers.Flatten()(x)
    x = layers.Dense(128)(x)
    x = layers.Dropout(0.5)(x)
    out = layers.Dense(1, activation='linear')(x)

    return Model(inputs=inputs, outputs=out)

def torch_max(model, mfcc):
    outputs = model(mfcc)
    _, predicted = torch.max(outputs.data, 1)
    return predicted
