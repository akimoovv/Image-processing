from skimage.io import imread, imsave, imshow
from numpy import histogram, clip

#img = imread('https://stepik.org/media/attachments/lesson/58402/tiger-low-contrast.png') 
img = imread('img.png') 
h, bin_edges = histogram(img, bins=range(257)) 
k = round(img.size * 0.05) # Отбрасываем 5% пикселей
count = 0

for i in range(256): # Бежим по гистограмме и ищем минимум гистограммы
    count += h[i]
    if count > k:
        x_min = i
        count = 0
        break
for i in range(255,0,-1): # Бежим по гистограмме и ищем максимум гистограммы
    count += h[i]
    if count > k:
        x_max = i
        break
res = img
res = clip(res, x_min, x_max) 
res = (res - x_min) * (255 / (x_max - x_min)) 
imsave('out_img.png', res.astype('uint8'))
