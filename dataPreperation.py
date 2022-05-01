import pandas as pd
from dash import html

# Read The Ted DataSet
df = pd.read_csv("ted_main.csv")

# Print The First Row of the Data(df)
# print(df.head(1))

# get Data_set Information (Nulls , Numbers of Records , Data Types)
# print(df.info())

# Count Null Values of each Column
# print(df.isna().sum())

# ====================================   Preprocessing The Data   ====================================

# fill null values in speaker occupation with unknown
df['speaker_occupation'].fillna('unknown', inplace=True)

# Convert The Date Col. from Unix Timestamp to Date Type
df['Date'] = pd.to_datetime(df['published_date'], unit='s')

# Drop Some Columns.
df.drop(columns=['event', 'film_date', 'languages', 'name', 'num_speaker',
                 'published_date', 'description', 'related_talks'], axis=1, inplace=True)

# print(df.head(1))
# print(df.info())

# getting year and month from date then drop date
df['month'] = df['Date'].dt.month_name()
df["year"] = df['Date'].map(lambda x: x.year)

# print(df.head(1))

df.drop('Date', inplace=True, axis=1)

# print(df.head(1))
# print(df.info())

# apply eval to tags
df["tags"] = df["tags"].apply(eval)

# update the formate of url col, so it can be clickable
link = []
for i in df['url']:
    link.append(html.A(html.P('Talk url'), href=i, target='_blank'))
df['url'] = link

# preprocessing column ratings
df1 = pd.concat([pd.DataFrame(eval(x)) for x in df['ratings']], keys=df.index).reset_index(level=1, drop=True)
df = df.join(df1).reset_index(drop=True)
df = df.loc[df.groupby(['title'])['count'].idxmax()]
new_data = df.drop(['id', 'ratings'], axis=1).reset_index(drop=True)

# print(len(new_data))
# print(new_data.iloc[0])

# returning the data frame to be used in many others files
def get_dataFrame():
    return new_data
