from skimage.io import imread,imsave
from skimage import img_as_float, img_as_ubyte
import numpy 
from numpy import histogram
img = imread('img.png')
values, bin_edges = histogram(img, bins=range(257))
h = values
cdf = [h[0]]
for i in range(1,len(h)):
    cdf.append(h[i] + cdf[i-1])
minCdf = 10**9
for values in cdf:
    if values != 0:  
        minCdf = min(minCdf,values)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x = img[i][j]
        img[i][j] = round(((cdf[x] - minCdf) / (img.size - 1)) * 255 )
imsave('out_img.png', img)
