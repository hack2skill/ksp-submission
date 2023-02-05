import dash_bootstrap_components as dbc
from dash import html


class UserAnalysisDescriptionStatsAccessories:
    def __init__(self):
        pass

    def global_breadcrumb(self):
        breadcrumbContent = dbc.Breadcrumb(
            items=[
                {"label": "Dashboard", "href": "/", "external_link": False},
                {
                    "label": "User Analysis",
                    "href": "/UserAnalysisDescriptionStats",
                    "external_link": False,
                },
                {
                    "label": "Description Statistics",
                    "href": "/UserAnalysisDescriptionStats",
                    "external_link": False,
                },
            ],
        )
        return breadcrumbContent

    def global_first_row(self):
        breadcrumbContent = self.global_breadcrumb()
        globalFirstRowLayout = dbc.Card(
            children=[
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(breadcrumbContent, md="9"),
                                dbc.Col(
                                    dbc.Button(
                                        html.Span(
                                            [
                                                html.I(className="fas fa-download"),
                                                "  Download Report",
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
                                        id="devlopmentEngineeringGlobalReport",
                                    ),
                                    md="3",
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        )

        return globalFirstRowLayout

    def global_second_row(self):
        globalSecondRowLayout = html.Div(
            [
                dbc.Tabs(
                    [
                        dbc.Tab(
                            label="Transaction Types Analysis",
                            tab_id="dev_global_tab1",
                        ),
                        dbc.Tab(
                            label="Volume | Frequency Analysis",
                            tab_id="dev_global_tab2",
                        ),
                        # dbc.Tab(label="Effort vs Duration", tab_id="dev_global_tab3"),
                    ],
                    id="devEngineeringTabs",
                    active_tab="dev_global_tab1",
                    loading_state={"is_loading": True},
                    persistence=True,
                    persistence_type="session",  # "local", "session", "memory"
                ),
                html.Div(id="devEngineeringTabsDiv"),
            ]
        )
        return globalSecondRowLayout


class UserAnalysisDescriptionStatsLayout(UserAnalysisDescriptionStatsAccessories):
    def __init__(self):
        UserAnalysisDescriptionStatsAccessories.__init__(self)
        pass

    def global_layout(self):
        firstRow = self.global_first_row()
        secondRow = self.global_second_row()
        finalLayout = dbc.Row(
            [
                # dbc.Col(firstRow, md="12"),
                dbc.Col(secondRow, md="12"),]
        )
        return finalLayout
