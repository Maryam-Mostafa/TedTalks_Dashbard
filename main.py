import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime

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

app = dash.Dash(__name__ , external_stylesheets=[dbc.themes.BOOTSTRAP]
                )
app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Img(src=app.get_asset_url('TED.png'), style={'height': '40%', 'width': '40%'})
                ], width=4),
                dbc.Col([
                    html.H1('Ted Talks Dashboard ', style={
                        'color': 'red',
                        'textAlign': 'center'}),

                ], width=4),
            ], align='center'),


        ])

    ),
    dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url("videoicon.jpg"), style={'height': '30%', 'width': '30%','text-align': 'center'},top=True),
        dbc.CardBody([
                html.H4("# 10,000", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and ",
                    className="card-text",
                )
            ]
        ),
    ],
    style={"width": "18rem"},
),

 dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url("microphone icon.jpg"), style={'height': '30%', 'width': '30%'},top=True),
        dbc.CardBody(
            [
                html.H4("# 10,989", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and ",
                    className="card-text",
                )
            ]
        ),
    ],
    style={"width": "18rem"},
),
dbc.Card(
    [
        dbc.CardImg(src=app.get_asset_url("6851050_preview.png"), style={'height': '20%', 'width': '20%','text-align': 'center' },top=True),
        dbc.CardBody(
            [
                html.H4("# 55,387", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and",
                    className="card-text",
                )
            ]
        ),
    ],
    style={"width": "18rem"},
)
])



app.run_server()