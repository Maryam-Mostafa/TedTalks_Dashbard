from dash.dependencies import Output, Input
import plotly.express as px
from run import app
from dataPreperation import get_dataFrame
import pandas as pd
from StaticCharts import *

df = get_dataFrame()
# tabs graphs update call back
@app.callback(Output('duration_fig1','figure'), [Input("tabs", "active_tab")])
def switch_tab(at):
    flag = False
    if at == "tab1_id":
        flag = False
    elif at == "tab2_id":
        flag = True
    duration = df[['title','duration']].sort_values('duration', ascending = flag)
    fig = px.bar(duration.iloc[:10], x='title', y='duration',color='duration',
                 color_continuous_scale= ['#ffb08a', '#f29c7d', '#e68970', '#d97563', '#cd6256', '#c04e49', '#b43b3c', '#a7272f', '#9b1422', '#8e0015'],labels={'title':'Title of talk'}, template= 'simple_white', text = 'title')
    fig.update_traces(textposition='inside')
    fig.update(layout_coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig



@app.callback(Output('year-month_fig','figure'), [Input("tabs_ym", "active_tab")])
def switch_tab_month_year(at):
    return new_scatter_line(df,at)
    #flag = False
    # if at == "year_id":
    #     flag = False
    #     year_wise_talks_frequency = pd.DataFrame()
    #     year_wise_talks_frequency["count"] = df.groupby("year").size()
    #     fig = px.area(year_wise_talks_frequency, x=year_wise_talks_frequency.index, y="count",
    #                   labels={'year': 'Year', 'count': 'Frequency'}, template="simple_white")
    #
    # elif at == "month_id":
    #     month_wise_talks_frequency = pd.DataFrame()
    #     df['count'] = df.groupby("month").size()
    #     new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
    #                  'November', 'December']
    #     month_wise_talks_frequency = month_wise_talks_frequency.reindex(new_order, axis=0)
    #     month_wise_talks_frequency["count"] = df.groupby("month").size()
    #     fig = px.area(month_wise_talks_frequency, x=month_wise_talks_frequency.index,
    #                   y=month_wise_talks_frequency["count"], color="count", markers=True,
    #                   labels={'month': 'Month', 'count': 'Frequency'}, template="simple_white")
    #


@app.callback(

    Output('pop_occupation', 'figure'),
    Output('pop_speaker', 'figure'),
    Output('pop_talk', 'figure'),
    Output('most_disscused_talk', 'figure'),

    Input('main_slider_id', 'value')
)
def update_graphs_bySlider(curr_year):
    filterDf = df[df.year == curr_year]

    return most_popular_speaker_occupation(filterDf),\
           most_popular_speaker(filterDf),\
           mostPopularTalk(filterDf),\
           popular_talk_pieChart(filterDf)
