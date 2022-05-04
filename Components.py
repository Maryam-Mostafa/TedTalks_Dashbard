from dash import  dcc
from dash import html
import dash_bootstrap_components as dbc
from run import app
from StaticCharts import mostPopularTalk, popular_talk_pieChart, most_popular_speaker, most_popular_speaker_occupation
from dataPreperation import get_dataFrame

# preparing dataframe to be used
df = get_dataFrame()

# some global varibales
red_color = '#9b1422'
config = {'displayModeBar': False, 'autosizable': False}

# main title components
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

# big cards number component
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

################################################################################################
#                                    analysis components in layout                             #
################################################################################################

# year/month figure with tabs
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

# creating word cloud and call it but, we are not calling it as we already did and have the img
def wordCloud():
    img_card = html.Div([
            html.H4("Top TED searched tags", className="card-text"),
            html.Hr(),
            html.Img(src=app.get_asset_url("Finalwc.png"),style={'height':'100%', 'width':'100%'}, className='shadow')
        ])
    return img_card

# most popular talk figure card
def mostPopTalk_card():
   talk_card =  [
                    html.H4("Most Popular TED Talks", className="card-title"),
                    html.Hr(),
                    dcc.Graph(id='pop_talk', config=config, className='shadow'),
                ]
   return talk_card

# most popular speaker figure card
def mostPopSpreaker_Card():
      speaker=[
                html.H4("Most Popular TED Speakers", className="card-title"),
                html.Hr(),
                dcc.Graph(id='pop_speaker', config=config, className='shadow')
      ]
      return speaker

# most popular speaker occupation figure card
def most_popular_occupation():
    occupation = [
        html.H4("Most Popular Occupations", className="card-title"),
        html.Hr(),
        dcc.Graph(id='pop_occupation', config=config, className='shadow')

    ]
    return occupation

# most disscused and argued talk figure based on comments card
def mostDiscussionTopic():
    dissc_topic= [
                    html.H4("Top most discussed topics",
                            className="card-title"),
                    html.Hr(),
                    dcc.Graph(id='most_disscused_talk', config=config, className='shadow')
                ]
    return dissc_topic

# duration longest and shortest and tabs figure card
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
                dcc.Graph(id='duration_fig1', config=config, className='shadow', style={'height':'57vh'})
            ]
    return duration

# year slider with title
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


# rate type dropdown with title
def dropDown():
    drop = [
        html.H6("Rate type", className="me-1"),
        html.Br(),
        dcc.Dropdown(id = 'dropDownId',
                  options = [{'label': str(rate_type), 'value':str(rate_type)} for rate_type in df['name'].unique()],
                  value = None,
                  placeholder = 'Choose rate types...',
                  multi = True,
                  className = 'dropdown',
                 ),
        html.Br()]
    return drop

# combine the above 2 filters in one a row
def filters():
    row = dbc.Row([
        dbc.Col(main_years_slider(), width=8),
        dbc.Col(dropDown(), width=3),
    ],justify="evenly",)
    return row


# combine most_popular_occupation and mostPopSpreaker_Card in one a row
def graphes1():
    row = dbc.Row([
        dbc.Col(most_popular_occupation(), width=6),
        dbc.Col(mostPopSpreaker_Card(), width=6),

    ])
    return row

# combine mostPopTalk_card and mostDiscussionTopic in a row
def graphes2():
    row = dbc.Row([
        dbc.Col(mostPopTalk_card(), width=6),
        dbc.Col(mostDiscussionTopic(), width=6),

    ])
    return row

# merging all above elemnets in a big container for the analysis
def analysis_container():
     analysis = dbc.Container([
                # row 1: filters ==================================================
                dbc.Row([
                    dbc.Col(filters(), width=12, className="card"),
                ]),
                html.Br(),

                # row 2: the 4 graphs merging then here in 2 cols ====================
                dbc.Row([
                    dbc.Col(graphes1(), width=6),
                    dbc.Col(graphes2(), width=6),

                ],justify='evenly', className='div'),
                html.Br(),

                # row 3: wordcloud and duration =======================================
                dbc.Row([
                    dbc.Col(wordCloud(), width=4,),
                    dbc.Col(duration_card(), width=8),

                ]),
                html.Br(),

                # row 4: last graph in analysis talks count throw year/month ============
                dbc.Row([
                    dbc.Col(yearMonthCard(), width=12),
                ])
         ],style={
                   'backgroundColor': '#ECECEC',
                   "padding-top": "2%", "padding-left": "2%", "padding-right": "2%",
                   "padding-bottom": '2%'
               }, fluid=True)

     return analysis

################################################################################################
#                              recommendation components in layout                             #
################################################################################################

# dropdown of talk names
def talk_dropDown():
    drop = dcc.Dropdown(id = 'talk_dropDownId',
                  options = [{'label': str(talk), 'value':str(talk)} for talk in df['title'].unique()],
                  value = 'Do schools kill creativity?',
                  placeholder = 'Choose talk...',
                  multi = False,
                  className = 'dropdown',
                  style= {'width':'400px'}
                 )
    return drop

# merging the above elemnet in the big container for the recommendation
def recommendation_container():
        analysis = dbc.Container([
            # row 1: containg the title, and the dropdown list  =========================
            dbc.Row(
                dbc.Col(
                    # we make this to have the title and the dropdown alighned horizontally as col of a row
                    dbc.Row([
                            dbc.Col([html.H2('Recommending Talks based on similar other talk')], width=7),
                            dbc.Col(talk_dropDown(), width=4),
             ], justify='evenly'),className='card', style=
                    {"padding-top": "2%", "padding-left": "2%", "padding-right": "2%", "padding-bottom": '2%'})
            ),
            html.Br(),
            # row 2: data table that will have the result  =========================
            dbc.Row([
                dbc.Col(dbc.Table(id='dataframe_id'), width=12, className="card")
            ])

        ],style={
                   'backgroundColor': '#ECECEC',
                   "padding-top": "2%", "padding-left": "2%", "padding-right": "2%",
                   "padding-bottom": '2%'
               }, fluid=True)

        return analysis