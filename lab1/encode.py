def decode(y,Cb_coded,Cr_coded):
    
    
    Cb = np.zeros(y.shape[0:2], dtype = 'float64')
    Cr = np.zeros(y.shape[0:2], dtype = 'float64')
    
    for i in range(Cb_coded.shape[0]):
        slice_i = slice(i * 2, i * 2 + 2)
        
        for j in range(Cb_coded.shape[1]):
            slice_j = slice(i * 2, i * 2 + 2)
            
            Cb[slice_i,slice_j] = Cb_coded[i,j]
            Cr[slice_i,slice_j] = Cr_coded[i,j]
    
    
    
    r = y + 1.402 * (Cr - 0.5)
    g = y - 0.34414 * (Cb - 0.5) - 0.71414 * (Cr - 0.5)
    b = y + 1.772 * (Cb - 0.5)  
    
    
    img = np.dstack((y,Cb,Cr))
    img = np.clip(img,0,1)
    img = img_as_ubyte(img)
    
    return img
