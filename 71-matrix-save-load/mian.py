#Save a NumPy matrix to a binary file in .npy format and load it back into a different variable.

#-Importing : The module!
import numpy as np, os

#-Getting directory : The file!
my_dirdir = os.path.dirname(__file__)

#-Creating : The matrix!
mad = np.array([[66,4,42],[3,3,6],[7,5,3],[8,5,5],[47,23,66]])

#-Saving : The matrix!
fnamer = os.path.join(my_dirdir,'the_matrix.npy')
np.save(fnamer,mad)

#-Loading : The data!
my_data = np.load(fnamer)
print(my_data)