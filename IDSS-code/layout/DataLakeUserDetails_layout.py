import dash_bootstrap_components as dbc
from dash import html


class DataLakeUserDetailsAccessories:
    def __init__(self):
        pass

    def project_breadcrumb(self):
        breadCrumbContent = dbc.Breadcrumb(
            items=[
                {"label": "Dashboard", "href": "/", "external_link": False},
                {
                    "label": "Data Lake",
                    "href": "/DataLakeBankDetails",
                    "external_link": False,
                },
                {
                    "label": "User Details",
                    "href": "/DataLakeUserDetails",
                    "external_link": False,
                },
            ],
        )
        return breadCrumbContent

    def project_first_row(self):
        breadcrumbContent = self.project_breadcrumb()
        projectFirstLayout = dbc.Card(
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
                                        id="validationEngineeringProjectReport",
                                    ),
                                    md="3",
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        )
        return projectFirstLayout

    def project_second_row(self):
        projectSecondLayout = html.Div(
            [
                dbc.Tabs(
                    [
                        dbc.Tab(label="Project Wise", tab_id="val_proj_comp_tab1"),
                        dbc.Tab(label="WBS Tasks Wise", tab_id="val_proj_comp_tab2"),
                        dbc.Tab(label="Module Wise", tab_id="val_proj_comp_tab3"),
                        dbc.Tab(label="Employee Wise", tab_id="val_proj_comp_tab4"),
                    ],
                    id="valEngineeringTabs",
                    active_tab="val_proj_comp_tab1",
                    loading_state={"is_loading": True},
                    persistence=True,
                    persistence_type="session",  # "local", "session", "memory"
                ),
                html.Div(id="valEngineeringTabsDiv"),
            ]
        )
        return projectSecondLayout


class DataLakeUserDetailsLayout(DataLakeUserDetailsAccessories):
    def __init__(self):
        DataLakeUserDetailsAccessories.__init__(self)
        pass

    def project_layout(self):
        firstRow = self.project_first_row()
        secondRow = self.project_second_row()
        finalLayout = dbc.Row(
            [
                # dbc.Col(firstRow, md="12"),
                dbc.Col(secondRow, md="12")
            ]
        )

        return finalLayout
