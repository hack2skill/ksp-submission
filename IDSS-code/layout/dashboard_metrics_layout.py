import dash_bootstrap_components as dbc
from dash import dcc, html


class DashboardMetricsAccessories:
    def __init__(self):
        self.icon_style = {
            "padding-top": "3px",
            "margin-top": "3px",
            "text-align": "center",
            "background": "#ffffff",
            "color": "#76aa60",
            "border-color": "#76aa60",
            "border-bottom-width": "0px",
        }
        self.card_header_style = {
            "padding": "2px",
            "text-align": "center",
            "background": "#76aa60",
            "color": "#ffffff",
            "border-bottom-width": "0px",
        }
        self.card_header_style_disabled = {
            "padding": "2px",
            "text-align": "center",
            "background": "#76aa60",
            "color": "#ffffff",
            "border-bottom-width": "0px",
            "opacity": 0.6,
            "cursor": "not-allowed",
        }
        self.card_body_style = {
            "padding": "2px",
        }
        self.card_body_row_style = {
            "padding": "10px",
        }
        self.card_footer_button_style = {
            "background-color": "#AF8FB9",
            "border-color": "#AF8FB9",
            "width": "100%",
        }
        self.card_footer_button_style_disabled = {
            "background-color": "#AF8FB9",
            "border-color": "#AF8FB9",
            "width": "100%",
            "opacity": 0.6,
            "cursor": "not-allowed",
        }
        self.card_footer_end_button_style = {
            "background-color": "#AF8FB9",
            "border-color": "#AF8FB9",
            "float": "right",
            "width": "100%",
        }
        self.card_footer_end_button_style_disabled = {
            "background-color": "#AF8FB9",
            "border-color": "#AF8FB9",
            "float": "right",
            "width": "100%",
            "opacity": 0.6,
            "cursor": "not-allowed",
        }
        self.card_sample_style = {
            "background-color": "white",
            "text-align": "center",
            "border": "2px solid white",
            "font-size": "20px",
            "font-weight": "bold",
        }
        self.card_sample_style_disabled = {
            "background-color": "white",
            "text-align": "center",
            "border": "2px solid white",
            "font-size": "20px",
            "font-weight": "bold",
            "opacity": 0.6,
            "cursor": "not-allowed",
        }

        self.tile_metric_button_style = {
            "background-color": "white",
            "color": "black",
            "text-align": "center",
            "margin-top": "25px",
            "border": "2px solid white",
            "font-size": "20px",
            "font-weight": "bold",
        }
        self.tile_comparison_button_style = {
            "background-color": "white",
            "color": "black",
            "text-align": "center",
            "margin-top": "25px",
            "border": "2px solid white",
            "font-size": "20px",
            "font-weight": "bold",
        }
    
    def get_cost_card(self):
        costCard = dbc.Card(
            children=[
                dbc.CardHeader(
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.H4(
                                            "Cost",
                                            className="card-title",
                                            style=self.card_header_style_disabled,
                                        ),
                                        md="10",
                                    ),
                                    dbc.Col(
                                        html.Button(
                                            ["", html.I(className="fas fa-info")],
                                            style=self.icon_style,
                                            id="cost-info-button",
                                            n_clicks=0,
                                        ),
                                        md="2",
                                    ),
                                    dbc.Offcanvas(
                                        html.P("Not Decided yet."),
                                        id="cost-off-canvas",
                                        title="Cost Metric",
                                        is_open=False,
                                        placement="bottom",
                                        scrollable=True,
                                        # style={"offcanvas-vertical-height": "10vh"},
                                    ),
                                ]
                            ),
                            #
                        ],
                    ),
                    style=self.card_header_style,
                ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Button(
                                            "-",
                                            title="Not Decided",
                                            id="cost_tile_value_button",
                                            n_clicks=0,
                                            style=self.card_sample_style_disabled,
                                        ),
                                    ],
                                    sm="6",
                                ),
                                dbc.Col(
                                    [
                                        html.Button(
                                            "-",
                                            title="Not Decided",
                                            id="cost_tile_comparison_button",
                                            n_clicks=0,
                                            style=self.card_sample_style_disabled,
                                        ),
                                    ],
                                    sm="6",
                                ),
                            ],
                            style=self.card_body_row_style,
                        ),
                    ],
                    style=self.card_body_style,
                ),
                dbc.CardFooter(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "-",
                                            style=self.card_footer_button_style_disabled,
                                            id="costProject",
                                        ),
                                    ],
                                    sm="6",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "-",
                                            style=self.card_footer_end_button_style_disabled,
                                            id="costTime",
                                        ),
                                    ],
                                    sm="6",
                                ),
                            ],
                        ),
                    ]
                ),
            ]
        )
        return costCard

    def get_quality_card(self):
        qualityCard = dbc.Card(
            children=[
                dbc.CardHeader(
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.H4(
                                            "Quality",
                                            className="card-title",
                                            style=self.card_header_style,
                                        ),
                                        md="10",
                                    ),
                                    dbc.Col(
                                        html.Button(
                                            ["", html.I(className="fas fa-info")],
                                            style=self.icon_style,
                                            id="quality-info-button",
                                            n_clicks=0,
                                        ),
                                        md="2",
                                    ),
                                    dbc.Offcanvas(
                                        dcc.Markdown(
                                            """
                                            This is a global metric defined to quantify the **quality** of the product 
                                            being produced
                                            
                                            Here Quality is defined as the **total number of (accepted and converted
                                            to a 'ChangeRequest')** defects filed on **JIRA**
                                            """
                                        ),
                                        id="quality-off-canvas",
                                        title="Quality Metric",
                                        is_open=False,
                                        placement="bottom",
                                        scrollable=True,
                                    ),
                                ]
                            ),
                            #
                        ],
                    ),
                    style=self.card_header_style,
                ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Button(
                                            " ",
                                            title="Number of Accepted Defects this year",
                                            id="quality_tile_value_button",
                                            n_clicks=0,
                                            style=self.tile_metric_button_style,
                                        ),
                                    ],
                                    sm="6",
                                ),
                                dbc.Col(
                                    [
                                        html.Button(
                                            " ",
                                            title="Comparison to historical average",
                                            id="quality_tile_comparison_button",
                                            n_clicks=0,
                                            style=self.tile_comparison_button_style,
                                        ),
                                    ],
                                    sm="6",
                                ),
                            ],
                            style=self.card_body_row_style,
                        ),
                    ],
                    style=self.card_body_style,
                ),
                dbc.CardFooter(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Defect Trend",
                                            style=self.card_footer_button_style,
                                            id="quality_bugs_trend_button",
                                        ),
                                    ],
                                    sm="6",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Defect Count",
                                            style=self.card_footer_end_button_style,
                                            id="quality_bugs_count_button",
                                        ),
                                    ],
                                    sm="6",
                                ),
                            ],
                        ),
                    ]
                ),
            ]
        )
        return qualityCard

    def get_delivery_card(self):
        deliveryCard = dbc.Card(
            children=[
                dbc.CardHeader(
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.H4(
                                            "Delivery",
                                            className="card-title",
                                            style=self.card_header_style,
                                        ),
                                        md="10",
                                    ),
                                    dbc.Col(
                                        html.Button(
                                            ["", html.I(className="fas fa-info")],
                                            style=self.icon_style,
                                            id="delivery-info-button",
                                            n_clicks=0,
                                        ),
                                        md="2",
                                    ),
                                    dbc.Offcanvas(
                                        dcc.Markdown(
                                            """
                                            This is a global metric defined to quantify the **delivery** of the 
                                            product being produced

                                            Here Delivery is defined as the **total number of On-Time Deliveries i.e 
                                            on or before the planned date of the release**
                                            
                                            Note: Here a **Delay Leeway of 14 days is used** i.e. any delivery will be 
                                            considered as On-Time Delivery if its under or on 14 days after the Planned 
                                            Delivery date
                                            """
                                        ),
                                        id="delivery-off-canvas",
                                        title="Delivery Metric",
                                        is_open=False,
                                        placement="bottom",
                                        scrollable=True,
                                    ),
                                ]
                            ),
                            #
                        ],
                    ),
                    style=self.card_header_style,
                ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Button(
                                            " ",
                                            title="Percentage of On-Time Deliveries this year",
                                            id="delivery_tile_value_button",
                                            n_clicks=0,
                                            style=self.tile_metric_button_style,
                                        ),
                                    ],
                                    sm="6",
                                ),
                                dbc.Col(
                                    [
                                        html.Button(
                                            " ",
                                            title="Comparison to historical average",
                                            id="delivery_tile_comparison_button",
                                            n_clicks=0,
                                            style=self.tile_comparison_button_style,
                                        ),
                                    ],
                                    sm="6",
                                ),
                            ],
                            style=self.card_body_row_style,
                        ),
                    ],
                    style=self.card_body_style,
                ),
                dbc.CardFooter(
                    [
                        dbc.Row(
                            [
                                # dbc.Col(
                                #     [
                                #         dbc.Button(
                                #             "Delivery Trend",
                                #             style=self.card_footer_button_style,
                                #             id="delivery_plot1_button",
                                #         ),
                                #     ],
                                #     sm="6",
                                # ),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Delivery Delay Trend",
                                            style=self.card_footer_end_button_style,
                                            id="delivery_plot2_button",
                                        ),
                                    ],
                                    sm="12",
                                ),
                            ],
                        ),
                    ]
                ),
            ]
        )
        return deliveryCard


class DashboardMetricsLayout(DashboardMetricsAccessories):
    def __init__(self):
        DashboardMetricsAccessories.__init__(self)

    def get_dashboard_top_level_metrics_layout(self):
        costCard = self.get_cost_card()
        qualityCard = self.get_quality_card()
        deliveryCard = self.get_delivery_card()
        dashboardTopMetricsLayout = dbc.Row(
            [
                dbc.Col(costCard, md="4"),
                dbc.Col(qualityCard, md="4"),
                dbc.Col(deliveryCard, md="4"),
            ]
        )
        return dashboardTopMetricsLayout
