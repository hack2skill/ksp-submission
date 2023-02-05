import dash_bootstrap_components as dbc
from dash import html


class UserAnalysisTransactionNetworkGraphAccessories:
    def __init__(self):
        pass

    def first_row(self):
        FirstLayout = dbc.Card(children=[
            dbc.CardBody([
                dbc.Row([
                    html.H3("User Transactions Network")
                ])
            ])
        ])

        return FirstLayout

    # def project_second_row(self):
    #     projectSecondLayout = html.Div(
    #         [
    #             dbc.Tabs(
    #                 [
    #                     dbc.Tab(label="Project Wise", tab_id="dev_proj_comp_tab1"),
    #                     dbc.Tab(label="WBS Tasks Wise", tab_id="dev_proj_comp_tab2"),
    #                     dbc.Tab(label="Module Wise", tab_id="dev_proj_comp_tab3"),
    #                     dbc.Tab(label="Employee Wise", tab_id="dev_proj_comp_tab4"),
    #                 ],
    #                 id="devEngineeringTabs",
    #                 active_tab="dev_proj_comp_tab1",
    #                 loading_state={"is_loading": True},
    #                 persistence=True,
    #                 persistence_type="session",  # "local", "session", "memory"
    #             ),
    #             html.Div(id="devEngineeringTabsDiv"),
    #         ]
    #     )
    #     return projectSecondLayout


class UserAnalysisTransactionNetworkGraphLayout(UserAnalysisTransactionNetworkGraphAccessories):
    def __init__(self):
        UserAnalysisTransactionNetworkGraphAccessories.__init__(self)
        pass

    def layout(self):
        firstRow = self.first_row()
        # secondRow = self.second_row()
        finalLayout = dbc.Row(
            [
                dbc.Col(firstRow, md="12"),
                # dbc.Col(secondRow, md="12"),
            ]
        )

        return finalLayout
