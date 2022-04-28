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
    title = dbc.CardGroup([
        html.Img(src=app.get_asset_url('t.png'),style={ "width": "10%", "height": "10%", "margin-right":"3px"}),
        html.H1('TED',style={'color': red_color,"font-weight": "900" ,"font-family":"Helvetica",'font-size':'100px', 'margin-top': '3%'}),
        html.H3('ideas worth spreading',
                style={'color': 'black', "font-weight": "bold", "font-family": "Helvetica",'margin-top': '10%'}),
        ])
    main_title = [ title,
                   html.Hr(),
                   html.P('Ted is a nonprofit devoted to spreading ideas,'
                          ' in the form of short, powerful talks.'
                          ' Ted began in 1984 as a conference where Technology, Entertainment and Design converged,'
                          ' and today covers almost all topics from science to business to global issues in more'
                          ' than 100 languages. Meanwhile, independently run TEDx events help share ideas in communities'
                          ' around the world.', style={
                       'color': 'black',
                       'font-size': '12', }
                          )
                      ]
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
                dcc.Graph(id='duration_fig1', config=config, className='shadow', style={'height':'59vh'})
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

def dropDown(): # rate type dropdown
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

def analysis_container():
     analysis = dbc.Container([
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
                ])
         ],style={
                   'backgroundColor': '#ECECEC',
                   "padding-top": "2%", "padding-left": "2%", "padding-right": "2%",
                   "padding-bottom": '2%'
               }, fluid=True)

     return analysis

##################################### recommendation components for layout ######################################

def talk_dropDown():
    drop = dcc.Dropdown(id = 'talk_dropDownId',
                  options = [{'label': str(talk), 'value':str(talk)} for talk in df['title'].unique()],
                  value = 'Do schools kill creativity?',
                  placeholder = 'Choose talk...',
                  multi = False,
                  className = 'dropdown',
                  style= {'width':'600px'}
                 )
    return drop
def recommendation_container():
        # dbc.Container([
        # row 2 slider and drop down =============================================================================================
        analysis = dbc.Container([
            dbc.Row(
                dbc.Col(
                    dbc.Row([
                    dbc.Col([html.H1('Recommending Talks based on similar other talk')], width=7),
                    dbc.Col(talk_dropDown(), width=5),
             ]),width = 12,className='card', style=
                    {"padding-top": "2%", "padding-left": "2%", "padding-right": "2%",
                   "padding-bottom": '2%'})
            ),
            html.Br(),
            dbc.Row([
                dbc.Col(dbc.Table(id='dataframe_id'), width=12, className="card")
            ])

        ],style={
                   'backgroundColor': '#ECECEC',
                   "padding-top": "2%", "padding-left": "2%", "padding-right": "2%",
                   "padding-bottom": '2%'
               }, fluid=True)


        return analysis