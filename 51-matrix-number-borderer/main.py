#Create a 5 x 5 matrix with 1s on the border and 0s on the inside.

#-Importing:
import numpy as np

#-Method 1:
def delimited_matrix(filler = 0, border = 1,width = 4, height = 4) -> int:
    arr = np.full((width,height),filler)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if i == 0 or i == arr.shape[0] - 1 or j == 0 or j == arr.shape[1] - 1:
                arr[i,j] = border
    return arr

print(delimited_matrix(0,1,5,5))

#-Method 2:
def alt_delimited_matrix(filler = 0, border = 1,width = 4, height = 4) -> int:
    if 1 in (width,height) or 0 in (width,height):
        return filler
    else:
        tba = [[border] * width]
        mid_arr = tba[0].copy(); mid_arr[1:-1] = [filler] * (width - 2)
        [tba.append(mid_arr) for i in range(height - 2)]; tba.append(tba[0])
        return np.array(tba)
print(alt_delimited_matrix(1,2,20,20))