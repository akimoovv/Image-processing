def rgb_to_yuv(img): #Функция перевода из rgb в yuv
    img_f = img_as_float(img)
    res = img_f.copy()
    
    
    r = img_f[:,:,0]
    g = img_f[:,:,1]
    b = img_f[:,:,2]
    
    
    res[:,:,0] = 0.299 * r  + 0.587 * g  + 0.114 * b
    res[:,:,1] = 0 - 0.1687 * r - 0.3313 * g + 0.5 * b + 128
    res[:,:,2] = 0.5 * r - 0.4187 * g - 0.0813 * b + 128
    
    
    return res


def yuv_to_rgb(img): #Функция перевода из yuv в rgb
    img_f = img_as_float(img)
    res = img_f.copy()
    
    
    y = img_f[:,:,0]
    cb = img_f[:,:,1]
    cr = img_f[:,:,2]
    
    res[:,:,0] = y + 1.402 * (cr - 128)
    res[:,:,1] = y - 0.34414 * (cb - 128) - 0.71414 * (cr - 128)
    res[:,:,2] = y + 1.772 * (cb - 128)
    
    return res
