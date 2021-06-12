import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from Visualizor import *
from HomePage import *

app = dash.Dash()
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])


@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home' or pathname == '/':
        return Homepage()
    elif pathname =='/corona-predictor':
        return state_predictor()
    elif pathname is None or pathname == '/':
        return 'Loading...'
    elif pathname == '/visualize':
        feature_dropdown = featurerender()
        return Campaign_Visualizor(feature_dropdown)


@app.callback(
    Output('output_piegraph', 'children'),
    [Input('feature_dropdown', 'value')
     ]
)
def update_graph(feature):
    graph = visualize_piegraph(feature)
    return graph

@app.callback(
    Output('output_bargraph', 'children'),
    [Input('feature_dropdown', 'value')
     ]
)
def update_graph(feature):
    graph = visualize_bargraph(feature)
    return graph

@app.callback(
    Output('output_linegraph', 'children'),
    [Input('feature_dropdown', 'value')
     ]
)
def update_graph(feature):
    graph = visualize_linegraph(feature)
    return graph

    




if __name__ == '__main__':
    app.run_server(debug=True)
