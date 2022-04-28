import re
from dataPreperation import get_dataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = get_dataFrame()
df = df.loc[:,['title', 'main_speaker', 'speaker_occupation', 'url', 'views', 'tags']]

# clean the tags from comma's prases etc
def clean_text(x):
    letter_only = re.sub("[^a-zA-Z]", " ", x)
    return ' '.join(letter_only.split()).lower()

df.tags = df.tags.astype('str')
df['tags'] = df['tags'].apply(clean_text)


# Convert to sparse matrix using count vectorize to get features
cv = CountVectorizer()
cv_tags = cv.fit_transform(df['tags'])

# using Cosine Similarity
cos_sim = cosine_similarity(cv_tags)

def get_recommendation_based_title(x):
    index_to_search = df[df['title'] == x].index[0]
    series_similar = pd.Series(cos_sim[index_to_search])
    index_similar = series_similar.sort_values(ascending=False).head(10).index
    return df.loc[index_similar]

# print(get_recommendation_based_title('Do schools kill creativity?'))
