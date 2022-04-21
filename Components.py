from dash import  dcc
from dash import html
import dash_bootstrap_components as dbc
from run import app
from StaticCharts import mostPopularTalk, popular_talk_pieChart, most_popular_speaker

def mainTitle_desc():
    main_title = [
        html.Img(src=app.get_asset_url('TED_wordmark.svg.png'), style={'height': '25%', 'width': '100%'}),
        html.Hr(),
        html.H2('this is a dashboard for visualizing some analysis on ted talks dataset made by maryam and alaa', style={
            # 'color': '#d90000',
            'color': 'black',
            #"font-weight": "bold"
        })]
    return main_title


# def singleCard (): when alaa comes

def bigCards():
    card_group = dbc.CardGroup([
        dbc.Card([
            dbc.CardImg(src=app.get_asset_url("videoicon.jpg"),
                        style={"margin-left": "auto", "margin-right": "auto", "width": "30%"}),
            dbc.CardBody([
                html.H1("#10,000", className="card-title", style={"font-weight": "bold"}),
                html.Br(),
                html.P(
                    "Some quick example text to build on the card title and ",
                    className="card-text",
                )
            ], style={'text-align': 'center'},
            ),
        ],
        ),

        dbc.Card([
            dbc.CardImg(src=app.get_asset_url("microphone icon.jpg"),
                        style={"margin-left": "auto", "margin-right": "auto", "width": "30%"}),
            dbc.CardBody([
                html.H1("#10,000", className="card-title", style={"font-weight": "bold"}),
                html.Br(),
                html.P(
                    "Some quick example text to build on the card title and ",
                    className="card-text",
                )
            ], style={'text-align': 'center'},
            ),
        ],
        ),

        dbc.Card(
            [
                dbc.CardImg(src=app.get_asset_url("6851050_preview.png"),
                            style={"margin-left": "auto", "margin-right": "auto", "width": "30%"}),
                dbc.CardBody([
                    html.H1("#10,000", className="card-title", style={"font-weight": "bold"}),
                    html.Br(),
                    html.P(
                        "Some quick example text to build on the card title and ",
                        className="card-text",
                    )
                ], style={'text-align': 'center'},
                ),
            ],
        ),
    ])
    return card_group


def yearMonthCard():
    y_m_ChartCard = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H4("TED talks through months and years", className="card-title"),
                    html.Hr(),
                    html.P("This is some card text", className="card-text"),
                ]
            ),
        ],
        style={"height": '100%'},
    )
    return y_m_ChartCard


def wordCloud():
    img_card = dbc.Card(
        [
            dbc.CardBody(html.H4("Top TED searched tags", className="card-text")),
            html.Hr(),
            dbc.CardImg(src="/static/images/Picture1.png", bottom=True),
        ],
        style={ "height": '100%'},
     )
    return img_card

def mostPopTalk_card():
    talk_card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H4("Most popular TED talks", className="card-title"),
                    html.Hr(),
                    dcc.Graph(figure=mostPopularTalk(), responsive=True)  # style={"width": '140vh'},)
                ],
            ),
        ],
        style={ "height": '100%'},
    )
    return talk_card

def mostPopSpreaker_Card():
    speaker = dbc.Card(
        dbc.CardBody(
            [
                html.H4("Most popular TED speakers", className="card-title"),
                html.Hr(),
                dcc.Graph(figure=most_popular_speaker(), responsive=True)
            ]
        ),
        style={ "height": '100%'},
    )
    return speaker

def mostDiscussionTopic_card():
    dissc_topic = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H4("Top most attracted and discussed topics",
                            className="card-title"),
                    html.Hr(),
                    dcc.Graph(id='duration_fig', figure=popular_talk_pieChart(), responsive=True),
                ]
            ),
        ]
        , style={"height": '100%'}
    )
    return dissc_topic

def duration_card():
    duration =  dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("The most longest and shortest talks duration", className="card-title"),
                        html.Hr(),
                        dbc.Tabs(
                            [
                                dbc.Tab(label="Longest duration", tab_id="tab1_id"),
                                dbc.Tab(label="Shortest duration", tab_id="tab2_id"),
                            ],
                            id="tabs",
                            active_tab="tab1_id",
                        ),
                        dcc.Graph(id='duration_fig1', responsive=True),
                    ]
                ),
                style={"height": '100%'}
            )
    return duration

def talkOfFavSpeaker_card():
   fav = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H4("Finding TED talks of your favorite Author", className="card-title"),
                    html.Hr(),

                    create_linkCard(),
                ]
            ),
        ],
        # style={"width": "18rem", "margin-left": "15px", "margin-bottom": "15px", "margin-top": "15px", "height":350},
        # className="w-100",
   )
   return fav

def create_linkCard():
    card = dbc.Card(
        [
            dbc.CardImg(
                src="/static/images/featured_art_DuncanDavidsonTED.jpg",
                top=True,
                style={"opacity": 0.2},
            ),
            dbc.CardImgOverlay(
                dbc.CardBody(
                    [
                        html.H4("Card title", className="card-title"),
                        html.P(
                            "An example of using an image in the background of "
                            "a card.",
                            className="card-text",
                        ),
                    ],
                ),
            ),
        ],
        style={"width": "15%"},
    )
    return card
