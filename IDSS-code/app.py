import ast
import os
import urllib.parse
import pandas as pd
import numpy as np
import dash
import plotly.express as px
import networkx as nx
import holidays
import math
from colour import Color
import plotly.graph_objects as go
from dash import State
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback, callback_context
from plotly.subplots import make_subplots

from layout import (
    dashboard_layout,
    dashboard_metrics_layout,
    UserAnalysisDescriptionStats_layout,
    UserAnalysisTransactionNetworkGraph_layout,

    DataLakeBankDetails_layout,
    DataLakeUserDetails_layout,
)
from charts.dashboard_quality_charts import QualityCharts
from charts.dashboard_delivery_charts import DeliveryCharts
from charts.UserTransactionAnalysis_charts import UserTransactionAnalysisGraphChart
# from charts.UserAnalysisDescriptionStats_charts import UserAnalysisDescriptionStatsChart
from charts.PatternAnalysisDataTable_charts import PatternAnalysisDetailsChart
from charts.UserAnalysisTransactionNetworkGraph_charts import UserAnalysisTransactionNetworkGraphChart
from charts.UserProfile_charts import UserProfile
from charts.DataLakeBankDetails_charts import DataLakeBankDetailsChart
from charts.UserTransactionHistoryDetails_charts import UserTransactionHistoryDetailsDataTableChart
from charts.DataLakeUserDetails_charts import DataLakeUserDetailsChart

# from callbacks import callback_manager as plots_callback_manager
# from offcanvas_callbacks import callback_manager as offcanvas_callback_manager

import warnings
warnings.simplefilter('ignore')


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],  # "https://codepen.io/chriddyp/pen/dZVMbK.css"
    suppress_callback_exceptions=True,
)

user_transaction_df = None


### STYLE SIDE BAR ###
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "51px",
    "left": 0,
    "bottom": 0,
    "width": "17rem",
    "height": "100%",
    "z-index": -9999,
    "overflow": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f1f3f5",
}

SIDEBAR_HIDDEN = {
    "position": "fixed",
    "top": "51px",
    "left": "-18rem",
    "bottom": 0,
    "width": "17rem",
    "height": "100%",
    "z-index": -99991,
    "overflow": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f1f3f5",
}
### CONTENT STYLE BAR ###
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "17.5rem",
    "margin-right": "1px",
    "margin-top": "1px",
    "padding": "2rem 1rem",
    "background-color": "#ffffff",
}

CHART_CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    # "margin-top": "20px",
    "margin-right": "1px",
    "padding": "2rem 1rem",
    "background-color": "#ffffff",
}


CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "1px",
    "padding": "2rem 1rem",
    "margin-top": "0px",
    "background-color": "#ffffff",
}

### Create the Side Bar and Navbar Layout together ###
dashboardLayoutObject = dashboard_layout.DashboardLayout(userName="chib")
navbarTemplate = dashboardLayoutObject.navbar_template()
sidebarTemplate = dashboardLayoutObject.sidebar_template()
del dashboardLayoutObject

### Create the top 3 Metrics Layout together ###
dashboardLayoutObject = dashboard_metrics_layout.DashboardMetricsLayout()
dashboardTopMetricsLayout = (
    dashboardLayoutObject.get_dashboard_top_level_metrics_layout()
)
del dashboardLayoutObject

### Call the Dashboard Quality Charts ###
qualityLayoutChartObject = QualityCharts()
qualityBugTrendChart = qualityLayoutChartObject.quality_bugs_trend_chart()
qualityBugCountChart = qualityLayoutChartObject.quality_bugs_count_chart()
qualityBugTrendMetricChart = qualityLayoutChartObject.quality_bug_trend_metric_chart()

del qualityLayoutChartObject

### Call the Dashboard Delivery Charts ###
deliveryLayoutChartObject = DeliveryCharts()
deliveryOntimeTrendChart = deliveryLayoutChartObject.delivery_ontime_trend_chart()
deliveryReleaseTrendChart = deliveryLayoutChartObject.delivery_release_trend_chart()
deliveryOntimeMetricChart = (
    deliveryLayoutChartObject.delivery_ontime_trend_metric_chart()
)
del deliveryLayoutChartObject


### Call the Development Global Metrics Layout ###
UserAnalysisDescriptionStatsLayoutObject = UserAnalysisDescriptionStats_layout.UserAnalysisDescriptionStatsLayout()
UserAnalysisDescriptionStatsLayout = UserAnalysisDescriptionStatsLayoutObject.global_layout()
del UserAnalysisDescriptionStatsLayoutObject

### Call the Development Global Charts ###
UserAnalysisDescriptionStatsChartObject = UserTransactionAnalysisGraphChart()
UserAnalysisDescriptionStatsTreeChart = UserAnalysisDescriptionStatsChartObject.user_transaction_analysis_p1_chart_tab()
UserAnalysisDescriptionStatsSunBurstChart = (
    UserAnalysisDescriptionStatsChartObject.user_transaction_analysis_p2_chart_tab()
)
# UserAnalysisDescriptionStatsEffortChart = (
#     UserAnalysisDescriptionStatsChartObject.user_transaction_analysis_p1_chart_tab()
# )
del UserAnalysisDescriptionStatsChartObject


### Call the Development Project Wise Charts ###
UserProfileObject = UserProfile()
UserProfileChart = UserProfileObject.user_profile_tab()
del UserProfileObject


### Call the Development Project Wise Charts ###
UserAnalysisTransactionNetworkGraphChartObject = UserAnalysisTransactionNetworkGraphChart()
UserAnalysisTransactionNetworkGraphChart = UserAnalysisTransactionNetworkGraphChartObject.user_analysis_transaction_network_chart_tab()
del UserAnalysisTransactionNetworkGraphChartObject

# PatternAnalysisDetailsChart
### Call the Validation Global Charts ###
PatternAnalysisDetailsChartObject = PatternAnalysisDetailsChart()
PatternAnalysisDetailsDataTable = PatternAnalysisDetailsChartObject.pattern_analysis_details_datatable()
del PatternAnalysisDetailsChartObject

### Call the Validation Global Charts ###
DataLakeBankDetailsChartObject = DataLakeBankDetailsChart()
DataLakeBankDetailsDataTable = DataLakeBankDetailsChartObject.bank_details_datatable()
del DataLakeBankDetailsChartObject


UserTransactionHistoryDataTableObject = UserTransactionHistoryDetailsDataTableChart()
UserTransactionHistoryDataTable = UserTransactionHistoryDataTableObject.user_transaction_history_details_datatable()
del UserTransactionHistoryDataTableObject

### Call the Validation Project Wise Charts ###
DataLakeUserDetailsChartObject = DataLakeUserDetailsChart()
DataLakeUserDetailsDataTable = DataLakeUserDetailsChartObject.user_details_datatable()
del DataLakeUserDetailsChartObject


### Sample Chart Content ###
cost_chartContent1 = dbc.Row(
    [
        html.H5("Cost Project Chart", id="dummy1"),
        dbc.Col(
            dcc.Loading(
                children=[dcc.Graph(id="chart-id-1")],
                color="#119DFF",
                type="cube",
            ),
            md=12,
            style={"textAlign": "center"},
        ),
    ],
)

cost_chartContent2 = dbc.Row(
    [
        html.H5("Cost Time Chart"),
        dbc.Col(
            dcc.Loading(
                children=[dcc.Graph(id="chart-id-2")], color="#119DFF", type="cube",
            ),
            md=12,
            style={"textAlign": "center"},
        ),
    ],
)


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)
dashboardChartContentLayout = dbc.Row(
    [], id="user-profile-chart-div", style={"padding-top": "15px"}
)
page_layout = html.Div(
    [
        dcc.Store(id="side_click"),
        dcc.Location(id="url"),
        navbarTemplate,
        sidebarTemplate,
        content,
    ],
)
app.layout = page_layout


@callback(
    Output("devEngineeringTabsDiv", "children"),
    [Input("devEngineeringTabs", "active_tab")],
)
def switch_dev_tab(at):

    switcher = {
        "dev_global_tab1": UserAnalysisDescriptionStatsTreeChart,
        "dev_global_tab2": UserAnalysisDescriptionStatsSunBurstChart,
        # "dev_global_tab3": UserAnalysisDescriptionStatsEffortChart,
    }
    if switcher.get(at):
        return switcher[at]
    else:
        return html.P("This shouldn't ever be displayed...")


@app.callback(
    Output("sampleOutput", "children"), [Input("development_1_tab_1_input", "value")]
)
def output_text(value):
    return value


### TOGGLE-SIDEBAR CALLBACK ###
@callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],
    [Input("btn_sidebar", "n_clicks")],
    [State("side_click", "data"),],
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = "SHOW"

    return sidebar_style, content_style, cur_nclick


### RENDER PAGE CONTENT  ###
@callback(
    Output("page-content", "children"), [Input("url", "pathname")],
)
def render_page_content(pathname):
    # if pathname in ["/dash/", "/"]:
        # firstLevelDashboard = dashboardTopMetricsLayout
        # chartDashboardLayout = dashboardChartContentLayout
        # return firstLevelDashboard, chartDashboardLayout
    if pathname in ["/dash/", "/", "/user_profile"]:
        return UserProfileChart
    elif pathname == "/eda":
        return UserAnalysisDescriptionStatsLayout
    elif pathname == "/transaction_network":
        return UserAnalysisTransactionNetworkGraphChart
    elif pathname == "/pattern_analysis":
        return PatternAnalysisDetailsDataTable
    elif pathname == "/transaction_history":
        return UserTransactionHistoryDataTable
    elif pathname == "/case_user_details":
        return DataLakeUserDetailsDataTable
    elif pathname == "/bank_details":
        return DataLakeBankDetailsDataTable
    else:
        return dbc.Row(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


user_data = {
    "#001": {
        "name": "Kranthi",
        "address": "Bangalore, India",
        "email": "gkranthi.kiran.99@gmail.com",
        "mobile": "8698570081",
        "aadhar_no": "460479158912",
        "pan_no": "HXMPK9385L",
        "picture": "assets/icons/man.png",
    }
}


def layout_update_postprocessing(fig):
    fig.update_layout(
        xaxis={
            "showgrid": False,
            "showline": True,
            # "mirror": True,  # Enable both to show borders on plot
            # "ticks": "outside",
            "linewidth": 1.5,
            "linecolor": "black",
            "ticklabeloverflow": "allow",
        },
        yaxis={
            "showgrid": False,
            "showline": True,
            # "mirror": True,
            # "ticks": "outside",
            "linewidth": 1.5,
            "linecolor": "black",
            "ticklabeloverflow": "allow",
        },
        # paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
        autosize=True,
    )

    return fig


def create_nodes_and_edges(df, cur_user_id, cur_user_name, cur_bank_name):
    t = df.copy()

    def beneficiary_na_filler(row):
        ben_id = row['beneficiary_name']
        if pd.isna(ben_id):
            # ref_no = row['Ref No./Cheque No.']
            # if pd.isna(ref_no):
            desc = row['Description']
            return desc
            # return ref_no
        return ben_id

    t['desc'] = t.apply(lambda x: beneficiary_na_filler(x), axis=1)
    t['index'] = t.index
    t['beneficiary_id'] = t.apply(
        lambda x: f"#Unknown-{x['index']}" if pd.isna(x['beneficiary_id']) else x['beneficiary_id'], axis=1)

    t.rename({
        "Txn Date": "Date",
        "Amount": "TransactionAmt"
    }, axis=1, inplace=True)

    # t['Source'] = None
    # t['Target'] = None

    t['Source'] = t.apply(lambda x: cur_user_id if x['is_debt'] == "Debit" else x['beneficiary_id'], axis=1)
    t['Source'] = t.apply(lambda x: x['beneficiary_id'] if x['is_debt'] == "Credit" else cur_user_id, axis=1)

    t['Target'] = t.apply(lambda x: x['beneficiary_id'] if x['is_debt'] == "Debit" else cur_user_id, axis=1)
    t['Target'] = t.apply(lambda x: cur_user_id if x['is_debt'] == "Credit" else x['beneficiary_id'], axis=1)

    def get_top_freq_bens(t, top_N=10):
        return t['beneficiary_id'].value_counts()[: top_N].index.tolist()

    t = t[t['beneficiary_id'].isin(get_top_freq_bens(t))]

    edges = t[['TransactionAmt', 'Source', 'Target', 'Date']].copy()

    nodes1 = t.groupby(['beneficiary_id'])['beneficiary_name'].unique().reset_index()
    nodes2 = t.groupby(['beneficiary_id'])['beneficiary_bank'].unique().reset_index()

    nodes1['beneficiary_name'] = nodes1['beneficiary_name'].apply(lambda x: x[0])
    nodes2['beneficiary_bank'] = nodes2['beneficiary_bank'].apply(lambda x: x[0])

    nodes = pd.merge(nodes1, nodes2, on=['beneficiary_id'], how='inner')

    nodes.loc[nodes.shape[0]] = [cur_user_id, cur_user_name, cur_bank_name]
    nodes = nodes.reindex(index=nodes.index[::-1])
    nodes.reset_index(drop=True, inplace=True)

    print(nodes.head())

    nodes.rename({
        "beneficiary_id": "Account",
        "beneficiary_name": "CustomerName",
        "beneficiary_bank": "Type",
    }, axis=1, inplace=True)

    nodes['CustomerName'] = nodes['CustomerName'].astype(str)
    nodes['Type'] = nodes['Type'].astype(str)

    return nodes, edges


def get_parsable_csv_path(case_id, user_id):
    # df = pd.read_csv("saved/master_db.csv")
    df = pd.read_csv("http://20.231.200.146:9000/master_db.csv")
    res = df[(df['Case ID'] == case_id) & (df['POI ID'] == user_id)]['POI Bank Statement'].values[0]

    return res


def parsed_csv_into_df(path="#56789_#004_2023-02-05-00-53-47.csv"):
    path = f"http://20.231.200.146:9000/bank_statments/{urllib.parse.quote_plus(path)}"
    data = pd.read_csv(path, skiprows=1)

    mapped_cols = []
    # data.columns = [i.strip() for i in data.columns.tolist()]
    data.columns = [i.replace('_', '').strip() for i in data.columns.tolist()]
    for x in data.columns:
        if x in ['Date', 'TXN DATE', 'Trans Date and Time', 'Posting Date']:
            mapped_cols.append('Txn Date')
        elif x in ['Narration', 'Narration details', 'DESCRIPTION REFERENCE', 'Transaction Particulars', 'Transaction Details',
                   'DESCRIPTION', 'Description', '___________________________________________\nDESCRIPTION']:
            mapped_cols.append('Description')
        elif x in ['Withdrawal Amt.', 'DEBITS', 'Debit', 'Withdrawal', 'WITH DRAWALS']:
            mapped_cols.append('Debit')
        elif x in ['Deposit Amt.', 'CREDITS', 'Credit', 'Deposit', 'DEPOSITS']:
            mapped_cols.append('Credit')
        elif x in ['BALANCE', 'Balance', 'Closing Balance']:
            mapped_cols.append('Balance')
        else:
            mapped_cols.append(x)
    data.columns = mapped_cols
    data = data[data['Debit'] != 'WITH DRAWALS']
    data['Debit'] = data['Debit'].fillna(0).astype(str).apply(
        lambda x: x.replace('Dr', '').replace(',', '').strip()).astype(np.float)
    data['Credit'] = data['Credit'].fillna(0).astype(str).apply(
        lambda x: x.replace('Cr', '').replace(',', '').strip()).astype(np.float)
    data['Balance'] = data['Balance'].fillna(0).astype(str).apply(
        lambda x: x.replace('Dr', '').replace('Cr', '').replace(',', '').strip()).astype(np.float)
    data = data[data['Txn Date'] != '03-JUN-2017 03-JUN-2017']

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

    # def get_beneficiary_id(desc):
    #     if len(desc.split("/")) == 7:
    #         bene_id = desc.split("/")[-2].strip()
    #         return bene_id
    #     else:
    #         return None
    def get_beneficiary_id(desc):
        if len(desc.split("/")) == 7:
            bene_id = desc.split("/")[-2].strip()
            return bene_id
        elif len(desc.split("/")) == 3:
            bene_id = desc.split("/")[-2].strip()
            return bene_id
        elif len(desc.split("/")) == 4:
            bene_id = desc.split("/")[-2].strip()
            return bene_id
        elif len(desc.split("/")) == 5:
            bene_id = desc.split("/")[-3].strip()
            return bene_id
        elif len(desc.split("/")) == 6:
            bene_id = desc.split("/")[-3].strip()
            return bene_id

    def get_beneficiary_name(desc):
        if len(desc.split("/")) == 7:
            bene_id = desc.split("/")[-4].strip()
            return bene_id
        else:
            return None

    def get_beneficiary_bank(desc):
        if len(desc.split("/")) == 7:
            bene_id = desc.split("/")[-3].strip()
            return bene_id
        else:
            return None

    def get_debit_or_credit_field(df):
        # df['Debit'] = df['Debit'].apply(lambda x: None if x.strip() == "" else x)
        # df['Credit'] = df['Credit'].apply(lambda x: None if x.strip() == "" else x)

        df['Debit'].fillna(0, inplace=True)
        df['Credit'].fillna(0, inplace=True)

        df['Debit'] = df['Debit'].astype(np.float)
        df['Credit'] = df['Credit'].astype(np.float)

        df['is_debt'] = df['Debit'].apply(lambda x: "Debit" if x > 0 else "Credit")

        return df

    data['type_of_transaction'] = data['Description'].apply(lambda x: get_transaction_type(x))
    data['beneficiary_id'] = data['Description'].apply(lambda x: get_beneficiary_id(x))
    data['beneficiary_name'] = data['Description'].apply(lambda x: get_beneficiary_name(x))
    data['beneficiary_bank'] = data['Description'].apply(lambda x: get_beneficiary_bank(x))
    data['Amount'] = data['Debit'] + data['Credit']
    data = get_debit_or_credit_field(data)

    # print(data.columns.tolist())

    return data


@app.callback(
    Output("user_analysis_transaction_network_chart", "figure"),
    [Input("case_id", "value"), Input("user_id", "value")]  # Input("username", "value")
)
def user_network_chart(case_id, user_id):
    if not user_id:
        return go.Figure()
    if not case_id:
        return go.Figure()

    # if type(user_transaction_df) != pd.DataFrame:
    #     user_transaction_df = pd.read_csv("saved/parsed_data.csv", parse_dates=['Txn Date', 'Value Date'])

    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    cur_df = parsed_csv_into_df(path=parsable_csv_path)

    # cur_df = user_transaction_df.copy()

    # if not user_id:
    #     return go.Figure()
    #
    # df = pd.read_csv("saved/parsed_data.csv")

    df = pd.read_csv("saved/master_db.csv")
    cur_user_name = df[(df['Case ID'] == case_id) & (df['POI ID'] == user_id)]['POI Name'].values[0]

    cur_bank_name = "SBI"  # TODO
    #
    # print(user_id, cur_user_name, cur_bank_name)

    node1, edge1 = create_nodes_and_edges(cur_df, cur_user_id=user_id, cur_user_name=cur_user_name, cur_bank_name=cur_bank_name)

    AccountToSearch = user_id

    # print(AccountToSearch)
    # print(edge1.head())

    edge1 = edge1[
        (edge1['Source'].apply(lambda x: False if "#Unknown" in x else True)) &
        (edge1['Target'].apply(lambda x: False if "#Unknown" in x else True))]
    edge1.reset_index(drop=True, inplace=True)

    node1 = node1[node1['Account'].apply(lambda x: False if "#Unknown" in x else True)]
    node1.reset_index(drop=True, inplace=True)

    accountSet = set()  # contain unique account
    for index in range(0, len(edge1)):
        accountSet.add(edge1['Source'][index])
        accountSet.add(edge1['Target'][index])

    # to define the centric point of the networkx layout
    shells = []
    shell1 = []
    shell1.append(AccountToSearch)
    shells.append(shell1)
    shell2 = []
    for ele in accountSet:
        if ele != AccountToSearch:
            shell2.append(ele)
    shells.append(shell2)

    G = nx.from_pandas_edgelist(edge1, 'Source', 'Target', ['Source', 'Target', 'TransactionAmt', 'Date'],
                                create_using=nx.MultiDiGraph())
    nx.set_node_attributes(G, node1.set_index('Account')['CustomerName'].to_dict(), 'CustomerName')
    nx.set_node_attributes(G, node1.set_index('Account')['Type'].to_dict(), 'Type')
    # pos = nx.layout.spring_layout(G)
    # pos = nx.layout.circular_layout(G)
    # nx.layout.shell_layout only works for more than 3 nodes
    if len(shell2) > 1:
        pos = nx.drawing.layout.shell_layout(G, shells)
    else:
        pos = nx.drawing.layout.spring_layout(G)
    for node in G.nodes:
        G.nodes[node]['pos'] = list(pos[node])

    if len(shell2) == 0:
        traceRecode = []  # contains edge_trace, node_trace, middle_node_trace

        node_trace = go.Scatter(x=tuple([1]), y=tuple([1]), text=tuple([str(AccountToSearch)]),
                                textposition="bottom center",
                                mode='markers+text',
                                marker={'size': 50, 'color': 'LightSkyBlue'})
        traceRecode.append(node_trace)

        node_trace1 = go.Scatter(x=tuple([1]), y=tuple([1]),
                                 mode='markers',
                                 marker={'size': 50, 'color': 'LightSkyBlue'},
                                 opacity=0)
        traceRecode.append(node_trace1)

        figure = {
            "data": traceRecode,
            "layout": go.Layout(
                title='Top 10 Frequent Beneficiaries',
                showlegend=False,
                                margin={'b': 40, 'l': 40, 'r': 40, 't': 40},
                                xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                                yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                                height=600
                                )}
        return figure

    traceRecode = []  # contains edge_trace, node_trace, middle_node_trace
    ############################################################################################################################################################
    colors = list(Color('lightcoral').range_to(Color('darkred'), len(G.edges())))
    colors = ['rgb' + str(x.rgb) for x in colors]

    index = 0
    for edge in G.edges:
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        weight = float(G.edges[edge]['TransactionAmt']) / max(edge1['TransactionAmt']) * 10
        trace = go.Scatter(x=tuple([x0, x1, None]), y=tuple([y0, y1, None]),
                           mode='lines',
                           line={'width': weight},
                           marker=dict(color=colors[index]),
                           line_shape='spline',
                           opacity=1)
        traceRecode.append(trace)
        index = index + 1
    ###############################################################################################################################################################
    node_trace = go.Scatter(x=[], y=[], hovertext=[], text=[], mode='markers+text', textposition="bottom center",
                            hoverinfo="text", marker={'size': 50, 'color': 'LightSkyBlue'})

    index = 0
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        hovertext = "CustomerName: " + str(G.nodes[node]['CustomerName']) + "<br>" + "AccountType: " + str(
            G.nodes[node]['Type'])
        text = node1['Account'][index]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['hovertext'] += tuple([hovertext])
        node_trace['text'] += tuple([text])
        index = index + 1

    traceRecode.append(node_trace)
    ################################################################################################################################################################
    middle_hover_trace = go.Scatter(x=[], y=[], hovertext=[], mode='markers', hoverinfo="text",
                                    marker={'size': 20, 'color': 'LightSkyBlue'},
                                    opacity=0)

    index = 0
    for edge in G.edges:
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        hovertext = "From: " + str(G.edges[edge]['Source']) + "<br>" + "To: " + str(
            G.edges[edge]['Target']) + "<br>" + "TransactionAmt: " + str(
            G.edges[edge]['TransactionAmt']) + "<br>" + "TransactionDate: " + str(G.edges[edge]['Date'])
        middle_hover_trace['x'] += tuple([(x0 + x1) / 2])
        middle_hover_trace['y'] += tuple([(y0 + y1) / 2])
        middle_hover_trace['hovertext'] += tuple([hovertext])
        index = index + 1

    traceRecode.append(middle_hover_trace)
    #################################################################################################################################################################
    figure = {
        "data": traceRecode,
        "layout": go.Layout(
            title='Top 10 Frequent Beneficiaries',
            showlegend=False, hovermode='closest',
                            margin={'b': 40, 'l': 40, 'r': 40, 't': 40},
                            xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                            yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                            height=600,
                            clickmode='event+select',
                            annotations=[
                                dict(
                                    ax=(G.nodes[edge[0]]['pos'][0] + G.nodes[edge[1]]['pos'][0]) / 2,
                                    ay=(G.nodes[edge[0]]['pos'][1] + G.nodes[edge[1]]['pos'][1]) / 2, axref='x',
                                    ayref='y',
                                    x=(G.nodes[edge[1]]['pos'][0] * 3 + G.nodes[edge[0]]['pos'][0]) / 4,
                                    y=(G.nodes[edge[1]]['pos'][1] * 3 + G.nodes[edge[0]]['pos'][1]) / 4, xref='x',
                                    yref='y',
                                    showarrow=True,
                                    arrowhead=3,
                                    arrowsize=4,
                                    arrowwidth=1,
                                    opacity=1
                                ) for edge in G.edges]
                            )}

    fig = go.Figure(figure)

    fig = layout_update_postprocessing(fig)

    fig.update_layout(
        # title_text="Transaction Types",
        # width=500,
        height=600,
    )
    return fig


@app.callback(
    Output("user_transaction_analysis_p11", "figure"),
    [Input("case_id", "value"), Input("user_id", "value"),]
)
def user_eda_chart_p11(case_id, user_id):
    # global user_transaction_df
    if not user_id:
        return go.Figure()
    if not case_id:
        return go.Figure()

    # if type(user_transaction_df) != pd.DataFrame:
    #     user_transaction_df = pd.read_csv("saved/parsed_data.csv", parse_dates=['Txn Date', 'Value Date'])

    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    cur_df = parsed_csv_into_df(path=parsable_csv_path)

    # cur_df = user_transaction_df.copy()

    agg = cur_df.groupby(['type_of_transaction'])['is_debt'].count().reset_index()
    agg.columns = ['type_of_transaction', 'count']
    agg['perc'] = np.round((agg['count'] / agg['count'].sum()) * 100, 2)

    fig = go.Figure(
        data=[
            go.Pie(
                labels=agg['type_of_transaction'],
                values=agg['count'],
                hovertemplate=
                '<b> Transaction : %{label}</b> <br>'
                ' Count : %{value}<br>'
            )
        ]
    )

    fig.update_layout(
        title_text="Transaction Types",
        width=500,
        height=500,
    )

    fig = layout_update_postprocessing(fig)

    return fig


@app.callback(
    Output("user_transaction_analysis_p12", "figure"),
    [Input("case_id", "value"), Input("user_id", "value"),]
)
def user_eda_chart_p12(case_id, user_id):
    # global user_transaction_df
    if not user_id:
        return go.Figure()
    if not case_id:
        return go.Figure()

    # if type(user_transaction_df) != pd.DataFrame:
    #     user_transaction_df = pd.read_csv("saved/parsed_data.csv", parse_dates=['Txn Date', 'Value Date'])

    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    cur_df = parsed_csv_into_df(path=parsable_csv_path)

    # cur_df = user_transaction_df.copy()

    agg = cur_df.groupby(['is_debt', 'type_of_transaction'])['Amount'].sum().reset_index()

    agg['perc'] = agg['Amount'].values
    agg.loc[agg['is_debt'] == 0, 'perc'] /= agg[agg['is_debt'] == 0]['Amount'].sum()
    agg.loc[agg['is_debt'] == 1, 'perc'] /= agg[agg['is_debt'] == 1]['Amount'].sum()

    agg['perc'] *= 100

    fig = go.Figure()
    fig1 = px.sunburst(
        agg,
        path=["is_debt", "type_of_transaction"],
        values="Amount",
        # hover_data=["perc"],
    )

    fig.add_trace(
        go.Sunburst(
            ids=fig1["data"][0]["ids"].tolist(),
            labels=fig1["data"][0]["labels"].tolist(),
            parents=fig1["data"][0]["parents"].tolist(),
            values=fig1["data"][0]["values"].tolist(),
            # customdata=fig1["data"][0]["customdata"],
            branchvalues=fig1["data"][0]["branchvalues"],
            hovertemplate="<b> %{label} </b> <br>" + " Amount : %{value:.2f}<br>"
                          # + " Perc : %{customdata[0]:.2f}<br>"
        )
    )  # , 1, idx+1
    del fig1

    fig.update_layout(
        title_text="Sunburst Distribution",
        width=500,
        height=500,
    )

    fig = layout_update_postprocessing(fig)

    return fig


# @app.callback(
#     Output("user_transaction_analysis_p13", "figure"),
#     Input("user_id", "value"),
# )
# def user_network_chart_p13(user_id):
#     if not user_id:
#         return go.Figure()
#
#     G = nx.random_geometric_graph(200, 0.125)
#
#     edge_x = []
#     edge_y = []
#     for edge in G.edges():
#         x0, y0 = G.nodes[edge[0]]['pos']
#         x1, y1 = G.nodes[edge[1]]['pos']
#         edge_x.append(x0)
#         edge_x.append(x1)
#         edge_x.append(None)
#         edge_y.append(y0)
#         edge_y.append(y1)
#         edge_y.append(None)
#
#     edge_trace = go.Scatter(
#         x=edge_x, y=edge_y,
#         line=dict(width=0.5, color='#888'),
#         hoverinfo='none',
#         mode='lines')
#
#     node_x = []
#     node_y = []
#     for node in G.nodes():
#         x, y = G.nodes[node]['pos']
#         node_x.append(x)
#         node_y.append(y)
#
#     node_trace = go.Scatter(
#         x=node_x, y=node_y,
#         mode='markers',
#         hoverinfo='text',
#         marker=dict(
#             showscale=True,
#             # colorscale options
#             # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
#             # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
#             # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#             colorscale='YlGnBu',
#             reversescale=True,
#             color=[],
#             size=10,
#             colorbar=dict(
#                 thickness=15,
#                 title='Node Connections',
#                 xanchor='left',
#                 titleside='right'
#             ),
#             line_width=2))
#
#     node_adjacencies = []
#     node_text = []
#     for node, adjacencies in enumerate(G.adjacency()):
#         node_adjacencies.append(len(adjacencies[1]))
#         node_text.append('# of connections: ' + str(len(adjacencies[1])))
#
#     node_trace.marker.color = node_adjacencies
#     node_trace.text = node_text
#
#     fig = go.Figure(data=[edge_trace, node_trace],
#                     layout=go.Layout(
#                         # title='<br>Network graph made with Python',
#                         titlefont_size=16,
#                         showlegend=False,
#                         hovermode='closest',
#                         margin=dict(b=20, l=5, r=5, t=40),
#                         # annotations=[dict(
#                         #     text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
#                         #     showarrow=False,
#                         #     xref="paper", yref="paper",
#                         #     x=0.005, y=-0.002)],
#                         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
#                     )
#
#     # fig = layout_update_postprocessing(fig)
#
#     return fig
#

@app.callback(
    Output("user_transaction_analysis_p21", "figure"),
    [Input("case_id", "value"), Input("user_id", "value"),]
)
def user_eda_chart_p21(case_id, user_id):
    # global user_transaction_df
    if not user_id:
        return go.Figure()
    if not case_id:
        return go.Figure()

    # if type(user_transaction_df) != pd.DataFrame:
    #     user_transaction_df = pd.read_csv("saved/parsed_data.csv", parse_dates=['Txn Date', 'Value Date'])

    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    cur_df = parsed_csv_into_df(path=parsable_csv_path)

    # cur_df = user_transaction_df.copy()

    cur_df['Txn Date'] = pd.to_datetime(cur_df['Txn Date'])

    cur_df.set_index("Txn Date", inplace=True)
    agg = cur_df.groupby([pd.Grouper(freq="D"), 'is_debt'])['Amount'].sum().reset_index()

    fig = px.line(
        agg,
        x="Txn Date",
        y="Amount",
        color="is_debt",
        markers=True,
        labels={"is_debt": "Type"},
    )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        title_text="Volume of Transactions",
        # width=500,
        # height=500,
    )

    fig = layout_update_postprocessing(fig)

    return fig


@app.callback(
    Output("user_transaction_analysis_p22", "figure"),
    [Input("case_id", "value"), Input("user_id", "value"),]
)
def user_eda_chart_p22(case_id, user_id):
    # global user_transaction_df
    if not user_id:
        return go.Figure()
    if not case_id:
        return go.Figure()

    # if type(user_transaction_df) != pd.DataFrame:
    #     user_transaction_df = pd.read_csv("saved/parsed_data.csv", parse_dates=['Txn Date', 'Value Date'])

    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    cur_df = parsed_csv_into_df(path=parsable_csv_path)

    cur_df['Txn Date'] = pd.to_datetime(cur_df['Txn Date'])

    cur_df.set_index("Txn Date", inplace=True)
    agg = cur_df.groupby([pd.Grouper(freq="D"), 'is_debt'])['Amount'].count().reset_index()

    fig = px.line(
        agg,
        x="Txn Date",
        y="Amount",
        color="is_debt",
        markers=True,
        labels={"is_debt": "Type"},
    )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        title_text="Frequency of Transactions",
    )
    fig = layout_update_postprocessing(fig)

    return fig


# @app.callback(
#     Output("user_transaction_analysis_p31", "figure"),
#     [Input("case_id", "value"), Input("user_id", "value"),]
# )
# def user_network_chart_p31(case_id, user_id):
#     if not user_id:
#         return go.Figure()
#
#     G = nx.random_geometric_graph(200, 0.125)
#
#     edge_x = []
#     edge_y = []
#     for edge in G.edges():
#         x0, y0 = G.nodes[edge[0]]['pos']
#         x1, y1 = G.nodes[edge[1]]['pos']
#         edge_x.append(x0)
#         edge_x.append(x1)
#         edge_x.append(None)
#         edge_y.append(y0)
#         edge_y.append(y1)
#         edge_y.append(None)
#
#     edge_trace = go.Scatter(
#         x=edge_x, y=edge_y,
#         line=dict(width=0.5, color='#888'),
#         hoverinfo='none',
#         mode='lines')
#
#     node_x = []
#     node_y = []
#     for node in G.nodes():
#         x, y = G.nodes[node]['pos']
#         node_x.append(x)
#         node_y.append(y)
#
#     node_trace = go.Scatter(
#         x=node_x, y=node_y,
#         mode='markers',
#         hoverinfo='text',
#         marker=dict(
#             showscale=True,
#             # colorscale options
#             # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
#             # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
#             # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#             colorscale='YlGnBu',
#             reversescale=True,
#             color=[],
#             size=10,
#             colorbar=dict(
#                 thickness=15,
#                 title='Node Connections',
#                 xanchor='left',
#                 titleside='right'
#             ),
#             line_width=2))
#
#     node_adjacencies = []
#     node_text = []
#     for node, adjacencies in enumerate(G.adjacency()):
#         node_adjacencies.append(len(adjacencies[1]))
#         node_text.append('# of connections: ' + str(len(adjacencies[1])))
#
#     node_trace.marker.color = node_adjacencies
#     node_trace.text = node_text
#
#     fig = go.Figure(data=[edge_trace, node_trace],
#                     layout=go.Layout(
#                         # title='<br>Network graph made with Python',
#                         titlefont_size=16,
#                         showlegend=False,
#                         hovermode='closest',
#                         margin=dict(b=20, l=5, r=5, t=40),
#                         # annotations=[dict(
#                         #     text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
#                         #     showarrow=False,
#                         #     xref="paper", yref="paper",
#                         #     x=0.005, y=-0.002)],
#                         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
#                     )
#
#     # fig = layout_update_postprocessing(fig)
#
#     return fig


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
    data["Txn Date_temp"] = pd.to_datetime(data["Txn Date"])
    data['Holiday'] = np.where(data['Txn Date_temp'].apply(lambda d: d in in_holidays) == True, 1, 0)

    data.columns = [i.strip() for i in data.columns.tolist()]

    return data


@app.callback(
    Output("pattern-details-datatable", "data"),
    [
        Input("pattern_filter_names", "value"),
        Input("case_id", "value"),
        Input("user_id", "value"),
    ],
)
def refresh_pattern_details(filters, case_id, user_id):
    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    print(case_id, user_id, parsable_csv_path)
    df = parsed_csv_into_df(path=parsable_csv_path)

    # df = pd.read_csv(
    #     "saved/user01_vinneth_2023-02-04-15-49-56_.csv")  # pd.read_csv(r"C:\Users\gandem\Desktop\shit\police-hack\aml-squad\saved\ifsc_global_data.csv")
    df = pp_for_pattern_analysis(df)
    # filters = ['High Volume Debit', 'High Volume Credit', 'Is_Weekend', 'Holiday']  # , 'type_of_transaction'

    to_show_cols = ['Txn Date', 'Description', 'Debit', 'Credit', 'type_of_transaction',
                    'High Volume Debit', 'High Volume Credit', 'Is_Weekend', 'Holiday']

    df['res'] = 0
    for col in filters:
        df['res'] += df[col]

    df = df[df['res'] == len(filters)]
    df = df[to_show_cols]

    return df.to_dict("records")


@app.callback(
    Output("bank-details-datatable", "data"),
    [
        Input("bank_details_bank_name", "value"),
    ]
)
def refresh_bank_details(bank_names):
    df = bank_details_df[bank_details_df['BANK'].isin(bank_names)].copy()

    return df.to_dict("records")


@app.callback(
    Output("user-details-datatable", "data"),
    [
        Input("case_id", "value"),
    ]
)
def refresh_case_user_details(case_id):
    df = pd.read_csv("saved/master_db.csv")
    df = df[df['Case ID'] == case_id]

    return df.to_dict("records")


@app.callback(
    Output('user_id', 'options'),
    [Input("case_id", "value"),])
def currentCaseUserList(case_id):
    try:
        df = pd.read_csv("saved/master_db.csv")
        df = df[df['Case ID'] == case_id]

        obj = df['POI ID'].unique().tolist()
        return obj
    except AttributeError:
        return []
    except KeyError:
        return []


@app.callback(
    Output('username', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"),])
def currentUserName(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    df = pd.read_csv("saved/master_db.csv")
    res = df[(df['Case ID'] == case_id) & (df['POI ID'] == user_id)]['POI Name'].values[0]

    return res


@app.callback(
    Output('userid', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"), ])
def currentUserID(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    return user_id


@app.callback(
    Output('userpan', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"), ])
def currentUserPAN(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    df = pd.read_csv("saved/master_db.csv")
    res = df[(df['Case ID'] == case_id) & (df['POI ID'] == user_id)]['POI PAN Card'].values[0]

    return res


@app.callback(
    Output('useraadhar', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"), ])
def currentUserAadhaar(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    df = pd.read_csv("saved/master_db.csv")
    res = df[(df['Case ID'] == case_id) & (df['POI ID'] == user_id)]['POI Aadhaar'].values[0]

    return res


@app.callback(
    Output('userinitBS', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"), ])
def currentUserInitBS(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    cur_df = parsed_csv_into_df(path=parsable_csv_path)

    cur_df['Txn Date'] = pd.to_datetime(cur_df['Txn Date'])

    min_date = str(min(cur_df['Txn Date'].dt.date))

    return min_date


@app.callback(
    Output('userlatBS', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"), ])
def currentUserLatestBS(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    parsable_csv_path = get_parsable_csv_path(case_id, user_id)
    cur_df = parsed_csv_into_df(path=parsable_csv_path)

    cur_df['Txn Date'] = pd.to_datetime(cur_df['Txn Date'])

    max_date = str(max(cur_df['Txn Date'].dt.date))

    return max_date


@app.callback(
    Output('usercaseID', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"), ])
def currentUserCaseID(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    df = pd.read_csv("saved/master_db.csv")
    res = df[(df['Case ID'] == case_id) & (df['POI ID'] == user_id)]['Case ID'].values[0]

    return res


@app.callback(
    Output('usercaseDesc', 'children'),
    [Input("case_id", "value"), Input("user_id", "value"), ])
def currentUserCaseDesc(case_id, user_id):
    if not case_id:
        return ""
    if not user_id:
        return ""

    df = pd.read_csv("saved/master_db.csv")
    res = df[(df['Case ID'] == case_id) & (df['POI ID'] == user_id)]['Case Description'].values[0]

    return res


@app.callback(
    Output('userphoto', 'children'),
    [Input("user_id", "value")])
def currentUserPhoto(user_id):
    try:
        obj = "assets/icons/man.png"  # user_data[user_id]['picture']
        return html.Img(src=obj, height="150px")
    except AttributeError or KeyError:
        return ''
    except KeyError:
        return ''


bank_details_df = pd.read_csv("saved/ifsc_global_data.csv")  # pd.read_csv(r"C:\Users\gandem\Desktop\shit\police-hack\aml-squad\saved\ifsc_global_data.csv")


# @app.callback(
#     Output('email', 'children'),
#     [Input("user_id", "value")])
# def currentUserEmail(user_id):
#     try:
#         email = user_data[user_id]['email']
#         return email
#     except AttributeError:
#         return ''


#

# ### DEVELOPMENT COLLAPSE  ###
# @callback(
#     Output("devCollapse", "is_open"),
#     [Input("eda", "n_clicks")],
#     [State("devCollapse", "is_open")],
# )
# def development_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open


# @callback(
#     Output("valCollapse", "is_open"),
#     [Input("transaction-network", "n_clicks")],
#     [State("valCollapse", "is_open")],
# )
# def validation_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open


# ### TOGGLE SIDEBAR ICON  ###
# @callback(
#     output=(
#         Output("eda", "className"),
#         Output("sidebarPlusIcon", "className"),
#     ),
#     inputs=dict(n=Input("sidebarPlusIcon", "n_clicks")),
#     state=dict(sidebar_current_classname=State("eda", "className")),
# )
# def toggle_sidebar_icon(n, sidebar_current_classname):
#     if sidebar_current_classname == "":
#         return "collapsed", "fas fa-minus-square sidebar-icon-padding"
#     return "", "fas fa-plus-square sidebar-icon-padding"


@app.callback(
    Output("user-profile-chart-div", "children"),
    Input("costProject", "n_clicks"),
    Input("costTime", "n_clicks"),
    Input("quality_bugs_trend_button", "n_clicks"),
    Input("quality_bugs_count_button", "n_clicks"),
    # Input("delivery_plot1_button", "n_clicks"),
    Input("delivery_plot2_button", "n_clicks"),
    Input("quality_tile_value_button", "n_clicks"),
    # Input("quality_tile_comparison_button", "n_clicks"),
    Input("delivery_tile_value_button", "n_clicks"),
    # Input("delivery_tile_comparison_button", "n_clicks"),
    Input("cost_tile_value_button", "n_clicks"),
    # Input("cost_tile_comparison_button", "n_clicks"),
)
def displayClick(
    btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8,  # btn9, btn10, btn11, btn12
):
    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    if "costProject" in changed_id:
        msg = cost_chartContent1
    elif "costTime" in changed_id:
        msg = cost_chartContent2
    elif "quality_bugs_trend_button" in changed_id:
        msg = qualityBugTrendChart
    elif "quality_bugs_count_button" in changed_id:
        msg = qualityBugCountChart
    elif "delivery_plot1_button" in changed_id:
        msg = deliveryOntimeTrendChart
    elif "delivery_plot2_button" in changed_id:
        msg = deliveryReleaseTrendChart
    elif "quality_tile_value_button" in changed_id:
        msg = qualityBugTrendMetricChart
    # elif "quality_tile_comparison_button" in changed_id:
    #     msg = quality_tile_value_metric_chartContent
    elif "delivery_tile_value_button" in changed_id:
        msg = deliveryOntimeMetricChart
    # elif "delivery_tile_comparison_button" in changed_id:
    #     msg = delivery_tile_value_metric_chartContent
    elif "cost_tile_value_button" in changed_id:
        msg = None
    # elif "cost_tile_comparison_button" in changed_id:
    #     msg = None
    elif "btn-nclicks-3" in changed_id:
        msg = "Button 3 was most recently clicked"
    else:
        msg = ""  #
    return html.Div(msg)


# @app.callback(
#     Output("user_analysis_transaction_network_chart", "figure"),
#     Input("user_analysis_transaction_network__user_id", "value"),
# )
# def plot(user_id):
#     data_canada = px.data.gapminder().query("country == 'Canada'")
#     fig = px.bar(data_canada, x='year', y='pop')
#
#     # fig = layout_update_postprocessing(fig)
#
#     return fig

# plots_callback_manager.attach_to_app(app)
# offcanvas_callback_manager.attach_to_app(app)
# dash_url_helper.setup(app=app, page_layout=page_layout)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080, debug=False)
