# youtube.com/@ailearningcorner ----------
# iloc example in Pandas Dataframe
import pandas as pd

# df.iloc[start:stop:step ,start:stop:step ]

data = {'Chanel': ["AI", "Learning",
                   "Channel", "YouTube"],
        'Months': [1, 2, 3, 4]}
df = pd.DataFrame(data)
print(df)

# Select 4th Row and 1st Column
print("4rd Row and First Column is :")
print(df.iloc[3, 0])
