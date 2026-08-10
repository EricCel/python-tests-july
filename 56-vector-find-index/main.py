#Find the indices of non-zero elements within the array np.array([1, 2, 0, 0, 4, 0]).

#-Importing:
import numpy as np

#-Vector:
vector_victor = np.array([1, 2, 0, 0, 4, 0])

#-Function:
def array_nonzero_finder(arr):
    return [i for i in range(arr.size) if arr[i] != 0]

#-Displaying:
print(array_nonzero_finder(vector_victor))
