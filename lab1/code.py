def code(img, n):
    img_yuv = rgb_to_yuv(img) # преобразовываем изображение в yuv
    
    res = img_yuv.copy()
    #Итерируемся по изображению и каждый пиксель "квадрата" размера n^2 делаем равным левому верхнему элементу квадрата
    #То есть делаем децимацию
    for i in range(0,res.shape[0],n):
        for j in range(0,res.shape[1],n):
            for k1 in range(n):
                for k2 in range(n): 
                    try: res[i + k1,j + k2, 1] = img_yuv[i,j,1]; res[i + k1,j + k2, 2] = img_yuv[i,j,2]; 
                    except: pass 
                    
                    
    y = res[:,:,0]
    cb = res[:,:,1]
    cr = res[:,:,2]    
    
    
    return y,cb,cr 
