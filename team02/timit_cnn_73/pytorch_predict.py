import os
import numpy as np
import torch
import torch.nn as nn


# Device configuration
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
#device = torch.device('cpu')
num_classes = 48

f = open("48_new.txt")
target = f.read().splitlines()
f.close()

map48 = {}

for i, val in enumerate(target):
    map48[val] = i

map48_phoneme = {}

for i, val in enumerate(target):
    map48_phoneme[i] = val


def prepare_data():
    test_x = np.load("test_x_p.txt.npy")
    test_y = np.load("test_y_p.txt.npy")

    print("shape of test_x" ,np.shape(test_x))
    print("shape of test_y" ,np.shape(test_y))
    return (test_x, test_y)


class ConvNet(nn.Module):
    def __init__(self, num_classes=48):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 128, kernel_size=(3, 3), stride=1, padding=0),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(128, 128, kernel_size=(3, 3), stride=1, padding=0),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))


        self.fc = nn.Linear(4*8*128, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.4)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        #out = self.dropout(out)
        out = out.reshape(out.size(0), -1)
        #out = self.dropout(out)
        out = self.fc(out)
        out = self.dropout2(out)
        out = self.fc2(out)

        return out





def product():
    x_test, y_test = prepare_data()
    model = ConvNet(num_classes).to(device)

    model.load_state_dict(torch.load('72model.ckpt', map_location='cpu'))
    model.eval()
    #print(model)


    calculate(model, x_test, y_test)


def calculate(model, x_test_local, y_test_local):

    correct = 0
    total = 0
    x_test_tensor = torch.from_numpy(x_test_local).float()


    outputs = model(x_test_tensor)
    _, predicted = torch.max(outputs.data, 1)
    answer = np.array([np.argmax(i) for i in y_test_local])
    predict = predicted.cpu().numpy()

    acc = np.sum(predict == answer) / len(predict)
    for i in range(len(predict)):
        print(map48_phoneme[predict[i]], '-->', map48_phoneme[answer[i]])
    print('Single phone test accuracy: {:.2%}'.format(acc))
    print('----------------------------------\n')


if __name__ == '__main__':
    product()
