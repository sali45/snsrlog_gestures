import numpy as np
import matplotlib.pyplot as plt


def segment_energy(data, th):
    mag = np.array([np.linalg.norm(data[0]), np.linalg.norm(data[1]), np.linalg.norm(data[2])])
    mag -= np.mean(mag)

    above = np.where(mag >= th*np.std(mag))
    indicator = np.zeros(mag.shape)
    indicator[above] = 1
    plt.plot(mag)
    plt.plot(indicator * 1000, 'r')
    plt.show()
