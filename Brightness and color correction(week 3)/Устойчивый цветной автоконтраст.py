from skimage.io import imread, imsave, imshow
from skimage import img_as_float, img_as_ubyte
from numpy import clip, dstack, histogram

img = imread('img.png')
img_f = img_as_float(img)

r = img_f[:, :, 0]
g = img_f[:, :, 1]
b = img_f[:, :, 2]

y = 0.2126 * r +  0.7152*g + 0.0722* b
u = -0.0999 * r + -0.3360*g + 0.4360* b
v = 0.6150 * r + (-0.5586*g) + -0.0563* b

k = int(round(y.size * 0.05))
y_flat = sorted(y.flatten())
y_min = y_flat[k]
y_max = y_flat[-k]

y = (y - y_min) / (y_max - y_min)
y = clip(y,0,1)                 

r = y +  1.2803 * v
g = y + -0.2148 * u + -0.3805 * v
b = y +  2.1279 * u

img = dstack((r, g, b))
img = clip(img, 0, 1)

imsave('out_img.png', img)
