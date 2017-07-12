import os
from Preprocessing.Denoising import sample_difference
from Segmentation.segmentation import segment_energy
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave3Accelerometer.csv'
]


def ecdf_representation(D, n):
    """calculate ECDF from D at n points"""
    m = np.mean(D)
    X = []
    print D
    for d in xrange(D.shape[1] + 1):
        func = ECDF(([D[:, d] + np.random.randn(np.shape(D[:, d])) * 0.01]))
        ll = func(np.linspace(0, 1, n))
        X = [X, ll]
    X = [X, m]
    plt.plot(X)
    plt.show()
    return X


def lda():
    return LDA(n_components=1)

for my_files in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", my_files),
              'rU') as my_file:
        ecdf_representation(segment_energy(sample_difference(my_file), 2), 13)