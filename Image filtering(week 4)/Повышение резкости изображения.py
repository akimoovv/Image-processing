import math
from skimage.io import imread, imsave, imshow
import numpy as np


def f(img, array):
    K = array.shape[0]
    x = img.shape[0] - K + 1
    y = img.shape[1] - K + 1
    res = np.ndarray(shape=(x, y), dtype=int)
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i, j] = int((img[i:i + K, j:j + K] * array).sum())
    return np.clip(res, 0, 255)


img = imread('img.png')
array = 0.1 * np.array([[-1,-2,-1],[-2,22,-2],[-1,-2,-1]])
res = f(img,array)
imsave('out_img.png', res)




