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
        dbc.Col(mainTitle_desc(), width=5),
        dbc.Col([bigCards()], width=7),

        ], justify='around', style={"margin-top": "2%", "margin-left": "2%","margin-right": "1.5%"}),

    # row 2 ==================================================================================================
    dbc.Row([
        dbc.Col([yearMonthCard()], width=8),
        dbc.Col([wordCloud()], width=3),

    ], justify='around', style={"margin-top": "2%"}),

    # row 3 ==================================================================================================
    dbc.Row([

        dbc.Col([mostPopTalk_card()], width=6),
        dbc.Col([mostPopSpreaker_Card()], width=5),

    ], justify='around', style={"margin-top": "2%"}),  # style={"margin-top": "20px","margin-right": "15px"}),
    # row 4 ==================================================================================================
    dbc.Row([
        dbc.Col([mostDiscussionTopic_card()], width=5),
        dbc.Col([duration_card()], width=6),
    ], justify='around', style={"margin-top": "2%"}),  # style={"margin-top": "20px","margin-right": "15px"},),

    # row 5 ==================================================================================================
    dbc.Row([
        dbc.Col([talkOfFavSpeaker_card()], width=12, align="end"),
    ], style={"margin-top": "2%", "margin-right": "1.5%", "margin-left": "1.5%"}),  # style={"margin-right": "15px"}, ),

])
#app.run_server(port=5080)
if __name__ == '__main__':
    app.run_server(port=5050,debug=True)