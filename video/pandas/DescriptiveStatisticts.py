# youtube.com/@ailearningcorner ----------
# Descriptive Statistics of DataFrame
import pandas as pd

data = {'Rating': [5, 3, 2, 4],
        'Age': [12, 19, 34, 44],
        'Prices': [45, 99, 0, 2],
        'Distance': [1000, 1200, 340, 193]}
df = pd.DataFrame(data)

# Print Descriptive Statistics for DatFrame
print(df.describe())
