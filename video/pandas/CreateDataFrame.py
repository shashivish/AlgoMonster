# youtube.com/@ailearningcorner ----------
# Create a DataFrame from Numpy Array
import numpy as np
import pandas as pd

arr = np.random.randn(5, 4)
# print(arr)

# Create a DataFrame
df = pd.DataFrame(data=arr)
# print(df)
# Assign Name to Each column
df = pd.DataFrame(data=arr,
                  columns="A B C D".split())
print(df)
