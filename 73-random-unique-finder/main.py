#Generate an array of repeated random integers and extract only the unique values in sorted order using np.unique().

#-Importing : The module
import numpy as np

#-Generating : The array
rng = np.random.default_rng()
garray = rng.integers(1,50,size=100)

#-Extracting : The unique
the_unique = np.unique(garray)

#-Displaying : The values
print(garray)
print(the_unique)