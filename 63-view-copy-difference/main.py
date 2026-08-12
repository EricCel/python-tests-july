#Demonstrate the practical difference between a view and a copy by modifying a slice of an array and observing the original.

#-Importing : Module!
import numpy as np

#-The array : Vector!
the_array = np.array([7,5,3,51,3])

#-Differences : View and copy!
#--View : Part of the original
the_array[2:5] = 2
print(f'==View==\nModified view : {the_array}')
#--Copy : Recreation of the original
the_array_new = the_array.copy()
the_array_new[2:5] = 3
print(f'==Copy==\nOriginal : {the_array}\nCopy : {the_array_new}')