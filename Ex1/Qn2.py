#Convert a 1-D array into a 2-D array with 3 rows

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

print("The original array: \n", arr, "\n")

print("Reshaped array: \n", arr.reshape(3,-1), "\n")
