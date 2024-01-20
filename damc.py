import pandas as pd
import numpy as np
import seaborn as sns
from collections import Counter
df=pd.read_excel('Games Sales.xlsx')
df.head()
print(df.head())
print(df.count())
print(df.value_counts())

print(df['Name'].value_counts())
#print(df['Name'].value_types())
print(df['Release'].value_counts())

df_modified=df['Name'].duplicated()
print(df_modified.drop_duplicates())
df_upd=df.dropna()
df.drop_duplicates()
print(df.value_counts())
df['Release']=pd.to_datetime(df['Release'])
print(max(df['Release']))
print(min(df['Release']))

numonemax=max(df.groupby('Release',as_index=False)['Name'])
print(numonemax)
numonemin=min(df.groupby('Release',as_index=False)['Name'])
print(numonemin)

#df['Publisher']=pd.to_string(df['Publisher'])
k= df['Publisher'].value_counts()
numtwo=df.groupby('Publisher',as_index=False).value_counts()
m=df['Developer'].value_counts()
print(k)
print(m)

numford=max(df_upd.groupby('Sales',as_index=False)['Series'])
print(numford)

#numfif=max(df.groupby('Release',as_index=False)['Series'])
#print(numfif)

lm=df_upd['Series'].value_counts()
print(lm)

kl=max(lm)
print(kl)