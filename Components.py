from dash import  dcc
from dash import html
import dash_bootstrap_components as dbc
from run import app
from StaticCharts import mostPopularTalk, popular_talk_pieChart, most_popular_speaker, most_popular_speaker_occupation
from dataPreperation import get_dataFrame

df = get_dataFrame()

red_color = '#b22222' #'#800000'
config = {'displayModeBar': False, 'autosizable': False, 'responsive': True}

def mainTitle_desc():
    main_title = [
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url('t.png'),width=90),width = 3), #style={'height': '45%', 'width': '35%'}
            dbc.Col(
                html.H1('TED ideas worth spreading',
                    style={'color': red_color,"font-weight": "bold" , 'margin-top': '6%','margin-left': '-55px'})
                ,width = 7)
             ],justify='start', className="g-0"),
        html.Hr(),
        html.P('Ted is a nonprofit devoted to spreading ideas,'
                ' in the form of short, powerful talks.'
                ' Ted began in 1984 as a conference where Technology, Entertainment and Design converged,'
                ' and today covers almost all topics from science to business to global issues in more'
                ' than 100 languages. Meanwhile, independently run TEDx events help share ideas in communities'
                ' around the world.', style={
            'color': 'black',
            'font-size': '12',
            #"font-weight": "bold"
        })]
    return main_title


# def singleCard (): when alaa comes

def bigCards():
    card_group = dbc.CardGroup([
        dbc.Card([
            dbc.CardImg(src=app.get_asset_url("talk.png"),
                        style={"margin-left": "auto", "margin-right": "auto", "width": "30%"}),
            dbc.CardBody([
                html.H1('{:,}'.format(df["title"].count()), className="card-title", style={"font-weight": "bold"}),
                html.Br(),
                html.H4(
                    "NUMBER OF TALKS",
                    className="card-text",
                    #style={'margin-top': '15%'}
                )
            ], style={'text-align': 'center','padding':'15%','color':'white','background-color':red_color},
            ),
        ],
        ),

        dbc.Card([
            dbc.CardImg(src=app.get_asset_url("eye1.png"),
                        style={"margin-left": "auto", "margin-right": "auto", "width": "30%"}),
            dbc.CardBody([
                html.H1('{:,}'.format(df["views"].sum()), className="card-title", style={"font-weight": "bold"}),
                html.H4("NUMBER OF VIEWS")
            ], style={'text-align': 'center','padding':'10%','color':'white','background-color':red_color},
            ),
        ],
        ),

        dbc.Card(
            [
                dbc.CardImg(src=app.get_asset_url("p1.png"),
                            style={"margin-left": "auto", "margin-right": "auto", "width": "30%"}),
                dbc.CardBody([
                    html.H1('{:,}'.format(df['main_speaker'].nunique()), className="card-title", style={"font-weight": "bold"}),
                    html.Br(),
                    html.H4("NUMBER OF SPEAKERS")
                ], style={'text-align': 'center','padding':'15%','color':'white','background-color':red_color},
                ),
            ],
        ),
    ])
    return card_group


def yearMonthCard():
    y_m_ChartCard = [
        html.H4("TED talks through months and years", className="card-title"),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(label="Year-Wise", tab_id="year_id"),
                dbc.Tab(label="Month-Wise", tab_id="month_id"),
            ],
            id="tabs_ym",
            active_tab="year_id",
        ),
        dcc.Graph(id='year-month_fig')
    ]

    return y_m_ChartCard

##### still ++++++++++++++++
def wordCloud():
    img_card = [
            html.H4("Top TED searched tags", className="card-text"),
            html.Hr(),
            html.Br(),html.Br(),
            html.Img(src=app.get_asset_url("pic.jpg"),
                        style={"margin-left": "auto", "margin-right": "-50%"})
        ]
        #style={ "height": '100%'},

    return img_card

def mostPopTalk_card():
   talk_card =  [
                    html.H4("Most Popular TED Talks", className="card-title"),
                    html.Hr(),
                    #dcc.Graph(figure=mostPopularTalk(), responsive=True)  # style={"width": '140vh'},)
                    drawFigure(id= 'pop_talk',figure=mostPopularTalk()),
                ]
   return talk_card

def mostPopSpreaker_Card():

      speaker=[
                html.H4("Most Popular TED Speakers", className="card-title"),
                html.Hr(),
                #dcc.Graph(figure=most_popular_speaker(), responsive=True)
                drawFigure(id= 'pop_speaker',figure=most_popular_speaker()),

      ]
      return speaker

def most_popular_occupation():
    occupation = [
        html.H4("Most Popular Speakers Occupations", className="card-title"),
        html.Hr(),
        # dcc.Graph(figure=most_popular_speaker(), responsive=True)
        drawFigure(id='pop_occupation', figure=most_popular_speaker_occupation()),

    ]
    return occupation

def mostDiscussionTopic():
    dissc_topic= [
                    html.H4("Top most attracted and discussed topics",
                            className="card-title"),
                    html.Hr(),
                    drawFigure(id='duration_fig',figure=popular_talk_pieChart()),
                    #dcc.Graph(id='duration_fig', figure=popular_talk_pieChart(), responsive=True),
                ]
    return dissc_topic

def duration_card():
    duration =  [
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
                dcc.Graph(id='duration_fig1', responsive=True, config=config, style={'height':'100%'}),
            ]
    return duration

def talkOfFavSpeaker_card():
   fav =  [
            html.H4("Finding TED talks of your favorite Author", className="card-title"),
            html.Hr(),
         ]
   return fav

# Draw figure Function
def drawFigure(figure=None, id=None, config={'displayModeBar': False, 'autosizable':False, 'responsive':True}):
    return dcc.Graph(
                    id=id,
                    figure=figure.update_layout(
                        template     = 'simple_white',
                        #plot_bgcolor = 'rgba(0, 0, 0, 0)',
                        #paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        #autosize=True,
                        margin=dict(l=20, r=20, t=20, b=20),

                    ),
                    config=config,
                    style={'background-color':'white','height':'100%'} ## want the graph background to be transperent
                )