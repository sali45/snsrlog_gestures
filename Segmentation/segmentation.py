import numpy as np
import matplotlib.pyplot as plt
import os
from Preprocessing import sample_difference as sd

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'Wave3Accelerometer.csv'
]


def segment_energy(data, th):
    mag = np.array([np.linalg.norm(data['x']), np.linalg.norm(data['y']), np.linalg.norm(data['z'])])
    print "This is the mag: " + str(mag)
    mag -= np.mean(mag)

    above = np.where(mag >= th*np.std(mag))
    indicator = np.zeros(mag.shape)
    indicator[above] = 1
    # plt.plot(mag)
    # plt.plot(indicator * 1000, 'r')
    # plt.show()

for f in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", f), 'rU') as my_file:
        segment_energy(sd.sample_difference(my_file), 2)
