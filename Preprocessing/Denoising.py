import pandas as pd
import matplotlib.pyplot as plt
import os


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


def sample_difference(filename):
    df = pd.read_csv(filename, header=None, names=['timestamp', 'time skipped', 'x', 'y', 'z', 'label'], skipinitialspace=True)
    df.timestamp = pd.to_datetime(df.timestamp)  # Convert column type to be datetime
    df = df.set_index(['timestamp'])
    df.assign(dx=df.x.diff(), dy=df.y.diff(), dz=df.z.diff())
    # plt.plot(df['x'])
    # plt.plot(df['y'])
    # plt.plot(df['z'])
    # plt.show()
    return df

for my_files in files:
    with open(os.path.join("/Users", "saqibali", "PycharmProjects", "sensorLogProject", "Data", my_files),
              'rU') as my_file:
        sample_difference(my_file)
