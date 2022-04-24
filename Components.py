from dash import  dcc
from dash import html
import dash_bootstrap_components as dbc
from run import app
from StaticCharts import mostPopularTalk, popular_talk_pieChart, most_popular_speaker, most_popular_speaker_occupation
from dataPreperation import get_dataFrame

df = get_dataFrame()

red_color = '#9b1422'

config = {'displayModeBar': False, 'autosizable': False}

def mainTitle_desc():
    main_title = [
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url('t.png'),width=90),width = 3),
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
        })]
    return main_title

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
        dbc.Tabs(
            [
                dbc.Tab(label="Year-Wise", tab_id="year_id"),
                dbc.Tab(label="Month-Wise", tab_id="month_id"),
            ],
            id="tabs_ym",
            active_tab="year_id",
        ),
        dcc.Graph(id='year-month_fig', className="shadow")
    ]
    return y_m_ChartCard


def wordCloud():
    img_card = html.Div([
            html.H4("Top TED searched tags", className="card-text"),
            html.Hr(),
            html.Img(src=app.get_asset_url("finalwc.png"),style={'height':'100%', 'width':'100%'}, className='shadow')
        ])
    return img_card

def mostPopTalk_card():
   talk_card =  [
                    html.H4("Most Popular TED Talks", className="card-title"),
                    html.Hr(),
                    dcc.Graph(id='pop_talk', config=config, className='shadow'),
                ]
   return talk_card

def mostPopSpreaker_Card():
      speaker=[
                html.H4("Most Popular TED Speakers", className="card-title"),
                html.Hr(),
                dcc.Graph(id='pop_speaker', config=config, className='shadow')
      ]
      return speaker

def most_popular_occupation():
    occupation = [
        html.H4("Most Popular Speakers Occupations", className="card-title"),
        html.Hr(),
        dcc.Graph(id='pop_occupation', config=config, className='shadow')

    ]
    return occupation

def mostDiscussionTopic():
    dissc_topic= [
                    html.H4("Top most discussed topics",
                            className="card-title"),
                    html.Hr(),
                    dcc.Graph(id='most_disscused_talk', config=config, className='shadow')
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
                dcc.Graph(id='duration_fig1', config=config, className='shadow', style={'height':'62vh'})
            ]
    return duration


def main_years_slider():
   slider = [
       html.H6("Select a year", className="me-1"),
       html.Br(),
        dcc.Slider(
            df['year'].min(),
            df['year'].max(),
            id='main_slider_id',
            step=None,
            value=None,
            marks={str(i): str(i) for i in df['year'].unique()}
                   ), html.Br()
        ]
   return slider

def dropDown():
    drop = [
        html.H6("Rate type", className="me-1"),
        html.Br(),
        dcc.Dropdown(id = 'dropDownId',
                  options = [{'label': str(rate_type), 'value':str(rate_type)} for rate_type in df['name'].unique()],
                  value = None,
                  placeholder = 'Choose rate types...',
                  multi = True,
                  className = 'dropdown'
                 ),
        html.Br()]
    return drop

def filters():
    row = dbc.Row([
        dbc.Col(main_years_slider(), width=8),
        dbc.Col(dropDown(), width=4),
        #dbc.Col(button(),width=1, )

    ], justify='evenly')
    return row

def graphes1():
    row = dbc.Row([
        dbc.Col(most_popular_occupation(), width=6),
        dbc.Col(mostPopSpreaker_Card(), width=6),

    ],justify='evenly')
    return row

def graphes2():
    row = dbc.Row([
        dbc.Col(mostPopTalk_card(), width=6),
        dbc.Col(mostDiscussionTopic(), width=6),

    ],justify='evenly')
    return row

def button():
    return [html.Br(),
            html.Br(),
            dbc.Button(id='buttonID', children='Result',
            n_clicks=0,outline=True, className="me-1",
                       style = {'background-color': '#9b1422',
                      'color': 'white',
                      'height': '50px',
                      'width': '100px',})]
