#Add a new axis to a 1D vector to convert it into an N x 1 column matrix using np.newaxis.

#-Importing : The module!
import numpy as np

#-The vector : An array!
victory = np.array([76,34,53,72,34])

#-Adding new axis : 2D column vector, N x 1!
victory = victory[:,np.newaxis]

#-Displaying : The matrix!
print(victory)