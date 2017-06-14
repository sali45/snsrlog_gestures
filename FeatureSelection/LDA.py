from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from Preprocessing import sample_difference as sd
import os
import matplotlib.pyplot as plt

files = [
    'PickUpPhoneAccelerometer1.csv',
    'PickUpPhoneAccelerometer2.csv',
    'Wave1Accelerometer.csv',
    'Wave2Accelerometer.csv',
    'PickUpPhoneAccelerometer3.csv',
    'Wave3Accelerometer.csv'
]


def linear_discrimination_analysis(files):
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", files[0]),
              'rU') as my_file_0:
        df1 = sd.sample_difference(my_file_0)
    for f in files[1:len(files) - 2]:
            with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", f),
                      'rU') as my_file_1:
                df1.append(sd.sample_difference(my_file_1))
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", files[len(files) - 2]),
                      'rU') as my_file_2:
        df2 = sd.sample_difference(my_file_2)
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", files[len(files) - 1]),
                      'rU') as my_file_3:
        df2.append(sd.sample_difference(my_file_3))
    X = df1.values[2:]
    y = df2.values[2:]
    lda = LDA(n_components=1)
    lda.fit_transform(X, y)
    plt.show()

linear_discrimination_analysis(files)
