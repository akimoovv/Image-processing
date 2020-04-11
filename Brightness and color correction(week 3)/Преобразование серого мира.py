from skimage.io import imread,imsave
from skimage import img_as_float, img_as_ubyte
import numpy as np
img = imread('img.png')

def find_mid(y): # Функция нахождения среднего значения
    yf = y.flatten()
    y_mid = sorted(yf)[len(yf)//2]
    return y_mid



img_f = img_as_float(img)

r = img_f[:, :, 0] 
g = img_f[:, :, 1]
b = img_f[:, :, 2]

r_mid = np.mean(r)
g_mid = np.mean(g)
b_mid = np.mean(b)

avrg =(r_mid + g_mid + b_mid)/3
rw = r_mid / avrg
gw = g_mid / avrg
bw = b_mid / avrg

r = r / rw
b = b / bw
g = g / gw

img_f[:,:,0] = r
img_f[:,:,1] = g
img_f[:,:,2] = b

img_f = np.clip(img_f, 0, 1)
res = img_as_ubyte(img_f)
imsave('out_img.png', res)
