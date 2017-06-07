import numpy as np
import pandas as pd
from sklearn import preprocessing
from segmentation import segment_energy

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'Wave3Accelerometer.csv'
]


def scaling(filename, col):
    data = np.loadtxt(filename, delimiter=',')
    acc_d = data.transpose()[col]
    acc_d_normed = preprocessing.scale(acc_d)
    return acc_d_normed


def acc_data(filename):
    data = [[], [], []]
    # 2nd column has Acc_x data, 3rd has Acc_y data, 4th has Acc_z data
    for i in range(2, 5):
        data[i - 2].append(scaling(filename, i))
    return data


def label(filename):
    # Column 5 has the label value.
    data = np.array(pd.read_csv(filename, usecols=[5]))
    return data[0]

for f in files:
    print label(f)
    print acc_data(f)
    print "\n"
    segment_energy(acc_data(f), 2)
