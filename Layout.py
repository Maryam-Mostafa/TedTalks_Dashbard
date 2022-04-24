from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from Components import *
import Callback


app.layout = dbc.Container([

    # row 1 cards of big number  ================================================================================
    dbc.Row([
        dbc.Col(mainTitle_desc(), width=8),
        dbc.Col([bigCards()], width=4),

        ], justify='evenly'),
    html.Br(),

    # row 2 slider and drop down =============================================================================================
    dbc.Row([
        dbc.Col(filters(), width=12, className="card"),

    ],justify='around'),
    html.Br(),

    # row 3 ==================================================================================================
    dbc.Row([
        dbc.Col(graphes1(), width=6),
        dbc.Col(graphes2(), width=6),

    ],justify='evenly', className='div'),
    html.Br(),

    # row 4 ==================================================================================================
    dbc.Row([
        dbc.Col(wordCloud(), width=4,),
        dbc.Col(duration_card(), width=8),

    ]),
    html.Br(),

    # row 5 ==================================================================================================
    dbc.Row([
        dbc.Col(yearMonthCard(), width=12),
    ]),
],
style = {
         'backgroundColor' : '#ECECEC',
         "padding-top": "2%","padding-left": "2%","padding-right": "2%", "padding-bottom":'2%'
         }, fluid= True)

if __name__ == '__main__':
    app.run_server(port=5050,debug=True)