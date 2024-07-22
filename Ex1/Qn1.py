#Replace all odd numbers in the given array with -1

import numpy as np

arr = np.array([x for x in range(10)])
arr[arr % 2 == 1] = -1

print(arr)