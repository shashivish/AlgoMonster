# youtube.com/@ailearningcorner ----------
# Count of Categories in DF Column

import pandas as pd

data = {'Sports': ['Cricket', 'Football',
                   'Cricket', 'Hockey',
                   'BaseBall', 'Football',
                   'Football', 'Cricket',
                   'Cricket', 'Hockey']}

df = pd.DataFrame(data)
# Print Count of Each Category in
# Dataframe Column
print(df['Sports'].value_counts())
