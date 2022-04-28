from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from Components import *
import Callback

app.layout = dbc.Container([

    # row 1 cards of big number  and title  ======================================================
    dbc.Row([
        dbc.Col(mainTitle_desc(), width=7),
        dbc.Col([bigCards()], width=5),

        ], justify='evenly'),
    html.Br(),
    # row 2 tabs for chosing the container layout ==================================================
    dbc.Row([
        dbc.Col([
            dbc.Tabs(
                    [
                        dbc.Tab(label="Analysis", tab_id="analysis_Tab1_id"),

                        dbc.Tab(label="Recommendation", tab_id="recommendation_Tab2_id"),
                    ],
                    id="bigTabs",
                    active_tab="analysis_Tab1_id",
                ),
                html.Div(id='tabs-main-container'),
                ]),
            ])
    ],
    style = {
             'backgroundColor' : '#ECECEC',
             "padding-top": "2%","padding-left": "2%","padding-right": "2%", "padding-bottom":'2%'
             }, fluid= True)

if __name__ == '__main__':
    app.run_server(port=5050,debug=True)