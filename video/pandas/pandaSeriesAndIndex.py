# youtube.com/@ailearningcorner ----------
# How to Create Pandas Series and
# Assign label to index .
import numpy as np
import pandas as pd

age_arr = np.array([17, 35, 4, 39])
age_label = ['Teenage', 'Adult', 'Kid',
             'Adult']

# print(pd.Series(data=age_arr))
print(pd.Series(data=age_arr,
                index=age_label))
