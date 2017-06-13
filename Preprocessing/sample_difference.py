import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'Wave3Accelerometer.csv'
]


def sample_difference(filename):
    df = pd.read_csv(filename, header=None, names=['timestamp', 'time skipped', 'x', 'y', 'z', 'label']).set_index('timestamp')
    df.assign(dx=df.x.diff(), dy=df.y.diff(), dz=df.z.diff())
    array = df.values
    pca = PCA(n_components=3)
    fit = pca.fit_transform(array)
    plt.plot(fit)
    plt.show()
    return df

for f in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", f), 'rU') as my_file:
        sample_difference(my_file)
