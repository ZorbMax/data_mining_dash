import numpy as np
import pandas as pd
from scipy.stats import norm

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objs as go


from loader import hist_data


plotter_attributes = [
    "RS_E_InAirTemp_PC1",
    "RS_E_InAirTemp_PC2",
    "RS_E_WatTemp_PC1",
    "RS_E_WatTemp_PC2",
    "RS_T_OilTemp_PC1",
    "RS_T_OilTemp_PC2",
    "RS_E_OilPress_PC1",
    "RS_E_OilPress_PC2",
    "RS_E_RPM_PC1",
    "RS_E_RPM_PC2",
]

plotter_data = {attribute: hist_data[attribute] for attribute in plotter_attributes}


plotterTab = dcc.Tab(label='Plotter', children=[
    dcc.Dropdown(
        id='plotter-x-dropdown',
        options=plotter_attributes,
        value=plotter_attributes[0]
    ),
    dcc.Dropdown(
        id='plotter-y-dropdown',
        options=plotter_attributes,
        value=plotter_attributes[1]
    ),
    dcc.Graph(figure={}, id='plotter-graph'),
])


@callback(
    Output(component_id='plotter-graph', component_property='figure'),
    Input(component_id='plotter-x-dropdown', component_property='value'),
    Input(component_id='plotter-y-dropdown', component_property='value'),
)
def update_graph(x_value, y_value):
    df = pd.DataFrame({x_value: plotter_data[x_value], y_value: plotter_data[y_value]})
    return px.scatter(df, x=x_value, y=y_value, title='Scatter Plot')

