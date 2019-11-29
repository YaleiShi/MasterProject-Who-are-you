import os
import librosa
from pydub import AudioSegment
import torch.tensor as tensor
from torch.autograd import Variable

# files
input_size = 235
sequence_length = 40
hidden_size = 128
num_layers = 2
num_classes = 2  # TODO: Determine this from the data
learning_rate = 0.0001
num_epochs = 20000

# convert wav to mp3
def convert_m4a(src):
    filename = os.path.splitext(os.path.basename(src))[0]

    sound = AudioSegment.from_file(src)
    dst = 'wavs' + '/' + filename + '.wav'

    sound.export(dst, format="wav")
    return dst


path = convert_m4a("uploads/1575007703.m4a")
print(path)
