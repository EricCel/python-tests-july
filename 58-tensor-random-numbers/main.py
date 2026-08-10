#Create a 3 x 3 x 3 array of random floating-point numbers.

#-Importing:
import numpy as np

#-Tensor:
rng = np.random.default_rng()
my_tensor = rng.random((3,3,3))

#-Displaying:
print(my_tensor)