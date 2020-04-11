import numpy

def align(image, green_point):
    row_g, col_g = green_point
    img = img_as_float(image)
    rows, _ = img.shape
    delta = rows // 3

    # sizes of parts
    b_rows = 0, delta
    g_rows = delta, 2 * delta
    r_rows = 2 * delta, 3 * delta
    
    def cut_percents(img, percents: float):
        rows, columns = img.shape
        t_rows, t_columns = int(rows * percents), int(columns * percents)
        return img[t_rows:rows - t_rows, t_columns:columns - t_columns]
    
    percents = 0.1
    r = cut_percents(img[r_rows[0]:r_rows[1]], percents)
    g = cut_percents(img[g_rows[0]:g_rows[1]], percents)
    b = cut_percents(img[b_rows[0]:b_rows[1]], percents)
    
    def find_best_shift(fixed_channel, movable_channel):
        best_row_shift, best_col_shift = -15, -15
        best_corr = 0
        roll_range = range(-15, 16)
        
        for col_shift in roll_range:
            for row_shift in roll_range:
                tmp = numpy.roll(movable_channel, row_shift, axis=0)
                tmp = numpy.roll(tmp, col_shift, axis=1)
                correlation = (tmp * fixed_channel).sum()
                if correlation > best_corr:
                    best_col_shift = col_shift
                    best_row_shift = row_shift
                    best_corr = correlation
        
        return best_row_shift, best_col_shift

    roll_b_row, roll_b_col = find_best_shift(g, movable_channel=b)
    roll_r_row, roll_r_col = find_best_shift(g, movable_channel=r)
    
    blue = row_g - delta - roll_b_row, col_g - roll_b_col
    red = row_g + delta - roll_r_row, col_g - roll_r_col
    
    return blue, red 
