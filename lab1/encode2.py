def decode(y,Cb_coded,Cr_coded,n=2):
    
    
    Cb = y.copy()
    Cr = y.copy()
    
    for i in range(Cb_coded.shape[0]):
        for j in range(Cb_coded.shape[1]):
            for k1 in range(n):
                for k2 in range(n): 
                    try: Cb[i,j] = Cb_coded[i + k1,j + k2]; Cr[i,j] = Cr_coded[i + k1,j + k2]; 
                    except: pass 
    
    
    
    r = y + 1.402 * (Cr - 0.5)
    g = y - 0.34414 * (Cb - 0.5) - 0.71414 * (Cr - 0.5)
    b = y + 1.772 * (Cb - 0.5)   
    
    img = np.dstack((r,g,b))
    img = np.clip(img,0,1)
    img = img_as_ubyte(img)
    
    return img
