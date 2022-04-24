from dash.dependencies import Output, Input, State
import plotly.express as px
import dash
from run import app
from dataPreperation import get_dataFrame
import pandas as pd
from StaticCharts import *

#get dataset in a variable
df = get_dataFrame()


# tabs duration graph update
@app.callback(Output('duration_fig1','figure'), [Input("tabs", "active_tab")])
def switch_tab(at):
    return durationBar_chart(df,at)


# tabs year/month graph update
@app.callback(Output('year-month_fig','figure'), [Input("tabs_ym", "active_tab")])
def switch_tab_month_year(at):
    return new_scatter_line(df,at)
############################################### all the above is ggood *********************
# # updating graph by slider only
# @app.callback(
#     Output('pop_occupation', 'figure'),
#     Output('pop_speaker', 'figure'),
#     Output('pop_talk', 'figure'),
#     Output('most_disscused_talk', 'figure'),
#
#     Input('main_slider_id', 'value')
# )
# def update_graphs_bySlider(curr_year):
#
#     filterDf = df[df.year == curr_year]
#
#     pop_speaker = most_popular_speaker(filterDf)
#     pop_occupation = most_popular_speaker_occupation(filterDf)
#     pop_talk = mostPopularTalk(filterDf)
#     most_disscution = popular_talk_pieChart(filterDf)
#
#     return pop_occupation, pop_speaker, pop_talk, most_disscution
#
# # updating graph by dropdown only
# @app.callback(
#     Output('pop_occupation', 'figure'),
#     Output('pop_speaker', 'figure'),
#     Output('pop_talk', 'figure'),
#     Output('most_disscused_talk', 'figure'),
#
#     Input('dropDownId', 'value'),
# )
# def update_graphs_byDropDown(dropDownList):
#
#     filterDf = df[df['name'].isin(dropDownList)]
#
#     pop_speaker = most_popular_speaker(filterDf)
#     pop_occupation = most_popular_speaker_occupation(filterDf)
#     pop_talk = mostPopularTalk(filterDf)
#     most_disscution = popular_talk_pieChart(filterDf)
#
#     return pop_occupation, pop_speaker, pop_talk, most_disscution


#triggerList = []
@app.callback(

    Output('pop_occupation', 'figure'),
    Output('pop_speaker', 'figure'),
    Output('pop_talk', 'figure'),
    Output('most_disscused_talk', 'figure'),

    # State('main_slider_id', 'value'),
    # State('dropDownId', 'value'),

    Input('main_slider_id', 'value'),
    Input('dropDownId', 'value')

    #Input('buttonID','n_clicks')
)
# بصي دا شغال بس بيبوظ لما افضي الليسته و اجي اغير بقى السنة مبيحصلش تغيير بقى
def update_graphs_Slider_drop(curr_year,dropDownList):
    # ctx = dash.callback_context
    # input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    # pre_id = ''
    # #print(ctx.triggered)
    # if not ctx.triggered:
    #     filterDf = df
    #     print(f'\n**************  no filters *****************\n'
    #           f'current trigger : {input_id}\nlist of trigger:{triggerList}\n'
    #           f' ____________________________________________\n')
    #
    # if input_id == 'main_slider_id' and pre_id == '':
    #     triggerList.append(input_id)
    #     pre_id = triggerList[-2] if len(triggerList) >= 2 else  triggerList[-1]
    #     filterDf = df[df.year == curr_year]
    #     print(f'**************  just slider *****************\n'
    #           f'current trigger : {input_id}\npre trigger:{triggerList}\n ____________________________________________\n')
    #
    #
    #
    # if input_id == 'dropDownId':
    #     triggerList.append(input_id)
    #
    #     if pre_id == '':
    #         filterDf = df[df['name'].isin(dropDownList)]
    #         print(f'**************  just drop down *****************\n'
    #               f'current trigger : {input_id}\npre trigger:{triggerList}\n ____________________________________________\n')
    #
    #
    #     if dropDownList == []:
    #         if pre_id != '':
    #         #triggerList.append(input_id)
    #             print(f'************** slider as drop empty *****************\n'
    #                   f'current trigger : {input_id}\nlist of trigger:{triggerList}\n ____________________________________________\n')
    #             input_id = 'main_slider_id'
    #             filterDf = df[df.year == curr_year]
    #
    #         else: filterDf = df
    #
    #     pre_id = triggerList[-2] if len(triggerList) >= 2 else  triggerList[-1]
    #
    # if (input_id == 'dropDownId' and pre_id == 'main_slider_id') or (input_id == 'main_slider_id' and pre_id == 'dropDownId' and dropDownList!=''):
    #     triggerList.append(input_id)
    #     pre_id = triggerList[-2] if len(triggerList) >= 2 else triggerList[-1]
    #     filterDf = df[(df.year == curr_year) & (df['name'].isin(dropDownList))]
    #     print(f'**************  both slider and dropdown *****************\n'
    #           f'current trigger : {input_id}\nlist of trigger:{triggerList}\n ____________________________________________\n')

    if (curr_year is None) and (dropDownList is None):
        filterDf = df

    if (curr_year) and (dropDownList):
        print("\nboth")
        print(f"year = {curr_year}          dropdown = {dropDownList}")
        filterDf = df[(df.year == curr_year) & (df['name'].isin(dropDownList))]

    elif (curr_year) and (dropDownList is  None):
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
