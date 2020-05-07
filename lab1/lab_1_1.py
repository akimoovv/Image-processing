from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte, img_as_uint
import numpy as np


img = imread('img.png')
img_greyscale = img[:,:,0]



def encode(img,n):
    return (img/n).astype('uint8')
    
    
def decode(img,n):  
    return np.clip(img * n, 0, 255)
    
    
img_greyscale_encode = encode(img_greyscale,16)
img_greyscale_decode = decode(img_greyscale_encode,16)


imshow(img)
imshow(img_greyscale_encode)
imshow(img_greyscale_decode)



imsave('img_greyscale_encode.png',img_greyscale_encode)
