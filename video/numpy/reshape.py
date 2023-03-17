# youtube.com/@ailearningcorner ----
# ReShape one dimensional array to
# 2D array
import numpy as np

# One Dimensional Array
arr = np.arange(16)
print(arr)

# ReShape into [4,4] 2D array
re_arr = arr.reshape(4,4)
print(re_arr)
