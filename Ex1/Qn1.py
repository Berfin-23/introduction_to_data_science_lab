import numpy as np

arr = np.array([x for x in range(10)])
arr[arr % 2 == 1] = -1

print(arr)