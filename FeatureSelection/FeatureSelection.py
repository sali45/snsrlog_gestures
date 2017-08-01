import os
from Preprocessing.Denoising import sample_difference
from Segmentation.segmentation import sliding_window
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
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


def principal_components():
    df = pd.DataFrame(columns=['timestamp', 'time skipped', 'x', 'y', 'z', 'label']).set_index('timestamp')
    for my_files in files:
        with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", my_files),
                  'rU') as my_file:
            df = df.append(sample_difference(my_file))
    pca = PCA(n_components=2)
    print df
    # result = pca.fit_transform(df[['x', 'y', 'z']])
    # plt.plot(result)
    # plt.show()
    # return result

principal_components()
