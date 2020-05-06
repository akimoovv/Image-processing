def code(img, n=2): # Работает правильно
    img_f = img_as_float(img)
    
    r = img_f[:,:,0]
    g = img_f[:,:,1]
    b = img_f[:,:,2]
    
    y = 0.299 * r  + 0.587 * g  + 0.114 * b
    u = u2 = 0 - 0.1687 * r - 0.3313 * g + 0.5 * b + 0.5
    v = v2 = 0.5 * r - 0.4187 * g - 0.0813 * b + 0.5
    #Итерируемся по изображению и каждый пиксель "квадрата" размера n^2 делаем равным левому верхнему элементу квадрата
    #То есть делаем децимацию
    for i in range(0,u.shape[0],n):
        for j in range(0,u.shape[1],n):
            for k1 in range(n):
                for k2 in range(n): 
                    try: u[i + k1,j + k2] = u2[i,j]; v[i + k1,j + k2] = v2[i,j]; 
                    except: pass 
                    
                    
    y = y
    Cb = u
    Cr = v  
    
    return y,Cb,Cr
