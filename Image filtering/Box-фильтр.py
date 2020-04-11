from skimage.io import imread, imsave
import numpy as np
img = imread('img.png')
x = img.shape[0] - 4
y = img.shape[1] - 4
res = np.ndarray(shape=(x, y), dtype=int)
for i in range (res.shape[0]):
    for j in range(res.shape[1]): 
        res[i,j] = (img[i:i+5,j:j+5]).sum()/25
imsave('out_img.png', res.astype('uint8'))
