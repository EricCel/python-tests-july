#Create a 3 * 3 matrix with consecutive values from 0 to 8 using arange and reshape.

#-Importing:
import numpy as np

#-Array:
theArr = np.arange(0,9)

#-Matrix:
theArr = theArr.reshape(3,3)

#-Display:
print(theArr)