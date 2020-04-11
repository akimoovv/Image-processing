import math
from skimage.io import imread, imsave
import numpy as np

def gaus(sigma,x,y):
    return (1/(2*math.pi*(sigma**2)))*math.exp((-x**2-y**2)/(2*(sigma**2)))

def f(sigma):
    K = int(round(6 * sigma)+1)
    Sum = 0
    K_array = [[0]* K for _ in range(K)]
    
    for i in range(K):
        for j in range(K):
            x = j - K//2
            y = (-i) + K//2
            K_array[i][j] = gaus(sigma, x, y)
            Sum += K_array[i][j] 
    for i in range(K):
        for j in range(K):
            x = K_array[i][j]/Sum
            K_array[i][j] = x
    return K_array

def gauss_filter(img, array):
    K = array.shape[0]
    x = img.shape[0] - K + 1
    y = img.shape[1] - K + 1
    res = np.ndarray(shape=(x, y), dtype=int)
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i, j] = int((img[i:i + K, j:j + K] * array).sum())
    return np.clip(res, 0, 255)

img = imread('img.png')
array = np.array(f(0.66))
res = gauss_filter(img,array)
imsave('out_img.png', res)




