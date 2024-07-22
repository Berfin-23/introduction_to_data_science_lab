#Add 202 to all the values in given array

import numpy as np

arr = np.arange(4).reshape(2,-1)

print("The original array:\n", arr, "\n")
print("Method 1: \n",arr + np.full((2,2),202))