#Find the minimum and maximum values of a 10 x 10 random matrix.

#-Importing:
import numpy as np, string as st

#-Matrix
rng = np.random.default_rng()
mattrix_lobster = rng.random((10,10))

#-Find max and minimum:
max = round(np.max(mattrix_lobster),4)
min = round(np.min(mattrix_lobster),4)

#-Text template:
message = st.Template('The max number is $mx and the minimum number is $mm').safe_substitute(mx=max,mm=min)
print(message)