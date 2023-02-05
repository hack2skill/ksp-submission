import gc
import math
import holidays
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table

plot_style_dimensions = {"width": "100%", "height": "62vh"}  # 80, 68


def pp_for_pattern_analysis(data):
    def get_transaction_type(desc):

        if ("upi" in desc.lower()):
            return "UPI"

        mapping_dict = {
            "IMPS": "IMPS",
            "WITHDRAWAL TRANSFER": "ATM WDL",
            "ATM WDL": "ATM WDL",
            "CSH DEP": "CSH DEP",

            "NACH": "NACH",
            "INB": "NEFT",
            "SBILT": "NEFT",
            "NEFT": "NEFT",
        }

        for key, value in mapping_dict.items():
            if (key.lower() in desc.lower()):
                return value

        return "Others"

    data['type_of_transaction'] = data['Description'].apply(lambda x: get_transaction_type(x))

    data['Balance Lag'] = data['Balance'].shift(1)
    data['Movement'] = data['Balance'] - data['Balance Lag']

    debit_limit = data[data['Movement'] < 0]['Movement'].quantile(0.05)
    credit_limit = data[data['Movement'] > 0]['Movement'].quantile(0.95)
    data['High Volume Debit'] = data['Movement'].apply(lambda x: 1 if x < debit_limit else 0)
    data['High Volume Credit'] = data['Movement'].apply(lambda x: 1 if x > credit_limit else 0)

    # data['High Volume Debit'] = np.where(data['Movement'] >= abs(data['Movement'].quantile(0.05)), 1, 0)
    # data['High Volume Credit'] = np.where(data['Movement'] >= abs(data['Movement'].quantile(0.95)), 1, 0)
    data['Is_Weekend'] = np.where(pd.to_datetime(data["Txn Date"]).dt.weekday >= 5, 1, 0)
    in_holidays = holidays.country_holidays('IN')
    data['Holiday'] = np.where(pd.to_datetime(data["Txn Date"]).apply(lambda d: d in in_holidays) == True, 1, 0)

    data.columns = [i.strip() for i in data.columns.tolist()]

    return data


class PatternAnalysisDetailsChart:
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


    def pattern_analysis_details_datatable(self):
        df = pd.read_csv("saved/user01_vinneth_2023-02-04-15-49-56_.csv")  # pd.read_csv(r"C:\Users\gandem\Desktop\shit\police-hack\aml-squad\saved\ifsc_global_data.csv")
        df = pp_for_pattern_analysis(df)
        filters = ['High Volume Debit', 'High Volume Credit', 'Is_Weekend', 'Holiday']  # , 'type_of_transaction'

        to_show_cols = ['Txn Date', 'Description', 'Debit', 'Credit', 'type_of_transaction', *filters]

        df = df[df[filters[0]] == 1].copy()
        df = df[to_show_cols]

        chartContent = [
            dbc.Card(
                children=[
                    dbc.CardBody([
                        dbc.Row([
                            html.H3("Pattern Analysis", id="patterns_dummy")
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
                                        dbc.Row(
                                            [
                                                html.H5("Pattern Filters "),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        id="pattern_filter_names",
                                                        options=filters,
                                                        value=[filters[0]],
                                                        clearable=False,
                                                        multi=True,
                                                        placeholder="Select Filter Type ..",
                                                    ),
                                                    md="12",
                                                ),
                                            ]
                                        ),
                                        dash_table.DataTable(
                                            id='pattern-details-datatable',
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
