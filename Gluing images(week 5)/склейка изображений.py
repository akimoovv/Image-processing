import math
from skimage.io import imread, imsave,imshow
import numpy as np
from skimage import img_as_float, img_as_ubyte
def gluing(img1,img2,mask,sigma): # Функция, которая на выходе должна давать склеенные изображения
    def gaus_func(img): #Функция, применяющая гауссовское ядро к изображению, аналогична с функцией из предыдущего отчета
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
            res = np.ndarray(shape=(x, y), dtype=int)
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    res[i, j] = int((img[i:i + K, j:j + K] * array).sum())
            return np.clip(res, 0, 255)
    
    
        array = np.array(f(sigma))
        img = gauss_filter(img,array)
        return img

    def timesA(a,b): # Функция, перемножающая попиксельно изображений LA и GM
        x = min(a.shape[0],b.shape[0])
        y = min(a.shape[1],b.shape[1])
        res = np.ndarray(shape=(x, y), dtype=int)
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                res[i,j] = a[i,j] * b[i,j]
        return res

    def timesB(a,b): # Функция, перемножающая попиксельно изображений LA и GM
        x = min(a.shape[0],b.shape[0])
        y = min(a.shape[1],b.shape[1])
        res = np.ndarray(shape=(x, y), dtype=int)
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                res[i,j] = a[i,j] * (1 - b[i,j])
        return res


    def sub(A,B): # Функция, вычитающая попикельно изображения
        x = min(A.shape[0],B.shape[0])
        y = min(A.shape[1],B.shape[1])
        res = np.ndarray(shape=(x, y), dtype=int)
        for i in range(x):
            for j in range(y):
                res[i,j] = A[i,j]- B[i,j]
        return res

    def add(A,B,C,D): # Функция, суммирующая попикельно 4 изображения
        x = min(A.shape[0],B.shape[0],C.shape[0],D.shape[0])
        y = min(A.shape[1],B.shape[1],C.shape[1],D.shape[1])
        res = np.ndarray(shape=(x, y), dtype=int)
        for i in range(x):
            for j in range(y):
                res[i,j] = A[i,j] + B[i,j] + C[i,j] + D[i,j]
        return res

    def add2(A,B): # Функция, суммирующая попикельно 2 изображения
        x = min(A.shape[0],B.shape[0])
        y = min(A.shape[1],B.shape[1])
        res = np.ndarray(shape=(x, y), dtype=int)
        for i in range(x):
            for j in range(y):
                res[i,j] = A[i,j] + B[i,j]
        return res
    

    
    
    #Строим гауссовскую пирамиду для изображения  A
    A = gaus_func(img1)
    A1 = gaus_func(A)
    A2 = gaus_func(A1)
    A3 = gaus_func(A2)

    #Строим лапласовскую пирамиду для изображения  A
    LA1 = sub(A,A1)
    LA2 = sub(A1,A2)
    LA3 = sub(A2,A3)
    LA4 = A3


    #Строим гауссовскую пирамиду для изображения  B
    B = gaus_func(img2)
    B1 = gaus_func(B)
    B2 = gaus_func(B1)
    B3 = gaus_func(B2)

    #Строим лапласовскую пирамиду для изображения  B
    LB1 = sub(B,B1)
    LB2 = sub(B1,B2)
    LB3 = sub(B2,B3)
    LB4 = B3
        
    #Строим гауссовскую пирамиду для маски
    GM1 = mask
    GM2 = gaus_func(GM1)
    GM3 = gaus_func(GM2)
    GM4 = gaus_func(GM3)

    #Умножаем и складываем каждые части лапласовской пирамиды
    res1 = add2(timesA(LA4,GM4),timesB(LB4,GM4))
    res2 = add2(timesA(LA3,GM3),timesB(LB3,GM3))
    res3 = add2(timesA(LA2,GM2),timesB(LB2,GM2))
    res4 = add2(timesA(LA1,GM1),timesB(LB1,GM1))
    
    #Складываем все полученные суммы
    res = add(res1,res2,res3,res4)
    res =  np.clip(res,0,254)
    return res
  
  
  
#Считываем изображения
img1 = imread('A2.png')
img2 = imread('B2.png')

# Создаем маску
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
        
        
        
#Обрабатываем отдельно каждый канал изображений
a1 = img1[:,:,0]
a2 = img1[:,:,1]
a3 = img1[:,:,2]

b1 = img2[:,:,0]
b2 = img2[:,:,1]
b3 = img2[:,:,2]

m1 = mask[:,:,0]
m2 = mask[:,:,1]
m3 = mask[:,:,2]

k1 = gluing(a1,b1,m1,0.77)
k2 = gluing(a2,b2,m2,0.77)
k3 = gluing(a3,b3,m3,0.77)

#Объединяем каналы изображений
res = np.dstack((k1, k2, k3))

