# Will attempt to train classifiers here.

import numpy as np

import math as m
import cv2

img = cv2.imread('exercise-2.jpg')
print img.shape
height, width, ch = img.shape


def rgb2IRgBy(img):
    b, g, r = cv2.split(img)
    height, width, ch = img.shape

    r_zero_resp = np.amin(r[10:height - 10, 10: width - 10])
    g_zero_resp = np.amin(g[10:height - 10, 10: width - 10])
    b_zero_resp = np.amin(b[10:height - 10, 10: width - 10])
    true_zero = np.amin([r_zero_resp, g_zero_resp, b_zero_resp])

    r -= true_zero
    g -= true_zero
    b -= true_zero
    lr = np.zeros((height, width))
    lb = np.zeros((height, width))
    lg = np.zeros((height, width))

    for rows in range(height):
        for cols in range(width):

            lr[rows, cols] = 105*m.log10(r[rows, cols] + 1)
            lb[rows, cols] = 105*m.log10(b[rows, cols] + 1)
            lg[rows, cols] = 105*m.log10(g[rows, cols] + 1)


    I = (lr + lb + lg) / 3
    Rg = lr - lg
    By = lb - ((lg + lr) / 2)
    scale = round(width + height / 320)
    integer_scale = int(scale)

    print Rg.shape

    if scale == 0:
        scale = 1


    Rg = cv2.medianBlur(Rg, 4 * integer_scale-1)
    By = cv2.medianBlur(By, 4 * integer_scale-1)
    I_filt = cv2.medianBlur(I, 8 * integer_scale-1)
    MAD = I - I_filt
    MAD = abs(MAD)
    MAD = cv2.medianBlur(MAD, 12 * integer_scale-1)


    hue = (np.arctan2(Rg, By) * (180/m.pi))
    saturation = np.sqrt(np.power(Rg, 2) + np.power(By, 2))


    map = np.zeros((height, width))

    for rows in range(height):
        for cols in range(width):
            if (MAD[rows, cols] < 4.5) & (120 < hue[rows, cols]) & (hue[rows, cols] < 160) & (10 < saturation[rows, cols]) & (saturation[rows, cols] < 60):
                map[rows, cols] = 1
            if (MAD[rows, cols] < 4.5) & (150 < hue[rows, cols]) & (hue[rows, cols] < 180) & (saturation[rows, cols] > 20) & (saturation[rows, cols] < 80):
                map[rows, cols] = 1


    kernal = np.ones((10 * integer_scale, 10 * integer_scale),np.uint8)
    map = cv2.dilate(map, kernal, iterations=5)

    print map.shape

    cv2.imshow('img', img)
    temp = img
    for rows in range(height):
        for cols in range(width):
            if map[rows, cols] == 0:
                temp[rows, cols] = [0, 0, 0]


    ugly = cv2.merge((By, Rg, I))

    cv2.imshow('ugly', ugly)


    print 'waiting on you'
    cv2.waitKey(0)
    cv2.destroyAllWindows()


rgb2IRgBy(img)


