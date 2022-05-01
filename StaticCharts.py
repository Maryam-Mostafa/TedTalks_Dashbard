import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
import plotly.graph_objects as go
from dataPreperation import get_dataFrame
#from wordcloud import WordCloud
import seaborn as sns

data = get_dataFrame()

red_pallete = ['#8e0015', '#9b1422', '#a7272f', '#b43b3c', '#c04e49', '#cd6256', '#d97563', '#e68970', '#f29c7d',
               '#ffb08a']


# view most popular talk based on views in a bar chart
def mostPopularTalk(df):
    most_popular_talk_by_views = df.sort_values(by="views", ascending=False)
    fig = px.bar(most_popular_talk_by_views[:10], y="title", x="views", text='title', orientation='h',
                 color='title', color_discrete_sequence=red_pallete, template="simple_white")
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      margin=dict(l=20, r=20, t=20, b=20))

    return fig


# view the most discussed talks based on comment in a donut chart
def popular_talk_pieChart(df):
    popular_df = df[['title', 'comments']].sort_values('comments', ascending=False)
    fig = px.pie(popular_df.iloc[:5], values='comments', names='title', hole=.2,
                 color_discrete_sequence=red_pallete, template="simple_white")
    fig.update_layout(
        legend=dict(xanchor="center", orientation="h", x=0.5, y=-0.2),
        margin=dict(l=20, r=20, t=20, b=20))
    return fig


# view popular speaker based on views in a bar chart
def most_popular_speaker(df):
    top_speakers = df.sort_values(by="views", ascending=False)
    top_speakers.drop_duplicates(subset=['main_speaker'], inplace=True)
    fig = px.bar(top_speakers[:10], x="views", y="main_speaker",
                 orientation='h', color='main_speaker', color_discrete_sequence=red_pallete,
                 labels={'title': 'TED talks title', 'views': 'Total number of views'}, text='main_speaker',
                 template="simple_white")
    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig


# view most popular speaker occupation in a bar chart
def most_popular_speaker_occupation(df):
    top_occupations = df.sort_values(by="views", ascending=False)
    top_occupations.drop_duplicates(subset=['speaker_occupation'], inplace=True)

    fig = px.bar(top_occupations[:10], x="views", y="speaker_occupation",
                 orientation='h', color='speaker_occupation', color_discrete_sequence=red_pallete,
                 labels={'views': 'TED talks Views', 'speaker_occupation': 'Speaker Occupation'},
                 text='speaker_occupation', template="simple_white")

    fig.update_traces(textposition='inside')
    fig.update_yaxes(showticklabels=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig


# view talk based on duration in a bar chart
def durationBar_chart(df, at):
    flag = False
    if at == "tab1_id":
        flag = False
    elif at == "tab2_id":
        flag = True
    duration = df[['title', 'duration']].sort_values('duration', ascending=flag)
    fig = px.bar(duration.iloc[:10], x='title', y='duration', color='duration',
                 color_continuous_scale=['#ffb08a', '#f29c7d', '#e68970', '#d97563', '#cd6256', '#c04e49', '#b43b3c',
                                         '#a7272f', '#9b1422', '#8e0015'], labels={'title': 'Title of talk', 'duration':'duration (sec)'},
                 template='simple_white', text='title')

    fig.update_traces(textposition='inside')
    fig.update(layout_coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), )

    return fig


# area chart of year and month
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
        yaxis=dict(title='Number of talks'),
        template='plotly_white',
        margin=dict(l=20, r=20, t=20, b=20)
    )
    fig = go.Figure(data=trace, layout=layout)
    return fig


# # creating word cloud and save it as img
# def create_wordCloud_img():
#     tag_dict = pd.Series([x for _list in data.tags for x in _list])
#     count = {}
#     for word in tag_dict:
#         count.setdefault(word, 0)
#         count[word] += 1
#
#     list_count = list(count.items())
#     list_count.sort(key=lambda i: i[1], reverse=True)
#     for i in list_count:
#         print(i[0], ':', i[1])
#
#     plt.subplots(figsize=(8, 8))
#     wordcloud = WordCloud(
#         background_color='white',
#         colormap='gist_heat',
#         width=800,
#         height=800, max_words=11100
#     ).generate(str(list_count))
#     plt.imshow(wordcloud)  # image show
#     plt.axis('off')  # to off the axis of x and y
#     plt.savefig("wordcloud.png")
#     plt.show()

