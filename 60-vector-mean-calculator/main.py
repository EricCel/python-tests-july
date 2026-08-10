#Generate a random vector of size 30 and calculate its mean value.

#-Importing:
import numpy as np

#-Vector:
rng = np.random.default_rng()
the_vec = rng.random(30)

#-Display:
print(the_vec.mean())