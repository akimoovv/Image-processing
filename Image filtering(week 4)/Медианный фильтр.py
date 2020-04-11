import math
from skimage.io import imread, imsave, imshow
from numpy import ndarray, clip
img = imread('img.png')
res = ndarray(shape=(img.shape[0] - 6, img.shape[1] - 6), dtype=int)
for i in range(res.shape[0]):
    for j in range(res.shape[1]):
        flatten_array_sorted = sorted((img[i:i + 7, j:j + 7]).flatten())
        res[i,j] = flatten_array_sorted[24]
imsave('out_img.png' , res)
