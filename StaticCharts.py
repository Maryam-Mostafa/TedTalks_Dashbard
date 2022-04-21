import plotly.express as px
import pandas as pd
from dataPreperation import get_dataFrame

df = get_dataFrame()

def mostPopularTalk():
    most_popular_talk_by_views = df.sort_values(by="views",ascending=False)
    fig = px.bar(most_popular_talk_by_views[:10], x="views", y="title", title='Most popular TED talks',text = 'views',
                 orientation='h', color='title' ,color_discrete_sequence=px.colors.sequential.Teal)
    fig.update_traces(textposition='inside')
    fig.update(layout_showlegend=False)
    #fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    return fig


def popular_talk_pieChart():
    popular_df = df[['title', 'comments']].sort_values('comments', ascending = False)
    fig = px.pie(popular_df.iloc[:5,:5], values='comments', names='title', hole=.2, color_discrete_sequence=px.colors.sequential.Reds)# height = 500)
    return fig


# for getting most popular spreaker
top_ted_talks_speaker_obj = {}
for index, row in df.iterrows():
    speaker = row["main_speaker"]
    if speaker not in top_ted_talks_speaker_obj:
        ted_talk_obj = {}
        ted_talk_obj["speaker_count"] = 1
        ted_talk_obj["views"] = row["views"]
        ted_talk_obj["comments"] = row["comments"]
        ted_talk_obj["main_speaker"] = speaker
    else:
        ted_talk_obj = top_ted_talks_speaker_obj.get(speaker)
        ted_talk_obj["speaker_count"] += 1
        ted_talk_obj["views"] += row["views"]
        ted_talk_obj["comments"] += row["comments"]
        ted_talk_obj["main_speaker"] = speaker
    top_ted_talks_speaker_obj[speaker] = ted_talk_obj

top_ted_talks_speaker = pd.DataFrame(top_ted_talks_speaker_obj.values())
top_ted_talks_speaker = top_ted_talks_speaker.sort_values(by="speaker_count",ascending=False)

def most_popular_speaker():
    top_speakers = top_ted_talks_speaker[:10]
    fig = px.bar(top_speakers, x = "speaker_count", y = "main_speaker",title='Most popular Speaker',
                 orientation='h', color='main_speaker' ,color_discrete_sequence=px.colors.sequential.Reds,
                 labels={'title':'TED talks title' , 'views': 'Total number of views'} )
    #fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    #fig.update_yaxes(ticksuffix = "    ")
    return fig

# word cloud
tag_dict = pd.Series([x for _list in df.tags for x in _list])
count = {}
for word in tag_dict:
    count.setdefault(word, 0)
    count[word] += 1

list_count = list(count.items())
list_count.sort(key=lambda i: i[1], reverse=True)
for i in list_count:
    print(i[0], ':', i[1])
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
# plt.show()
