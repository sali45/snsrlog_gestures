from sklearn.decomposition import PCA
from Preprocessing import sample_difference as sd
from Segmentation import segmentation as seg
import os
import pandas as pd
import matplotlib.pyplot as plt

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'Wave3Accelerometer.csv'
]


def principal_component_analysis(filename):
    df = sd.sample_difference(filename)
    array = df.values
    pca = PCA(n_components=3)
    fit = pca.fit_transform(array)
    plt.plot(fit)
    plt.show()

for f in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", f), 'rU') as my_file:
        principal_component_analysis(my_file)
