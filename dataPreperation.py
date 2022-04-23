import pandas as pd

# Read The Ted DataSet
df = pd.read_csv("ted_main.csv")
# Print The First Row of the Data(df)
# print(df.head(1))


#get Data_set Information (Nulls , Numbers of Records , Data Types)
# print(df.info())

# Count Null Values of each Column
# print(df.isna().sum())

#Preprocessing The Data

#Convert The Date Col. from Unix Timestamp to Date Type
df['Date'] = pd.to_datetime(df['published_date'], unit='s')

#Drop Some Columns.
df.drop(columns = ['description','event', 'film_date', 'languages', 'name','num_speaker',
                   'published_date' , 'ratings', 'related_talks'], axis = 1 , inplace = True)

# print(df.head(1))

# print(df.info())

#df['month'] = df['Date'].map(lambda x: x.month)
# df['month'].sort_values()
df['month']= df['Date'].dt.month_name()
df["year"] = df['Date'].map(lambda x: x.year)
# print(df.head(1))
df.drop('Date', inplace = True , axis =1)
# print(df.head(20))
# print(df.info())
df["tags"] = df["tags"].apply(eval)

def get_dataFrame():
    return  df
