from skimage.io import imread, imsave
img = imread('img.png')
img = ((img - img.min()) * (255 / (img.max() - img.min())))
imsave('out_img.png', img.astype('uint8'))
