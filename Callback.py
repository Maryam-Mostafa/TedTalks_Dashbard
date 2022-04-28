from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import plotly.express as px
import dash
from run import app
from dataPreperation import get_dataFrame
import pandas as pd
from StaticCharts import *
from Components import analysis_container, recommendation_container
from recommendation_system import get_recommendation_based_title

df = get_dataFrame()


# tabs duration graph update
@app.callback(Output('duration_fig1','figure'), [Input("tabs", "active_tab")])
def switch_tab(at):
    return durationBar_chart(df,at)


# tabs year/month graph update
@app.callback(Output('year-month_fig','figure'), [Input("tabs_ym", "active_tab")])
def switch_tab_month_year(at):
    return new_scatter_line(df,at)

# year slider and rate dropdown list update
@app.callback(
    Output('pop_occupation', 'figure'),
    Output('pop_speaker', 'figure'),
    Output('pop_talk', 'figure'),
    Output('most_disscused_talk', 'figure'),

    Input('main_slider_id', 'value'),
    Input('dropDownId', 'value')
)
def update_graphs_Slider_drop(curr_year,dropDownList):

    if (curr_year is None) and (dropDownList is None):
        filterDf = df

    if (curr_year) and (dropDownList):
        print("\nboth")
        print(f"year = {curr_year}          dropdown = {dropDownList}")
        filterDf = df[(df.year == curr_year) & (df['name'].isin(dropDownList))]

    elif (curr_year) and (dropDownList is  None or dropDownList == []):
        print('\nslider')
        print(f"year = {curr_year}          dropdown = {dropDownList}")
        filterDf = df[df.year == curr_year]

    elif (curr_year is None) and (dropDownList):
        print('\ndropdown')
        print(f"year = {curr_year}          dropdown = {dropDownList}")
        filterDf = df[df['name'].isin(dropDownList)]


    pop_speaker = most_popular_speaker(filterDf)
    pop_occupation = most_popular_speaker_occupation(filterDf)
    pop_talk = mostPopularTalk(filterDf)
    most_disscution = popular_talk_pieChart(filterDf)

    return pop_occupation, pop_speaker, pop_talk, most_disscution


# main layout callbacks update
@app.callback(Output('tabs-main-container', 'children'),
              [Input('bigTabs', 'active_tab')])
def render_content(tab):
    if tab == 'analysis_Tab1_id':
        return analysis_container()
    elif tab == 'recommendation_Tab2_id':
        return recommendation_container()

# talk name dropdown in recommendation system update
@app.callback(Output("dataframe_id", "children"),
              Input('talk_dropDownId', 'value'))
def update_table(value):
    new_df = get_recommendation_based_title(value)
    return dbc.Table.from_dataframe(new_df, striped=True, bordered=True, hover=True)
