import math
from skimage.io import imread, imsave,imshow
import numpy as np

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
                s = 0
                for i1 in range(i,i+K):
                    for j1 in range(j,j + K):
                        s = s + (img[i1,j1][0] * array[i1 - i,j1 - j])
                s = int(s)
                res[i,j][0] = s
            
            
            
                s = 0
                for i1 in range(i,i+K):
                    for j1 in range(j,j + K):
                        s = s + (img[i1,j1][1] * array[i1 - i,j1 - j])
                s = int(s)
                res[i,j][1] = s
            
            
            
                s = 0
                for i1 in range(i,i+K):
                    for j1 in range(j,j + K):
                        s = s + (img[i1,j1][2] * array[i1 - i,j1 - j])
                s = int(s)
                res[i,j][2] = s
            
        return np.clip(res, 0, 255)
    
    
    array = np.array(f(0.66))
    img = gauss_filter(img,array)
    return img
   
def sub(A,B):
    x = A.shape[0] 
    y = A.shape[1] 
    res = A.copy()
    for i in range(x):
        for j in range(y):
            res[i,j][0] = A[i,j][0] - B[i,j][0]
            res[i,j][1] = A[i,j][1] - B[i,j][1]
            res[i,j][2] = A[i,j][2] - B[i,j][2]
    return res

def add(A,B,C,D):
    x = A.shape[0] 
    y = A.shape[1] 
    res = A.copy()
    for i in range(x):
        for j in range(y):
            res[i,j][0] = A[i,j][0] + B[i,j][0] + C[i,j][0] + D[i,j][0]
            res[i,j][1] = A[i,j][1] + B[i,j][1] + C[i,j][1] + D[i,j][1]
            res[i,j][2] = A[i,j][2] + B[i,j][2] + C[i,j][2] + D[i,j][2]
    return res
img = imread('A2.png')

A = gaus_func(img)
A1 = gaus_func(A)
A2 = gaus_func(A1)
A3 = gaus_func(A2)


LA1 = sub(A,A1)
LA2 = sub(A1,A2)
LA3 = sub(A2,A3)
LA4 = A3

res = add(LA1,LA2,LA3,LA4)
res = np.clip(res,0,255)
