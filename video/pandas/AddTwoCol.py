# youtube.com/@ailearningcorner ----------
#  Add Two Column and Write Result to Third
# Column

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [5, 10, 15, 20],
                   'B': [1, 2, 3, 4]})

# Create a new column C that is the
# sum of columns A and B
df['C'] = df.apply(lambda r: r['A'] +
                             r['B'],
                   axis=1)
print(df)
