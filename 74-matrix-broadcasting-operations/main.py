#Perform matrix-scalar multiplication on a 2 x 3 matrix using broadcasting.

#-Importing : The module
import numpy as np

#-Creating : The matrix
marathon_1 = np.array([[1,2],[7,5],[2,7]])

#-Doing : The broadcasting
result = marathon_1 * 5

#-Displaying : The post-broadcasting matrix
print(result)