import os
from Preprocessing.Denoising import sample_difference
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.stride_tricks import as_strided as ast
import pandas as pd


files = [
    'Circle1Accelerometer.csv',
    'Circle2Accelerometer.csv',
    'Circle3Accelerometer.csv',
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'Wave3Accelerometer.csv'
]


def segment_energy(data, th):
    mag = np.linalg.norm(data.loc[:, ['x', 'y', 'z']], axis=1)
    mag = np.array(mag)
    mag -= np.mean(mag)

    above = np.where(mag >= th * np.std(mag))
    indicator = np.zeros(mag.shape)
    indicator[above] = 1
    print indicator
    plt.plot(mag)
    plt.plot(indicator * 1000, 'r')
    plt.show()
    indicator *= 1000
    m = indicator != 0
    out = np.split(indicator, np.flatnonzero(m[1:] != m[:-1]) + 1)
    return out


def sliding_window(arr, ws, ss):
    r = np.arange(len(arr))
    s = r[::ss]
    z = list(zip(s, s + ws))
    f = '{0[0]}:{0[1]}'.format
    g = lambda t: arr.iloc[t[0]:t[1]]
    return map(g, z)


def window(a, w=4, o=2, copy=False):
    sh = (a.size - w + 1, w)
    st = a.strides * 2
    view = np.lib.stride_tricks.as_strided(a, strides=st, shape=sh)[0::o]
    if copy:
        return view.copy()
    else:
        return view

for f in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", f),
              'rU') as my_file:
        sliding_window(sample_difference(my_file), 50, 25)

