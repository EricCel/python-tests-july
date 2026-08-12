#Compare the behavioral difference between .flatten() and .ravel() when modifying an element in the resulting array.

#-Importing : The module!
import numpy as np

#-The array : A matrix!
giaaaaaaargh = np.array([[6,4,2,7,1],[8,9,5,3,1],[8,3,2,1,9]])

#-Differences :
#--Flatten : Returns a copy!
flattened = giaaaaaaargh.flatten() #-Flatten
flattened[2] = 166 #-Changing
print(f'Original :\n{giaaaaaaargh}\nFlattened :\n{flattened}\n\n') #-Display
#--Ravel : Returns a view!
raveled = giaaaaaaargh.ravel() #-Ravel
raveled[2] = 122 #-Changing
print(f'Original :\n{giaaaaaaargh}\nRaveled :\n{raveled}\n\n') #-Display