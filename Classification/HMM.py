from hmmlearn import hmm
import matplotlib.pyplot as plt
from FeatureSelection.FeatureSelection import principal_components
from Segmentation.segmentation import sliding_window
from Preprocessing.Denoising import sample_difference
import os

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'Wave3Accelerometer.csv'
]


def HMM(data):
    model = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)
    model.fit(data)
    Z = model.predict(data)
    print Z
    return Z

for my_files in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", my_files),
              'rU') as my_file:
        HMM(principal_components(sliding_window(sample_difference(my_file), 100, 50)))

