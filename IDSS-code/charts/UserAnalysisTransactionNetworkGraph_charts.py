import dash_bootstrap_components as dbc
from dash import dcc, html

plot_style_dimensions = {"width": "100%", "height": "62vh"}


class UserAnalysisTransactionNetworkGraphChart:
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

    def user_analysis_transaction_network_chart_tab(self):
        chartContent = [
            # dbc.Card(
            #     children=[
            #         dbc.CardBody([
            #             dbc.Row([
            #                 html.H3("User Transactions Network")
            #             ])
            #         ])
            # ]),
            html.H3('User Transactions Network'),
            html.Hr(),
            dbc.Card(
                children=[
                    dbc.CardBody(
                        children=[
                            # dbc.Row([
                            #     dbc.Col(
                            #         html.H5("User ID : "),
                            #         md="3"
                            #     ),
                            #     dbc.Col(
                            #         dcc.Dropdown(
                            #             id="user_analysis_transaction_network__user_id",
                            #             options=["#001", "#002", "#003", "#004", "#005"],
                            #             value="#001",
                            #             clearable=False,
                            #             multi=False,
                            #             placeholder="User ID",
                            #         ),
                            #         md="3",
                            #     ),
                            # ]),
                            dbc.Col(
                                dcc.Loading(
                                    children=[
                                        dcc.Graph(
                                            id="user_analysis_transaction_network_chart",
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
