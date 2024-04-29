from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('output.csv')

unique_regions = df['region'].unique()

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Sales increased after the Pink Morsel price increase on the 15th of January, 2021.', style={'textAlign':'center'}),
    html.Hr(),
    dcc.RadioItems(
        options=[{'label': 'all', 'value': 'all'}] + [{'label': region, 'value': region} for region in unique_regions], 
        value='All', 
        id='controls-and-radio-item'
    ),
    dcc.Graph(figure={}, id='controls-and-graph')
])

@app.callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    [Input(component_id='controls-and-radio-item', component_property='value')]
)
def update_graph(region_selected):
    if region_selected == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region_selected]
    
    fig = px.line(filtered_df, x='date', y='sales')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
