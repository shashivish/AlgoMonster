# youtube.com/@ailearningcorner ----------
# Conditional Selection on DataFrame Col
import pandas as pd

data = {'Chanel': ["AI", "Learning",
                   "Channel", "YouTube"],
        'Age': [12, 19, 34, 44]}
df = pd.DataFrame(data)

# print(df)

# Select Rows where Age > 20

print(df[df['Age'] > 20])
