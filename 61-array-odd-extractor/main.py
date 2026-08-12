#Given a one-dimensional array, extract all odd numbers using a boolean mask.

#-Importing: Module!
import numpy as np

#-Array: Vector!
the_toex_arr = np.array([6,6,3,1,6,78,8,4])

#-Extract: Maskof conditionals!
mask = the_toex_arr % 2

#-Display:
print(f'The odd numbers of the array are {the_toex_arr[mask == 0]} and the even are {the_toex_arr[mask != 0]}')