import numpy as np
import pandas as pd
from scipy.stats import norm

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objs as go


class MultiAttribute:
    def __init__(self, name, *attributes):
        self.name = name
        self.attributes = attributes
        self.column = pd.concat(attributes, ignore_index=True)
        self.mean = self.column.mean()
        self.median = self.column.median()
        self.mode = self.column.mode().iloc[0]
        self.std = self.column.std()

        self.figure = self.make_histogram()

    def make_histogram(self):
        # Create histogram
        fig_hist = go.Figure()
        for attribute in self.attributes:
            fig_hist.add_trace(
                go.Histogram(x=attribute, nbinsx=80, name=attribute.name)
            )
        fig_hist.update_traces(opacity=0.5)

        xmin, xmax = self.column.min(), self.column.max()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, self.mean, self.std) * len(self.attributes[0]) * (xmax - xmin) / 80
        normal_distrib = go.Scatter(x=x, y=p, mode='lines', name='Normal Distribution')
        fig_hist.add_trace(normal_distrib)

        return fig_hist.update_layout(
            barmode="overlay",
            title=f"{self.name} Histogram",
            xaxis=dict(title=self.name),
            yaxis=dict(title='Frequency')
        )


# file_path = "C:/Users/sezne/Downloads/ar41_cleaned.csv"
# file_path = "C:/Users/sezne/Downloads/ar41_for_ulb.csv"
# file_path = "C:/Users/sezne/Downloads/ar41_sample_10k.csv"
# file_path = "C:/Users/sezne/Downloads/ar41_sample_200k.csv"
# file_path = "C:/Users/sezne/Downloads/ar41_for_ulb_mini.csv"
file_path = "h.csv"  # TODO : full file ?
# file_path = "C:/Users/sezne/Downloads/ar41_diff.csv"
hist_data = pd.read_csv(file_path, sep=';')

hist_attributes = [
    MultiAttribute("Air Temperature", hist_data["RS_E_InAirTemp_PC1"], hist_data["RS_E_InAirTemp_PC2"]),
    MultiAttribute("Water Temperature", hist_data["RS_E_WatTemp_PC1"], hist_data["RS_E_WatTemp_PC2"]),
    MultiAttribute("Oil Temperature", hist_data["RS_T_OilTemp_PC1"], hist_data["RS_T_OilTemp_PC2"]),
    MultiAttribute("Oil Pressure", hist_data["RS_E_OilPress_PC1"], hist_data["RS_E_OilPress_PC2"]),
    MultiAttribute("RPM", hist_data["RS_E_RPM_PC1"], hist_data["RS_E_RPM_PC2"]),
    # MultiAttribute("Air Temperature diff",  hist_data["Air_temp_diff"]),
    # MultiAttribute("Water Temperature diff",  hist_data["Water_temp_diff"]),
    # MultiAttribute("Oil Temperature diff",  hist_data["Oil_temp_diff"]),
    # MultiAttribute("Oil Pressure diff",  hist_data["Oil_press_diff"]),
]

histogramTab = dcc.Tab(label='Histograms', children=[
    dcc.RadioItems(
        options=[
            {'label': hist_attributes[i].name, 'value': i} for i in range(len(hist_attributes))
        ],
        value=0,
        id='histogram-radio-item'
    ),
    dcc.Graph(figure={}, id='histogram-graph'),
])


@callback(
    Output(component_id='histogram-graph', component_property='figure'),
    Input(component_id='histogram-radio-item', component_property='value')
)
def update_graph(col_chosen):
    return hist_attributes[col_chosen].figure