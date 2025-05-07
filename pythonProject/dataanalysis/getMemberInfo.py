import pandas as pd

filename = 'memberInfo.csv'
df = pd.read_csv(filename)
print('df:\n', df)

newdf01 = df.set_index(keys=['id'])  # drop=True (기본값)
print('newdf01:\n', newdf01)

newdf02 = df.set_index(keys=['id'], drop=False)
print('newdf02:\n', newdf02)

df02 = pd.read_csv(filename, index_col='id')
print('df02:\n', df02)
