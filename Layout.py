from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from Components import *
#from run import app
import Callback

app.layout = html.Div([

    ### row 1 cards of big number  ================================================================================
    dbc.Row([
        dbc.Col(mainTitle_desc(), width=6),
        dbc.Col([bigCards()], width=6),

        ], justify='center', style={"margin-top": "2%", "margin-left": "2%","margin-right": "1.5%"}),

    # row 2 ==================================================================================================
    dbc.Row([
        dbc.Col(yearMonthCard(), width=12),

    ], justify='around', style={"margin-top": "2%"}),

    # row 4 ==================================================================================================
    dbc.Row([
        dbc.Col(mostPopTalk_card(), width=4),
        dbc.Col(mostPopSpreaker_Card(), width=4),
    ], align='center', style={"margin-top": "2%","margin-left": "15px", 'layout.autosize': 'true'}, ),  # style={"margin-top": "20px","margin-right": "15px"},),
    # row 3 ==================================================================================================
    dbc.Row([

        dbc.Col(mostDiscussionTopic(), width=4),
        dbc.Col(duration_card(), width=4),
        dbc.Col(wordCloud(), width=4),


    ], align='center', style={"margin-top": "2%","margin-left": "15px"}),  # style={"margin-top": "20px","margin-right": "15px"}),

    # row 5 ==================================================================================================
    # dbc.Row([
    #     dbc.Col([talkOfFavSpeaker_card()], width=12, align="end"),
    # ], style={"margin-top": "2%", "margin-right": "1.5%", "margin-left": "1.5%"}),  # style={"margin-right": "15px"}, ),

], #style = {'background-image':"url('https://media.istockphoto.com/vectors/white-brick-wall-textured-background-vector-id1094376824?k=20&m=1094376824&s=612x612&w=0&h=X2573vpqJFd9F_sqFN9Xb-fKhe88ZpPLuYta4srrLQI=')" })
style = {#'background-image':"url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStzFM4eqUXlfeLkXO_C32jljkxMUl3wlH53Ywmx1368KNbLVcSjfuVfcYm-FkC1zi55V8&usqp=CAU')"
         'backgroundColor' : '#ECECEC'

         })
#app.run_server(port=5080)
#style = {'backgroundColor':'#FAFAFA'})
if __name__ == '__main__':
    app.run_server(port=5050,debug=True)