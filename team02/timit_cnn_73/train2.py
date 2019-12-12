"""
    File name: train.py
    Function Des:

    ~~~~~~~~~~

    author: Skyduy <cuteuy@gmail.com> <http://skyduy.me>

"""
import os
import numpy as np




# from core.utils import load_data, APPEARED_LETTERS
#
#
# def prepare_data(folder):
#     print('... loading data')
#     letter_num = len(APPEARED_LETTERS)
#     data, label = load_data(folder)
#     data_train, data_test, label_train, label_test = \
#         train_test_split(data, label, test_size=0.1, random_state=0)
#     label_categories_train = to_categorical(label_train, letter_num)
#     label_categories_test = to_categorical(label_test, letter_num)
#     return (data_train, label_categories_train,
#             data_test, label_categories_test)

def prepare_data():
    train_x = np.load("train_x.txt.npy")
    train_y = np.load("train_y.txt.npy")
    test_x = np.load("test_x.txt.npy")
    test_y = np.load("test_y.txt.npy")

    return (train_x, train_y,
                test_x, test_y)







if __name__ == '__main__':
    x_train, y_train, x_test, y_test = prepare_data()
    print("shape of train_x" ,np.shape(x_train))
    print("shape of train_y" ,np.shape(y_train))
    print("shape of test_x" ,np.shape(x_test))
    print("shape of test_y" ,np.shape(y_test))
