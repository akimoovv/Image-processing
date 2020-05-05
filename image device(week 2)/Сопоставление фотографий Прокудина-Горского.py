import numpy as np

def find(channel1, channel2):
    l, r = -15, -15
    max_corr = 0
        
    for i in range(-15,16):
        for j in range(-15,16):
            tmp = np.roll(channel2, j, axis=0)
            tmp = np.roll(tmp, i, axis=1)
            corr = (tmp * channel1).sum()
            if corr > max_corr:
                r = i
                l = j
                max_corr = corr
        
    return l, r

def cut_img(img, k):
    x, y = img.shape
    t_x, t_y = int(x * k), int(y * k)
    return img[t_x:x - t_x, t_y:y - t_y]


def align(img, g_coord):
    row_g, col_g = g_coord
    img = img_as_float(img)

    rows = img.shape[0] 
    n = rows // 3

    b_row = 0, n
    g_row = n, 2 * n
    r_row = 2 * n, 3 * n
        
    #Обрезаем изображения (10%)
    b = cut_img(img[b_row[0]:b_row[1]], 0.1)
    g = cut_img(img[g_row[0]:g_row[1]], 0.1)
    r = cut_img(img[r_row[0]:r_row[1]], 0.1)
   
    
    b_row_new, b_col_new = find(g, b) #запоминаем сдвиги вертикали с наибольщей похожестью
    r_row_new, r_col_new = find(g, r)
    
    
    row_b, col_b = row_g - n - b_row_new, col_g - b_col_new
    row_r, col_r = row_g + n - r_row_new, col_g - r_col_new
    return (row_b, col_b), (row_r, col_r)




