# youtube.com/@ailearningcorner ----------
# Apply Function to Column Values in DF.
import pandas as pd

# Function to Computes Square of a Number
def square_fun(x):
    return x**2
# Create DF
df = pd.DataFrame({'A': [1, 2, 3, 4]})

# Apply Function
df['A_sqr'] = df['A'].apply(square_fun)

print(df)
