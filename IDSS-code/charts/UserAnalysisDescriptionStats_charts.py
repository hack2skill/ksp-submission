import dash_bootstrap_components as dbc
from dash import dcc, html
from callbacks import dataloader

plot_style_dimensions = {"width": "100%", "height": "62vh"}  # 80, 68


class UserAnalysisDescriptionStatsChart:
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

    def global_tab_tree_chart(self):
        chartContent = dbc.Card(
            dbc.CardBody(
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            html.H5(
                                                "Total Effort Splits - TreeMap",
                                                id="dev_global_treemap_dummy",
                                            ),
                                            width="auto",
                                        ),
                                        dbc.Col(
                                            html.Button(
                                                [
                                                    "",
                                                    html.I(
                                                        className="fas fa-info"  # bi bi-info-circle-fill me-2
                                                    ),
                                                ],
                                                style=self.icon_style,
                                                id="dev_global_treemap_info_button",
                                                n_clicks=0,
                                            ),
                                            width="auto",
                                        ),
                                        dbc.Offcanvas(
                                            dcc.Markdown(
                                                """
                                                This infographic represents the **split of total development effort in a 
                                                hierarchical manner** : 
                                                
                                                - Modules
                                                - Projects
                                                - Releases
                                                - EmployeeType (i.e Internal, External, YGT)
                                                """
                                            ),
                                            id="dev_global_treemap_off_canvas",
                                            title="Total Effort Splits - TreeMap",
                                            is_open=False,
                                            placement="bottom",
                                            scrollable=True,
                                        ),
                                    ]
                                ),
                                md="9",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    html.Span(
                                        [
                                            html.I(className="fas fa-download"),
                                            "  Download Data",
                                        ]
                                    ),
                                    style={
                                        "margin-right": "5px",
                                        "float": "right",
                                        "background-color": "#AF8FB9",
                                        "border-color": "#AF8FB9"
                                        # "align-content": "flex-end"
                                        # "horizontal-align": "right"
                                    },
                                    id="downloadGlobalTreeData",
                                ),
                                md="3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        dcc.Loading(
                            children=[
                                dcc.Graph(
                                    id="dev_global_treemap",
                                    style=plot_style_dimensions,
                                )
                            ],
                            color="#119DFF",
                            type="cube",
                        ),
                        md=12,
                        style={"textAlign": "center"},
                    ),
                ],
            ),
            className="mt-3",
        )

        return chartContent

    def global_tab_sunburst_chart(self):
        chartContent = dbc.Card(
            dbc.CardBody(
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            html.H5(
                                                "Total Effort Splits - Sunburst",
                                                id="dev_global_sunburst_dummy",
                                            ),
                                            width="auto",
                                        ),
                                        dbc.Col(
                                            html.Button(
                                                [
                                                    "",
                                                    html.I(
                                                        className="fas fa-info"  # bi bi-info-circle-fill me-2
                                                    ),
                                                ],
                                                style=self.icon_style,
                                                id="dev_global_sunburst_info_button",
                                                n_clicks=0,
                                            ),
                                            width="auto",
                                        ),
                                        dbc.Offcanvas(
                                            dcc.Markdown(
                                                """
                                                This infographic represents the **split of total development effort in a 
                                                hierarchical manner** : 
                                                
                                                - Modules
                                                - Projects
                                                - Releases
                                                - EmployeeType (i.e Internal, External, YGT)
                                                """
                                            ),
                                            id="dev_global_sunburst_off_canvas",
                                            title="Total Effort Splits - Sunburst",
                                            is_open=False,
                                            placement="bottom",
                                            scrollable=True,
                                        ),
                                    ]
                                ),
                                md="9",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    html.Span(
                                        [
                                            html.I(className="fas fa-download"),
                                            "  Download Data",
                                        ]
                                    ),
                                    style={
                                        "margin-right": "5px",
                                        "float": "right",
                                        "background-color": "#AF8FB9",
                                        "border-color": "#AF8FB9"
                                        # "align-content": "flex-end"
                                        # "horizontal-align": "right"
                                    },
                                    id="downloadGlobalSunburstData",
                                ),
                                md="3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        dcc.Loading(
                            children=[
                                dcc.Graph(
                                    id="dev_global_sunburst",
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
            ),
            className="mt-3",
        )
        return chartContent

    def global_tab_effort_duration_chart(self):
        chartContent = dbc.Card(
            dbc.CardBody(
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            html.H5(
                                                "Effort vs Duration",
                                                # id="dev_global_sunburst_dummy",
                                            ),
                                            width="auto",
                                        ),
                                        dbc.Col(
                                            html.Button(
                                                [
                                                    "",
                                                    html.I(
                                                        className="fas fa-info"  # bi bi-info-circle-fill me-2
                                                    ),
                                                ],
                                                style=self.icon_style,
                                                id="dev_global_effort_vs_duration_info_button",
                                                n_clicks=0,
                                            ),
                                            width="auto",
                                        ),
                                        dbc.Offcanvas(
                                            dcc.Markdown(
                                                """
                                                This infographic represents the **Trend of the Effort** put in **Module-Wise** : 
                                                
                                                - **Work** : The actual amount of effort put in
                                                - **Duration** : How much time did it take to put in the effort (work)  
                                                
                                                **Filters Available** : 
                                                
                                                - Modules
                                                """
                                            ),
                                            id="dev_global_effort_vs_duration_off_canvas",
                                            title="Effort vs Duration",
                                            is_open=False,
                                            placement="bottom",
                                            scrollable=True,
                                        ),
                                    ]
                                ),
                                md="9",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    html.Span(
                                        [
                                            html.I(className="fas fa-download"),
                                            "  Download Data",
                                        ]
                                    ),
                                    style={
                                        "margin-right": "5px",
                                        "float": "right",
                                        "background-color": "#AF8FB9",
                                        "border-color": "#AF8FB9"
                                        # "align-content": "flex-end"
                                        # "horizontal-align": "right"
                                    },
                                    id="downloadGlobalSunburstData",
                                ),
                                md="3",
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            # dbc.Col(html.H5("Module Name"), md="4"),
                            dbc.Col(
                                dcc.Dropdown(
                                    id="dev_global_effort_vs_duration_dropdown",
                                    options=dataloader.dev_efforts_parent[
                                        "modules_list"
                                    ],
                                    value=dataloader.dev_efforts_parent["modules_list"][
                                        0
                                    ],
                                    clearable=False,
                                    multi=False,
                                    placeholder="Module Name",
                                ),
                                md="4",
                            ),
                        ]
                    ),
                    dbc.Col(
                        dcc.Loading(
                            children=[
                                dcc.Graph(
                                    id="dev_global_effort_vs_duration",
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
            ),
            className="mt-3",
        )
        return chartContent
