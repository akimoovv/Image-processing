import math
from skimage.io import imread, imsave,imshow
import numpy as np
from skimage import img_as_float, img_as_ubyte
def gluing(img1,img2,mask):
    def gaus_func(img):
        def gaus(sigma,x,y):
            return (1/(2*math.pi*(sigma**2)))*math.exp((-x**2-y**2)/(2*(sigma**2)))

        def f(sigma):
            K = int(round(6 * sigma)+1)
            Sum = 0
            K_array = [[0]* K for _ in range(K)]
        
            for i in range(K):
                for j in range(K):
                    x = j - K//2
                    y = (-i) + K//2
                    K_array[i][j] = gaus(sigma, x, y)
                    Sum += K_array[i][j] 
            for i in range(K):
                for j in range(K):
                    x = K_array[i][j]/Sum
                    K_array[i][j] = x
            return K_array

        def gauss_filter(img, array):
            K = array.shape[0]
            x = img.shape[0] - K + 1
            y = img.shape[1] - K + 1
            res = img.copy()
            for i in range(x):
                for j in range(y):
                    res[i, j] = int((img[i:i + K, j:j + K] * array).sum())
            return np.clip(res, 0, 255)
    
    
        array = np.array(f(0.66))
        img = gauss_filter(img,array)
        return img

    def timesA(a,b):
        res = a.copy()
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                res[i,j] = a[i,j] * b[i,j]
        return res

    def timesB(a,b):
        res = a.copy()
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                res[i,j] = a[i,j] * (1 - b[i,j])
        return res


    def sub(A,B):
        x = A.shape[0] 
        y = A.shape[1] 
        res = A.copy()
        for i in range(x):
            for j in range(y):
                res[i,j] = A[i,j]- B[i,j]
        return res

    def add(A,B,C,D):
        x = A.shape[0] 
        y = A.shape[1] 
        res = A.copy()
        for i in range(x):
            for j in range(y):
                res[i,j] = A[i,j] + B[i,j] + C[i,j] + D[i,j]
        return res

    def add2(A,B):
        x = A.shape[0] 
        y = A.shape[1] 
        res = A.copy()
        for i in range(x):
            for j in range(y):
                res[i,j] = A[i,j] + B[i,j]
        return res
    

    
    
    
    A = gaus_func(img1)
    A1 = gaus_func(A)
    A2 = gaus_func(A1)
    A3 = gaus_func(A2)


    LA1 = sub(A,A1)
    LA2 = sub(A1,A2)
    LA3 = sub(A2,A3)
    LA4 = A3



    B = gaus_func(img2)
    B1 = gaus_func(B)
    B2 = gaus_func(B1)
    B3 = gaus_func(B2)


    LB1 = sub(B,B1)
    LB2 = sub(B1,B2)
    LB3 = sub(B2,B3)
    LB4 = B3
        
    GM1 = mask
    GM2 = gaus_func(GM1)
    GM3 = gaus_func(GM2)
    GM4 = gaus_func(GM3)


    res1 = add2(timesA(LA4,GM4),timesB(LB4,GM4))
    res2 = add2(timesA(LA3,GM3),timesB(LB3,GM3))
    res3 = add2(timesA(LA2,GM2),timesB(LB2,GM2))
    res4 = add2(timesA(LA1,GM1),timesB(LB1,GM1))

    res = add(res1,res2,res3,res4)
    res =  np.clip(res,0,254)
    return res
    
    
img1 = imread('A2.png')
img2 = imread('B2.png')
mask = img1.copy()
    
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]//2):
        mask[i,j][0] = 1
        mask[i,j][1] = 1
        mask[i,j][2] = 1
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]//2,mask.shape[1]):
        mask[i,j][0] = 0
        mask[i,j][1] = 0
        mask[i,j][2] = 0
   
   
   
a1 = img1[:,:,0]
a2 = img1[:,:,1]
a3 = img1[:,:,2]

b1 = img2[:,:,0]
b2 = img2[:,:,1]
b3 = img2[:,:,2]

m1 = mask[:,:,0]
m2 = mask[:,:,1]
m3 = mask[:,:,2]


k1 = gluing(a1,b1,m1)
k2 = gluing(a2,b2,m2)
k3 = gluing(a3,b3,m3)

res = np.dstack((k1, k2, k3))

imshow(res)
