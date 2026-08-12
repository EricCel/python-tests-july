#Reverse only the columns of a two-dimensional matrix using np.flip().

#-Importing : The module!
import numpy as np

#-Matrix : The array!
arrgh = np.array([[6,4,7,1,2],[7,4,9,2,1],[8,3,1,2,1]])

#-Flip : The colums!
arrgh2 = np.flip(arrgh,axis=1)

#-Display : The matrix!
print(f'Original\n{arrgh}')
print(f'New\n{arrgh2}')