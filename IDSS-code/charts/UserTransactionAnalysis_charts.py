import dash_bootstrap_components as dbc
from dash import dcc, html

plot_style_dimensions = {"width": "100%", "height": "62vh"}


class UserTransactionAnalysisGraphChart:
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

    def user_transaction_analysis_p1_chart_tab(self):
        chartContent = [
            # dbc.Card(
            #     children=[
            #         # dbc.CardBody([
            #         #     dbc.Row([
            #         #         html.H3("Transaction Types Distribution")
            #         #     ])
            #         # ])
            #         html.Hr(),
            # ]),
            html.Div(dbc.Row([
                html.Div([
                    dcc.Loading(
                        children=[
                            dcc.Graph(
                                id="user_transaction_analysis_p11",
                                style=plot_style_dimensions,
                            )
                        ],
                        color="#119DFF",
                        type="cube",
                    ),
                ], style={'width': "50%"}),
                html.Div([
                    dcc.Loading(
                        children=[
                            dcc.Graph(
                                id="user_transaction_analysis_p12",
                                style=plot_style_dimensions,
                            )
                        ],
                        color="#119DFF",
                        type="cube",
                    ),
                ], style={'width': "50%"}),
            ]))
            # dbc.Card(
            #     children=[
            #         dbc.CardBody(
            #             children=[
            #                 dbc.Row([
            #                     dbc.Col(
            #                         dcc.Loading(
            #                             children=[
            #                                 dcc.Graph(
            #                                     id="user_transaction_analysis_p11",
            #                                     style=plot_style_dimensions,
            #                                 )
            #                             ],
            #                             color="#119DFF",
            #                             type="cube",
            #                         ),
            #                         md=6,
            #                         style={"textAlign": "center"},
            #                     ),
            #                     dbc.Row([
            #                         dbc.Col(
            #                             dcc.Loading(
            #                                 children=[
            #                                     dcc.Graph(
            #                                         id="user_transaction_analysis_p12",
            #                                         style=plot_style_dimensions,
            #                                     )
            #                                 ],
            #                                 color="#119DFF",
            #                                 type="cube",
            #                             ),
            #                             md=6,
            #                             style={"textAlign": "center"},
            #                         ),
            #                         dbc.Col(
            #                             dcc.Loading(
            #                                 children=[
            #                                     dcc.Graph(
            #                                         id="user_transaction_analysis_p13",
            #                                         style=plot_style_dimensions,
            #                                     )
            #                                 ],
            #                                 color="#119DFF",
            #                                 type="cube",
            #                             ),
            #                             md=6,
            #                             style={"textAlign": "center"},
            #                         ),
            #                     ])
            #                 ])
            #             ]
            #         )
            #     ],
            # className="mt-3")
        ]

        return chartContent

    def user_transaction_analysis_p2_chart_tab(self):
        chartContent = [
            # dbc.Card(
            #     children=[
            #         # dbc.CardBody([
            #         #     dbc.Row([
            #         #         html.H3("Volume | Frequency Distribtion of Transactions")
            #         #     ])
            #         # ])
            # ]),
            html.Div([
                dbc.Row([
                    dcc.Loading(
                        children=[
                            dcc.Graph(
                                id="user_transaction_analysis_p21",
                                style=plot_style_dimensions,
                            )
                        ],
                        color="#119DFF",
                        type="cube",
                )]),
                html.Hr(),
                dbc.Row([
                    dcc.Loading(
                        children=[
                            dcc.Graph(
                                id="user_transaction_analysis_p22",
                                style=plot_style_dimensions,
                            )
                        ],
                        color="#119DFF",
                        type="cube",
                    )
                ])
            ])
        ]

        return chartContent

    def user_transaction_analysis_p3_chart_tab(self):
        chartContent = [
            dbc.Card(
                children=[
                    dbc.CardBody([
                        dbc.Row([
                            html.H3("Transactions Analysis")
                        ])
                    ])
            ]),
            dbc.Card(
                children=[
                    dbc.CardBody(
                        children=[
                            dbc.Col(
                                dcc.Loading(
                                    children=[
                                        dcc.Graph(
                                            id="user_transaction_analysis_p31",
                                            style=plot_style_dimensions,
                                        )
                                    ],
                                    color="#119DFF",
                                    type="cube",
                                ),
                                md=12,
                                style={"textAlign": "center"},
                            ),
                        ]
                    )
                ],
            className="mt-3")
        ]

        return chartContent
