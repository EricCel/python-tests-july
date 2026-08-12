#Stack two 2 x 3 matrices vertically and then horizontally using vstack and hstack.

#-Importing : Module!
import numpy as np

#-Matrices : Arrays!
first_matrix = np.array([[9,4,6,2,6],[6,2,1,6,2],[7,3,1,2,6]])
second_matrix = np.array([[6,1,2,3,5],[1,8,2,4,6],[8,6,4,2,7]])

#-Stacking : Matrices!
vertically = np.vstack((first_matrix,second_matrix))
horizontally = np.hstack((first_matrix,second_matrix))

#-Displaying : The stacking!
print(f'==Vertical stack==\n{vertically}')
print(f'==Horizontal stack==\n{horizontally}')