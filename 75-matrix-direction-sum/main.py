#Calculate the column sum (axis 0) and row sum (axis 1) of a 4 x 4 matrix.

#-Importing : The module
import numpy as np

#-Creating : The matrix
aaaah_matrix = np.array([[6,4,7,7],[1,2,7,3],[8,8,5,1],[8,6,9,3]]) # "Column" : Vertical!. "Row" : Horizontal!

#-Doing : The directional sum
column_sum_am = np.sum(aaaah_matrix,0)
row_sum_am = np.sum(aaaah_matrix,1)

#-Displaying : The results
print(column_sum_am, row_sum_am)