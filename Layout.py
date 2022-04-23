from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from Components import *
#from run import app
import Callback


app.layout = dbc.Container([

    ### row 1 cards of big number  ================================================================================
    dbc.Row([
        dbc.Col(mainTitle_desc(), width=6),
        dbc.Col([bigCards()], width=5 ),

        ], justify='evenly'),
    html.Br(),
    # row 2 ==================================================================================================
    dbc.Row([
        dbc.Col(yearMonthCard(), width=11, className="card"),

    ],justify='evenly'),# style={"margin-top": "2%"}),
    html.Br(),
    # slider row 3=============================================================================================
    dbc.Row([
        dbc.Col(main_years_slider() , width=12, className="card"),

    ],justify='around'),# style={"margin-top": "2%"}),
    html.Br(),
    # row 4 ==================================================================================================
    dbc.Row([
        dbc.Col(mostPopTalk_card(), width=6, className="card"),
        dbc.Col(mostDiscussionTopic(), width=5, className="card"),

    ],justify='evenly'),
    html.Br(),#style={"margin-top": "2%","margin-left": "15px", 'layout.autosize': 'true'}, ),  # style={"margin-top": "20px","margin-right": "15px"},),
    # row 5 ==================================================================================================
    dbc.Row([
        dbc.Col(most_popular_occupation(), width=6, className="card"),
        dbc.Col(mostPopSpreaker_Card(), width=5, className="card"),

    ],justify='evenly'),# style={"margin-top": "2%","margin-left": "15px"}),  # style={"margin-top": "20px","margin-right": "15px"}),
    html.Br(),
    # row 6 ==================================================================================================
    dbc.Row([
        dbc.Col(duration_card(), width=6, className="card"),
        dbc.Col(wordCloud(), width=5, className="card"),

    ], justify='evenly')

], #style = {'background-image':"url('https://media.istockphoto.com/vectors/white-brick-wall-textured-background-vector-id1094376824?k=20&m=1094376824&s=612x612&w=0&h=X2573vpqJFd9F_sqFN9Xb-fKhe88ZpPLuYta4srrLQI=')" })
style = {# 'background-image':"url('https://encrypted-tbn0.gstatic.com/images?q=tbn
    # :ANd9GcStzFM4eqUXlfeLkXO_C32jljkxMUl3wlH53Ywmx1368KNbLVcSjfuVfcYm-FkC1zi55V8&usqp=CAU')"
         'backgroundColor' : '#ECECEC',
         "padding-top": "2%", "padding-left": "2%","padding-right": "2%", "padding-bottom":'2%'
         }, fluid= True)
#app.run_server(port=5080)
#style = {'backgroundColor':'#FAFAFA'})
if __name__ == '__main__':
    app.run_server(port=5050,debug=True)