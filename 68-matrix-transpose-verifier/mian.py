#Apply the transpose (.T or .transpose()) to a 3 x 5 matrix and verify the resulting dimensions.

#-Importing : The module!
import numpy as np

#-The matrix : To transpose!
matter = np.array([[13,64,23],[75,34,23],[62,12,99],[77,23,65],[23,12,76]])

#-.T : First method!
transposed_1 = matter.T #-Transpose
print(transposed_1) #-Display

#-.transpose() : Second method!
transposed_2 = matter.transpose() #-Transpose
print(transposed_2) #-Display