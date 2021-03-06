import os
from Preprocessing.Denoising import sample_difference
from Segmentation.segmentation import sliding_window
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import pandas as pd
import warnings


training_files = [
    'Circle1Accelerometer.csv',
    'PickUpPhoneAccelerometer1.csv',
    'Wave1Accelerometer.csv',
]

test_files = [
    'Circle3Accelerometer.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave3Accelerometer.csv'
]


def ecdf_representation(D, n):
    """calculate ECDF from D at n points"""
    m = np.mean(D)
    X = []
    for d in xrange(D.shape[1] + 1):
        func = ECDF(([D[:, d] + np.random.randn(np.shape(D[:, d])) * 0.01]))
        ll = func(np.linspace(0, 1, n))
        X = [X, ll]
    X = [X, m]
    plt.plot(X)
    plt.show()
    return X


def windows(files):
    x = []
    for my_files in files:
        df = pd.DataFrame(columns=['timestamp', 'time skipped', 'x', 'y', 'z', 'label']).set_index('timestamp')
        with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", my_files), 'rU')\
                as my_file:
            for d in sliding_window(sample_difference(my_file), 500, 250):
                df = df.append(d)
        x.append(df[['x', 'y', 'z']].values)
    return np.array(x)


def principal_components():
    pca = PCA(n_components=2)
    training_result = []
    for window in windows(training_files):
        training_result.append(pca.fit_transform(window))
    testing_result = []
    for window in windows(test_files):
        testing_result.append(pca.transform(window))
    return np.array(training_result), np.array(testing_result)

warnings.filterwarnings("ignore")
principal_components()