import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt

from dataPreperation import get_dataFrame
from wordcloud import WordCloud
from PIL import Image
import numpy as np

df = get_dataFrame()
red_pallete = ['#ff0000','#ffa07a','#f08080','#fa8072','#e9967a','#ff6347','#cd5c5c','#ff4500','#dc143c','#b22222','#8b0000','#800000']


def mostPopularTalk():
    most_popular_talk_by_views = df.sort_values(by="views",ascending=False)
    fig = px.bar(most_popular_talk_by_views[:10], y="title", x="views", text = 'title',orientation='h',
                  color='title' ,color_discrete_sequence=px.colors.sequential.Reds)
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False)
                      )


    return fig


def popular_talk_pieChart():
    popular_df = df[['title', 'comments']].sort_values('comments', ascending = False)
    fig = px.pie(popular_df.iloc[:5,:5], values='comments', names='title', hole=.2, color_discrete_sequence=px.colors.sequential.RdBu)# height = 500)
    fig.update(layout_showlegend=False)
    return fig


def most_popular_speaker():
    top_speakers = df.sort_values(by="views", ascending=False)
    fig = px.bar(top_speakers[:10], x="views", y="main_speaker",
                 orientation='h', color='main_speaker', color_discrete_sequence=px.colors.sequential.Reds,
                 labels={'title': 'TED talks title', 'views': 'Total number of views'}, text = 'main_speaker')
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False)
                      )
    return fig

def most_popular_speaker_occupation():
    top_occupations = df.sort_values(by="views", ascending = False)
    fig = px.bar(top_occupations[:10], x="views", y="speaker_occupation",
                 orientation='h', color='speaker_occupation', color_discrete_sequence=px.colors.sequential.Reds,
                 labels={'views': 'TED talks Views', 'speaker_occupation': 'Speaker Occupation'}, text='speaker_occupation')
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False)
                      )
    return fig


# word cloud
tag_dict = pd.Series([x for _list in df.tags for x in _list])
count = {}
for word in tag_dict:
    count.setdefault(word, 0)
    count[word] += 1

list_count = list(count.items())
list_count.sort(key=lambda i: i[1], reverse=True)
# for i in list_count:
#    print(i[0], ':', i[1])


#### this part not working with me ####
# plt.subplots(figsize = (8,8))
# wordcloud = WordCloud (
#     background_color = 'white',
#     colormap = 'gist_heat',
#     width = 1000,
#     height = 600,max_words=11100
# ).generate(str(list_count))
# plt.imshow(wordcloud) # image show
# plt.axis('off') # to off the axis of x and y
# plt.savefig("wordcloud.png")
