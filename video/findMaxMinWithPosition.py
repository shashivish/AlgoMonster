# youtube.com/@ailearningcorner ----
# Find Max and Min from NP Array
# and their positions.

import numpy as np

arr = np.random.randint(1, 100, 10)

print("Array is : ", arr)
print("Max Element is : ", arr.max())
print("Max Element Position : ", arr.argmax())

print("Min Element is : ", arr.min())
print("Min Position is : ", arr.argmin())
