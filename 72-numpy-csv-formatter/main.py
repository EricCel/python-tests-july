#Export a NumPy matrix of decimals to a .csv file formatted to 2 decimal places and comma-delimited, then read it back using np.loadtxt()

#-Importing : The module
import numpy as np, os, time

#-Creating : The matrix
matt_matt = np.array([[1.6,2.3,5.8,67.87],[2.3,56.45,7.7,5.5],[4.2,6.3,7.4,45.5]])

#-Creating : The file name and path
nowtoday = time.time()
dih = os.path.dirname(__file__)
csv_m = os.path.join(dih,f'{str(nowtoday).replace('.','_')}.csv')

#-Saving : The matrix
np.savetxt(csv_m,matt_matt,fmt='%.2f',delimiter=',')

#-Loading : The matrix
new = np.loadtxt(csv_m,delimiter=',')

#-Displaying : The saved matrix
print(new)