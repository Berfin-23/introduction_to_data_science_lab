#Generate a 1-D array of 10 random integers. Each integer should be a number between 30 and 40 (inclusive)

import numpy as np

arr = np.random.randint(30, 41, size = (10))
print(arr)