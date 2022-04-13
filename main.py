import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime

# preprocessing
df = pd.read_csv("ted_main.csv")
print(df.head(1))

#get Data_set Information (Nulls , Numbers of Records , Data Types)
print(df.info())

# Count Null Values of each Column
print(df.isna().sum())

#preprocessing on data
df['Date'] = pd.to_datetime(df['published_date'], unit='s')
df.drop(columns = ['description','event', 'film_date', 'languages', 'name','num_speaker',
                   'published_date' , 'ratings', 'related_talks','speaker_occupation'], axis = 1 , inplace = True)
print(df.head(1))
print(df.info())
df["month"] = df['Date'].map(lambda x: x.month)
df["year"] = df['Date'].map(lambda x: x.year)
print(df.head(1))
df.drop('Date', inplace = True , axis =1)
print(df.head(20))
print(df.info())
df["tags"] = df["tags"].apply(eval)
tag_dict = pd.Series([x for _list in df.tags for x in _list]).value_counts()
print(tag_dict)


#################################Dashboard#############################################

app = dash.Dash(__name__ , external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.layout = html.Div([
    # row 1
    dbc.Row([
        dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.Img(src=app.get_asset_url('TED.png'), style={'height': '40%', 'width': '40%'})
                    ], width=4),
                    dbc.Col([
                        html.H1('TED TALKS DASHBOARD ', style={
                            'color': '#d90000',
                            'textAlign': 'center',
                            'font-size': '55px',
                            "font-weight": "bold"
                            }),

                    ], width=4),
                ], align='center'),
            ])),
        ], align='center'),

    # row 2
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src=app.get_asset_url("videoicon.jpg"),
                                style= {"margin-left": "auto", "margin-right": "auto" ,"width": "60%"}),
                    dbc.CardBody([
                        html.H1("#10,000", className="card-title", style = {"font-weight": "bold", 'font-size': '50px'}),
                        html.Br(),
                        html.H5(
                            "Some quick example text to build on the card title and ",
                            className="card-text",
                        )
                    ],style={'text-align': 'center'},
                    ),
                ],
                style={"width": "18rem", "margin-left": "15px", "margin-bottom": "15px", "height": 400},
            ),
        ], width=2),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.P("This is some card text", className="card-text"),
                        ]
                    ),
                ],
                style={"width": "18rem","height":400},className="w-100",
            )
        ], width=6),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("chart2", className="card-title"),
                        html.H6("Card subtitle", className="card-subtitle"),
                    ]
                ),
                style={"width": "18rem", "height":400},className="w-100",
            )
        ], width=4),
    ],style={"margin-top": "20px","margin-right": "15px"},),

    # row 3
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src=app.get_asset_url("microphone icon.jpg"),
                                style= {"margin-left": "auto", "margin-right": "auto" ,"width": "60%"}),
                    dbc.CardBody([
                        html.H1("#10,000", className="card-title", style = {"font-weight": "bold", 'font-size': '50px'}),
                        html.Br(),
                        html.H5(
                            "Some quick example text to build on the card title and ",
                            className="card-text",
                        )
                    ],style={'text-align': 'center'},
                    ),
                ],
                style={"width": "18rem", "margin-left": "15px", "margin-bottom": "15px", "height": 400},
            ),
        ], width=2),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.P("This is some card text", className="card-text"),
                        ]
                    ),
                ],
                style={"width": "18rem", "height": 400}, className="w-100",
            )
        ], width=5),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("chart2", className="card-title"),
                        html.H6("Card subtitle", className="card-subtitle"),
                    ]
                ),
                style={"width": "18rem", "height": 400}, className="w-100",
            )
        ], width=5),
    ], style={"margin-top": "20px","margin-right": "15px"}),
    # row 4
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src=app.get_asset_url("6851050_preview.png"),
                                style= {"margin-left": "auto", "margin-right": "auto" ,"width": "60%"}),
                    dbc.CardBody([
                        html.H1("#10,000", className="card-title", style = {"font-weight": "bold", 'font-size': '50px'}),
                        html.Br(),
                        html.H5(
                            "Some quick example text to build on the card title and ",
                            className="card-text",
                        )
                    ],style={'text-align': 'center'},
                    ),
                ],
                style={"width": "18rem", "margin-left": "15px", "margin-bottom": "15px", "height": 400},
            ),
        ], width=2),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.P("This is some card text", className="card-text"),
                        ]
                    ),
                ],
                style={"width": "18rem", "height": 400}, className="w-100",
            )
        ], width=5),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("chart2", className="card-title"),
                        html.H6("Card subtitle", className="card-subtitle"),
                    ]
                ),
                style={"width": "18rem", "height": 400}, className="w-100",
            )
        ], width=5),
    ], style={"margin-top": "20px","margin-right": "15px"}),
    # row 5
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("last card", className="card-title"),
                            html.P(
                                "Some quick example text to build on the card title and ",
                                className="card-text",
                            )
                        ]
                    ),
                ],
                style={"width": "18rem", "margin-left": "15px", "margin-bottom": "15px", "margin-top": "15px", "height":350},
                className="w-100",
            ),
        ], width=12),
    ],style={"margin-right": "15px"}),

])



app.run_server(debug = True)