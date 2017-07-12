import os
from Preprocessing.Denoising import sample_difference
import numpy as np
import matplotlib.pyplot as plt

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'PickUpPhoneAccelerometer3.csv',
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
    # plt.plot(mag)
    # plt.plot(indicator * 1000, 'r')
    # plt.show()
    # indicator *= 1000
    # m = indicator != 0
    # out = np.split(indicator, np.flatnonzero(m[1:] != m[:-1]) + 1)
    return indicator

for my_files in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", my_files),
              'rU') as my_file:
        segment_energy(sample_difference(my_file), 2)

