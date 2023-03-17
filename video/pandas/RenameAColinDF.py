# youtube.com/@ailearningcorner ----------
# Rename a Column in DF
import pandas as pd

# Create DF
df = pd.DataFrame({'A': [1, 2, 3, 4]})

df = df.rename(columns={'A': 'New_Col'})
print(df)
