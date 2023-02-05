import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,  #
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f1f3f5",
}

update_date = "14 Nov, 22"


class DashboardAccessories:
    def __init__(self, userName):
        self.userName = userName
        self.contactusIcon = "assets/icons/contactus.png"
        self.userImage = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

    def menubar_items(self):
        menubarItems = dbc.Row(
            children=[
                # dbc.Col(
                #     dbc.NavbarBrand(
                #         f"Last Updated on : {update_date}",
                #         style={
                #             "font-size": "14px",
                #         }
                #     )
                # ),dbc.Col(
                #                     dcc.Dropdown(
                #                         id="case_id",
                #                         options=["#C1", "#C2", "#C3", "#C4", "#C5"],
                #                         # value="#C1",
                #                         # clearable=False,
                #                         multi=False,
                #                         placeholder="Case ID",
                #                     ),
                #                     md="9",
                #                 ),
                #                 dbc.Col(
                #                     dcc.Dropdown(
                #                         id="user_id",
                #                         options=["#001", "#002", "#003", "#004", "#005"],
                #                         # value="#001",
                #                         # clearable=False,
                #                         multi=False,
                #                         placeholder="User ID",
                #                     ),
                #                     md="9",
                #                 ),

                # dbc.Col(
                #     dbc.NavItem(
                #         dbc.Button("Upload Data", color="warning", className="me-1", outline=False),
                #     ),
                # ),
            ],
            className="ms-auto navbar-item",
            align="center",
        )
        return menubarItems


class DashboardLayout(DashboardAccessories):
    def __init__(self, userName):
        DashboardAccessories.__init__(self, userName)
        self.projectIcon = "assets/icons/benchmark.png"

    def navbar_template(self):
        menubar = self.menubar_items()
        navbar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Button(
                        ["", html.I(className="fa-solid fa-bars")],
                        outline=True,
                        color="secondary",
                        className="mr-1",
                        id="btn_sidebar",
                        style={"margin-right": "5px"},
                    ),
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=self.projectIcon, height="38px")),
                                dbc.Col(
                                    [dbc.NavbarBrand(
                                        "Investigation Decision Support System (IDSS)",
                                        className="ms-2",
                                    ),
                                    ]
                                ),
                            ],
                            align="center",
                            className="g-0",
                            style={"margin-left": "0rem"},
                        ),
                        href="/",
                        style={"textDecoration": "none"},
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse(
                        menubar, id="navbar-collapse", is_open=False, navbar=True,
                    ),
                ],
                fluid=True,
                className="navbar-style",
            ),
            style={"height": "50px"},
        )
        return navbar

    def sidebar_template(self):
        df = pd.read_csv("http://20.231.200.146:9000/master_db.csv")
        df.to_csv("saved/master_db.csv", index=False)

        cases = df['Case ID'].unique().tolist()
        sidebar = html.Div(
            [
                dcc.Dropdown(
                    id="case_id",
                    options=cases, # ["#C1", "#C2", "#C3", "#C4", "#C5"]
                    multi=False,
                    placeholder="Case ID",
                ),
                dcc.Dropdown(
                    id="user_id",
                    options=[], # "#001", "#002", "#003", "#004", "#005"
                    multi=False,
                    placeholder="User ID",
                ),

                html.Hr(),
                dbc.Nav(
                    children=[
                        dbc.NavLink(
                            [
                                html.I(
                                    className="fa-solid fa-address-card"
                                ),
                                "  User Profile",
                            ],
                            id="user-profile",
                            href="/user_profile",
                            active="exact",
                            className="sidebar-navlink",
                        ),
                        dbc.NavLink(
                            [
                                html.I(
                                    className="fas fa-chart-line"
                                ),
                                "  Transactions Analysis",
                            ],
                            id="eda",
                            # active=False,
                            # style={"padding-left": "2px", "margin-top": "2px"},
                            href="/eda",
                            active="exact",
                            className="sidebar-navlink",
                        ),
                        dbc.NavLink(
                            [
                                html.I(
                                    className="fa-solid fa-magnifying-glass-chart" # "fa-solid fa-chart-network"
                                ),
                                " Transaction Network",
                            ],
                            id="transaction-network",
                            # active=False,
                            # style={"padding-left": "2px", "margin-top": "2px"},
                            href="/transaction_network",
                            active="exact",
                            className="sidebar-navlink",
                        ),
                        # dbc.NavLink(
                        #     [
                        #         html.I(
                        #             className="fas fa-chart-bar"
                        #         ),
                        #         " Transactions History",
                        #     ],
                        #     id="transaction-history",
                        #     # active=False,
                        #     # style={"padding-left": "2px", "margin-top": "2px"},
                        #     href="/transaction_history",
                        #     active="exact",
                        #     className="sidebar-navlink",
                        # ),
                        dbc.NavLink(
                            [
                                html.I(
                                    className="fas fa-chart-pie"
                                ),
                                " Pattern Analysis",
                            ],
                            id="pattern-analysis",
                            # active=False,
                            # style={"padding-left": "2px", "margin-top": "2px"},
                            href="/pattern_analysis",
                            active="exact",
                            className="sidebar-navlink",
                        ),
                        dbc.NavLink(
                            [
                                html.I(
                                    className="fas fa-users-gear"
                                ),
                                " Case-User Details",
                            ],
                            id="case-user-details",
                            # active=False,
                            # style={"padding-left": "2px", "margin-top": "2px"},
                            href="/case_user_details",
                            active="exact",
                            className="sidebar-navlink",
                        ),
                        dbc.NavLink(
                            [
                                html.I(
                                    className="fas fa-address-book"
                                ),
                                " Bank Details",
                            ],
                            id="bank-details",
                            # active=False,
                            # style={"padding-left": "2px", "margin-top": "2px"},
                            href="/bank_details",
                            active="exact",
                            className="sidebar-navlink",
                        ),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            id="sidebar",
            style=SIDEBAR_STYLE,
        )
        return sidebar
