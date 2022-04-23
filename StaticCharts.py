import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
import plotly.graph_objects as go
from dataPreperation import get_dataFrame
from wordcloud import WordCloud
from PIL import Image
import numpy as np
# try again
data = get_dataFrame()
red_pallete = ['#ff0000', '#ffa07a', '#f08080', '#fa8072', '#e9967a', '#ff6347', '#cd5c5c', '#ff4500', '#dc143c',
               '#b22222', '#8b0000', '#800000']


def mostPopularTalk(df):
    most_popular_talk_by_views = df.sort_values(by="views", ascending=False)
    fig = px.bar(most_popular_talk_by_views[:10], y="title", x="views", text='title', orientation='h',
                 color='title', color_discrete_sequence=px.colors.sequential.Reds, template="simple_white")
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      margin=dict(l=20, r=20, t=20, b=20))

    return fig


def popular_talk_pieChart(df):
    popular_df = df[['title', 'comments']].sort_values('comments', ascending=False)
    fig = px.pie(popular_df.iloc[:5], values='comments', names='title', hole=.2,
                 color_discrete_sequence=px.colors.sequential.RdBu, template="simple_white")  # height = 500)
    fig.update_layout(
        legend=dict(xanchor="center", orientation="h", x=0.5, y=-0.2),
        margin=dict(l=20, r=20, t=20, b=20))
    return fig


def most_popular_speaker(df):
    top_speakers = df.sort_values(by="views", ascending=False)
    top_speakers.drop_duplicates(subset=['main_speaker'], inplace=True)
    fig = px.bar(top_speakers[:10], x="views", y="main_speaker",
                 orientation='h', color='main_speaker', color_discrete_sequence=px.colors.sequential.Reds,
                 labels={'title': 'TED talks title', 'views': 'Total number of views'}, text='main_speaker',
                 template="simple_white")
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig


def most_popular_speaker_occupation(df):
    top_occupations = df.sort_values(by="views", ascending=False)
    top_occupations.drop_duplicates(subset=['speaker_occupation'], inplace=True)
    fig = px.bar(top_occupations[:10], x="views", y="speaker_occupation",
                 orientation='h', color='speaker_occupation', color_discrete_sequence=px.colors.sequential.Reds,
                 labels={'views': 'TED talks Views', 'speaker_occupation': 'Speaker Occupation'},
                 text='speaker_occupation', template="simple_white")
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig


def new_scatter_line(df, at):
    trace, x_axis = None, ''
    if at == "year_id":
        x_axis = 'Years'
        year_wise_talks_frequency = pd.DataFrame()
        year_wise_talks_frequency["count"] = df.groupby("year").size()
        trace = go.Scatter(x=year_wise_talks_frequency.index, y=year_wise_talks_frequency["count"], fill='tozeroy',
                           mode='lines+markers',
                           line=dict(width=2, color='#b22222'))  # fill down to xaxis
    elif at == "month_id":
        x_axis = 'Months'
        month_wise_talks_frequency = pd.DataFrame()
        df['count'] = df.groupby("month").size()
        new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
        month_wise_talks_frequency = month_wise_talks_frequency.reindex(new_order, axis=0)
        month_wise_talks_frequency["count"] = df.groupby("month").size()
        trace = go.Scatter(x=month_wise_talks_frequency.index, y=month_wise_talks_frequency["count"], fill='tozeroy',
                           mode='lines+markers',
                           line=dict(width=2, color='#b22222'))

    layout = go.Layout(
        xaxis=dict(title=x_axis),
        yaxis=dict(title='Frequency'),
        template='simple_white',
        margin=dict(l=20, r=20, t=20, b=20)
    )
    fig = go.Figure(data=trace, layout=layout)
    return fig

#word cloud
def create_wordCloud_img():
    tag_dict = pd.Series([x for _list in data.tags for x in _list])
    count = {}
    for word in tag_dict:
        count.setdefault(word, 0)
        count[word] += 1

    list_count = list(count.items())
    list_count.sort(key=lambda i: i[1], reverse=True)
    for i in list_count:
       print(i[0], ':', i[1])


    # #### this part not working with me ####
    plt.subplots(figsize = (8,8))
    wordcloud = WordCloud(
        background_color = 'white',
        colormap = 'gist_heat',
        width = 1000,
        height = 600,max_words=11100
    ).generate(str(list_count))
    plt.imshow(wordcloud) # image show
    plt.axis('off') # to off the axis of x and y
    plt.savefig("wordcloud.png")
    plt.show()
