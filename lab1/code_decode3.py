def code(img, n=2): # Работает правильно
    img_f = img_as_float(img)
    
    r = img_f[:,:,0]
    g = img_f[:,:,1]
    b = img_f[:,:,2]
    
    y = 0.299 * r  + 0.587 * g  + 0.114 * b
    u = u2 = 0 - 0.1687 * r - 0.3313 * g + 0.5 * b + 0.5
    v = v2 = 0.5 * r - 0.4187 * g - 0.0813 * b + 0.5
    
    Cb = np.zeros((y.shape[0]//2, y.shape[1]//2) , dtype = 'float64')
    Cr = np.zeros((y.shape[0]//2, y.shape[1]//2), dtype = 'float64')
    
    #Итерируемся по изображению и каждый пиксель "квадрата" размера n^2 делаем равным левому верхнему элементу квадрата
    #То есть делаем децимацию
    i1 = j1 = -1
    for i in range(0,u.shape[0],n):
        i1 += 1
        for j in range(0,u.shape[1],n):
            j1 += 1
            try: Cb[i1,j1] = u[i,j]; Cr[i1,j1] = v[i,j]
            except: pass
        j1 = -1       
    
    return y,Cb,Cr
    
def decode(y,Cb_input,Cr_input,n=2):
    
    
    Cr = np.zeros(y.shape[0:2], dtype = 'float64')
    Cb = np.zeros(y.shape[0:2], dtype = 'float64')
    
    i1 = j1 = -1
    for i in range(0,y.shape[0],n):
        i1 += 1
        for j in range(0,y.shape[0],n):
            j1 += 1
            for k1 in range(n):
                for k2 in range(n): 
                    try: Cb[i + k1,j + k2] = Cb_input[i1,j1]; Cr[i + k1,j + k2] = Cr_input[i1,j1]; 
                    except: pass 
    
        j1 = -1
    
    r = y + 1.402 * (Cr - 0.5)
    g = y - 0.34414 * (Cb - 0.5) - 0.71414 * (Cr - 0.5)
    b = y + 1.772 * (Cb - 0.5)   
    
    img = np.dstack((r,g,b))
    img = np.clip(img,0,1)
    img = img_as_ubyte(img)
    
    return img
