import numpy as np

arr = np.arange(100).reshape(5,-1)

print("The original array: \n", arr, "\n")
print("The extracted array:")
print(arr[:,:4])