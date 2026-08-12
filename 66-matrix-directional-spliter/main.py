#Take a 6 x 4 matrix and split it into 2 equal 3 x 4 matrices using hsplit or vsplit.

#-Importing : Module!
import numpy as np

#-Matrix : Array!
springtrap = np.array([[6,4,7,2,4,8],[6,4,7,2,4,8],[6,4,7,2,4,8],[6,4,7,2,4,8]])

#-Spliting : Using hsplit!
arr_1, arr_2 = np.hsplit(springtrap,2)

#-Displaying : The matrices!
'22.37'
print(arr_1,'\n\n',arr_2)