from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

from loader import maps_data
# df = pd.read_csv('h.csv', delimiter=";")
df = maps_data


mapsTab = dcc.Tab(label='Maps', children=[
    html.H1(children="DashBoard"),
    # Dropdown to select elements
    dcc.Dropdown(
        id='map_anomaly',
        options=[
            {'label': 'Train engine anomaly', 'value': 'failed_engine'},
            {'label': 'Water/Oil cooling anomaly', 'value': 'wo'},
            {'label': 'No anomaly', 'value': 'nothing'}
        ],
        value='nothing'
    ),
    dcc.Graph(id='map', style={'width': '90vh', 'height': '90vh'})
])

@callback(
    Output('map', 'figure'),
    Input('map_anomaly', 'value')
)
def update_graph(value):
    dff = df[df['Anomalie_type']==value]
    fig = go.Figure(go.Scattergeo(
        lat=dff['lat'],
        lon=dff['lon'],
        text=dff['mapped_veh_id'],
        mode='markers',
        marker_color=dff['mapped_veh_id']
    )).update_geos(
        visible=False, resolution=50,
        showcountries=True, countrycolor="Blue"
    ).update_layout(
        geo=dict(
            center=dict(lat=50.5503, lon=4.3517),
            projection_scale=80
        )
    )
    return fig
