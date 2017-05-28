import numpy as np
from sliding_window import window


def scaling(filename, col):
    data = np.loadtxt(filename, delimiter=',')
    acc_d = data.transpose()[col]
    acc_d_normed = (acc_d - acc_d.min(axis=0)) / acc_d.ptp(axis=0)
    return acc_d_normed

print "Acc_1_x: " + str(list(window(scaling('PickUpPhoneAccelerometer1.csv', 2), 5)))
print "Acc_1_y: " + str(list(window(scaling('PickUpPhoneAccelerometer1.csv', 3), 5)))
print "Acc_1_z: " + str(list(window(scaling('PickUpPhoneAccelerometer1.csv', 4), 5)))

print "Acc_2_x: " + str(list(window(scaling('PickUpPhoneAccelerometer2.csv', 2), 5)))
print "Acc_2_y: " + str(list(window(scaling('PickUpPhoneAccelerometer2.csv', 3), 5)))
print "Acc_2_z: " + str(list(window(scaling('PickUpPhoneAccelerometer2.csv', 4), 5)))

print "Acc_3_x: " + str(list(window(scaling('PickUpPhoneAccelerometer3.csv', 2), 5)))
print "Acc_3_y: " + str(list(window(scaling('PickUpPhoneAccelerometer3.csv', 3), 5)))
print "Acc_3_z: " + str(list(window(scaling('PickUpPhoneAccelerometer3.csv', 4), 5)))
