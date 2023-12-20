from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('/home/neikara/Téléchargements/h.csv', delimiter=";")

app = Dash(__name__)
app.layout = html.Div([
    # Dropdown to select elements
    dcc.Dropdown(
        id='element-dropdown',
        options=['failed_engine', 'wo', 'nothing'],
    ),
    # Plotly graph
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('element-dropdown', 'value')
)
def update_graph(value):
    dff = df[df['Anomalie_type']==value]
    return px.line(dff, x='lat', y='lon')

if __name__ == '__main__':
    app.run(debug=True)


