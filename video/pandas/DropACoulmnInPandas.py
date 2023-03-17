# youtube.com/@ailearningcorner ----------
# Drop a column in DataFrame Pandas
import pandas as pd
import numpy as np

# Create a DF from NP Array
arr = np.random.randn(4, 4)
df = pd.DataFrame(arr, columns='A B C D'.split())
#print(df)
# Drop a Column

df.drop('D', axis=1)
#print(df)

df.drop('D' , axis=1, inplace=True)
print(df)