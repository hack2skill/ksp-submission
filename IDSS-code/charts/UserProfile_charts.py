import dash_bootstrap_components as dbc
from dash import dcc, html

plot_style_dimensions = {"width": "100%", "height": "62vh"}


class UserProfile:
    def __init__(self):
        self.icon_style = {
            "text-align": "center",
            "background": "#ffffff",
            "color": "#76aa60",
            "border-color": "#76aa60",
            "background-color": "white",
            "font-size": "15px",
            "font-weight": "bold",
            "border-radius": "50%",
        }

    def user_profile_tab(self):
        chartContent = dbc.Container([
            dbc.Container([
                html.H3('POI Information'),
                html.Hr(),
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Photograph:'),
                        html.Br(),
                    ], md=2),

                    dbc.Col([
                        dbc.Label(id='userphoto', className='text-success'),
                        html.Br()
                    ], md=4),
                ]),
                dbc.Row([

                    dbc.Col([
                        dbc.Label('POI Name:'),
                        html.Br(),
                        dbc.Label('POI ID:'),
                        html.Br(),
                        dbc.Label('POI PAN Number:'),
                        html.Br(),
                        dbc.Label('POI Aadhaar:'),
                        html.Br(),
                        dbc.Label('Initial Transaction:'),
                        html.Br(),
                        dbc.Label('Latest Transaction:'),
                        html.Br(),
                        dbc.Label('Case ID:'),
                        html.Br(),
                        dbc.Label('Case Description:'),
                    ], md=2),

                    dbc.Col([
                        dbc.Label(id='username', className='text-success'),
                        html.Br(),
                        dbc.Label(id='userid', className='text-success'),
                        html.Br(),
                        dbc.Label(id='userpan', className='text-success'),
                        html.Br(),
                        dbc.Label(id='useraadhar', className='text-success'),
                        html.Br(),
                        dbc.Label(id='userinitBS', className='text-success'),
                        html.Br(),
                        dbc.Label(id='userlatBS', className='text-success'),
                        html.Br(),
                        dbc.Label(id='usercaseID', className='text-success'),
                        html.Br(),
                        dbc.Label(id='usercaseDesc', className='text-success'),
                    ], md=4),
                ]),
            ], className='jumbotron')
        ])

        return chartContent
