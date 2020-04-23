img1 = imread('a.png')
img2 = imread('b.png')
mask = imread('mask.png')

#Подготавливаем маску
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        for y in range(3):
            if mask[i,j,y] >= 128:
                mask[i,j,y] = 1
            else:
                mask[i,j,y] = 0

a1 = img1[:,:,0]
a2 = img1[:,:,1]
a3 = img1[:,:,2]

b1 = img2[:,:,0]
b2 = img2[:,:,1]
b3 = img2[:,:,2]

m1 = mask[:,:,0]
m2 = mask[:,:,1]
m3 = mask[:,:,2]

k1 = gluing(a1,b1,m1,1.2)
k2 = gluing(a2,b2,m2,1.2)
k3 = gluing(a3,b3,m3,1.2)

res = np.dstack((k1, k2, k3))
imshow(res.astype('uint8'))
