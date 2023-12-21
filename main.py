from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

# Tabs
from histograms import histogramTab
from maps import mapsTab
from plotter import plotterTab


tabs = [
    mapsTab,
    histogramTab,
    plotterTab,
]

app = Dash(__name__)
app.layout = html.Div([
    dcc.Tabs(tabs)
])

if __name__ == '__main__':
    app.run(debug=True)
