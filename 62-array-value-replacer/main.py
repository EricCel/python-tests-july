#Replace all values greater than 10 in an array with the fixed value -1 without modifying the rest.

#-Importing : Module!
import numpy as np

#-Array : Vector!
myArr = np.array([1,15,6,11,2,4,745,5,23,2])

#-Mask : Greater than 10!
masker = myArr > 10

#-Changing : The true values!
myArr[masker] = -1

#Displaying : The modified vector!
print(myArr)