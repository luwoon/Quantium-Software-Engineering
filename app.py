from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('output.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Sales increased after the Pink Morsel price increase on the 15th of January, 2021.', style={'textAlign':'center'}),
    dcc.Graph(figure=px.line(df, x='date', y='sales'))
])

if __name__ == '__main__':
    app.run(debug=True)
