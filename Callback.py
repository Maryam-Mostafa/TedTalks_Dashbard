from dash.dependencies import Output, Input
import plotly.express as px
from run import app
from dataPreperation import get_dataFrame
import pandas as pd

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
    fig = px.bar(duration.iloc[:10,:10], x='title', y='duration',color='duration',
                 color_continuous_scale='RdGy',labels={'title':'Title of talk'}, template= 'simple_white', text = 'title')
    fig.update_traces(textposition='inside')
    fig.update(layout_coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig


@app.callback(Output('year-month_fig','figure'), [Input("tabs_ym", "active_tab")])
def switch_tab_month_year(at):
    flag = False
    if at == "year_id":
        flag = False
        year_wise_talks_frequency = pd.DataFrame()
        year_wise_talks_frequency["count"] = df.groupby("year").size()
        fig = px.line(year_wise_talks_frequency, x=year_wise_talks_frequency.index, y="count",

                      labels={'year': 'Year', 'count': 'Frequency'})

    elif at == "month_id":
        month_wise_talks_frequency = pd.DataFrame()
        df['count'] = df.groupby("month").size()
        month_wise_talks_frequency["count"] = df.groupby("month").size()
        fig = px.line(month_wise_talks_frequency, x=month_wise_talks_frequency.index,
                      y=month_wise_talks_frequency["count"],
                      labels={'month': 'Month', 'count': 'Frequency'})
        fig.update_layout(
            #autosize=True,
            margin=dict(l=20, r=20, t=20, b=20))
    return fig
