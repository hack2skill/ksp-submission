import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table

plot_style_dimensions = {"width": "100%", "height": "62vh"}  # 80, 68


class UserTransactionHistoryDetailsDataTableChart:
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

    def user_transaction_history_details_datatable(self):
        df = pd.read_excel("saved/IFCB2009_68.xlsx")  # pd.read_excel(r"C:\Users\gandem\Desktop\shit\police-hack\aml-squad\saved\IFCB2009_68.xlsx")
        chartContent = [
            html.H3("User Transaction History Data Table"), # , id="bank_details_dummy"
            html.Br(),
            # dbc.Card(
            #     children=[
            #         dbc.CardBody([
            #             dbc.Row([
            #                 html.H3("Bank Details", id="bank_details_dummy")
            #             ])
            #         ])
            #     ]),
            dbc.Card(
                children=[
                    dbc.CardBody(
                        children=[
                            dbc.Col(
                                dcc.Loading(
                                    children=[
                                        dash_table.DataTable(
                                            id='user-transaction-history-datatable',
                                            data=df.to_dict("records"),
                                            columns=[{"name": i, "id": i} for i in df.columns],
                                            filter_action="native",
                                            filter_options={"placeholder_text": "Filter column..."},
                                            page_size=10,
                                            virtualization=False,
                                            style_table={'overflowX': 'scroll'},
                                            style_data={
                                                'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                                                # 'overflow': 'hidden',
                                                'textOverflow': 'ellipsis',
                                            }
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
