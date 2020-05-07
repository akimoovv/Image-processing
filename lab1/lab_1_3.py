from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import histogram
import numpy as np





def entropy(img):
    h, _ = histogram(img, bins=range(257))
    H = 0
    probabilitys = (h * 1.0) / img.size
    for p in probabilitys:
        if p > 0:
            H += (-p * np.log2(p))
    return H
    
    
    
    
def mse(img1,img2):
    h1, _ = np.histogram(img1, bins = range(257))
    h2, _ = np.histogram(img2, bins = range(257))
    P = (h1*1.0)/img1.size
    Q = (h2*1.0)/img2.size
    MSE = (((P - Q) **2).sum()) / len(P)
    return MSE
