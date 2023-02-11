import dash
from dash import html
from dash import dcc
import pandas as pd
import datapackage

import dask.dataframe as dd

def load_prices_dask(package_url, columns):
    package = datapackage.Package(package_url)
    resources = package.resources
    dfs = []
    for resource in resources:
        if resource.tabular:
            df = dd.read_csv(resource.descriptor['path'], sample=1000000) # increase the sample size to 1 MB
            df = df[df.columns.intersection(columns)]
            dfs.append(df)
    df = dd.concat(dfs)
    return df.dropna().compute()

oil_df = load_prices_dask('https://datahub.io/core/oil-prices/datapackage.json', ['Date', 'Price'])
gas_df = load_prices_dask('https://datahub.io/core/natural-gas/datapackage.json', ['Date', 'Price'])

print('Oil DataFrame:')
print(oil_df)
print('Natural Gas DataFrame:')
print(gas_df)


# Initialize the dash app
app = dash.Dash()

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='Energy Prices Dashboard'),

    html.Div(children=[
        html.Div(children=[
            dcc.Dropdown(
                id='energy-type-dropdown',
                options=[
                    {'label': 'Oil Prices', 'value': 'oil'},
                    {'label': 'Natural Gas Prices', 'value': 'gas'}
                ],
                value='oil'
            ),
        ], className='six columns'),
        html.Div(children=[
            html.Button(id='submit-button', n_clicks=0, children='Submit')
        ], className='six columns'),
    ], className='row'),

    html.Div(children=[
        dcc.Graph(id='price-graph', figure={
            'data': [{
                'x': oil_df['Date'],
                'y': oil_df['Price'],
                'type': 'line'
            }],
            'layout': {
                'title': 'Oil Prices'
            }
        }),
    ], className='six columns'),

    html.Div(children=[
        dcc.Graph(id='price-histogram', figure={
            'data': [{
                'x': oil_df['Price'],
                'type': 'histogram'
            }],
            'layout': {
                'title': 'Oil Prices Distribution'
            }
        }),
    ], className='six columns'),

    html.Div(children=[
        dcc.Graph(id='price-boxplot', figure={
            'data': [{
                'y': oil_df['Price'],
                'type': 'box'
            }],
            'layout': {
                'title': 'Oil Prices Boxplot'
            }
        }),
    ], className='six columns'),

    html.Div(children=[
        dcc.Graph(id='price-scatterplot', figure={
            'data': [{
                'x': oil_df['Date'],
                'y': oil_df['Price'],
                'mode': 'markers'
            }],
            'layout': {
                'title': 'Oil Prices Scatterplot'
            }
        }),
    ], className='six columns'),

], className='container')


@app.callback(
    dash.dependencies.Output('submit-button', 'n_clicks'),
    [dash.dependencies.Input('submit-button', 'n_clicks')]
)
def update_n_clicks(n_clicks):
    return n_clicks + 1


# Define the callback to update the price graph and histogram
@app.callback(
    dash.dependencies.Output('price-graph', 'figure'),
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('energy-type-dropdown', 'value')]
)
def update_price_graph(n_clicks, energy_type):
    n_clicks = update_n_clicks(n_clicks)
    
    if energy_type == 'oil':
        data = oil_df
    else:
        data = gas_df

    return {
        'data': [{
            'x': data['Date'],
            'y': data['Price'],
            'type': 'line',
            'name': energy_type
        }],
        'layout': {
            'title': f'{energy_type.capitalize()} Prices Over Time',
            'xaxis': {
                'title': 'Year'
            },
            'yaxis': {
                'title': 'Price ($/bbl)'
            }
        }
    }

@app.callback(
    dash.dependencies.Output('price-histogram', 'figure'),
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('energy-type-dropdown', 'value')]
)
def update_price_histogram(n_clicks, energy_type):
    n_clicks = update_n_clicks(n_clicks)
    
    if energy_type == 'oil':
        data = oil_df
    else:
        data = gas_df

    return {
        'data': [{
            'x': data['Price'],
            'type': 'histogram',
            'name': energy_type
        }],
        'layout': {
            'title': f'{energy_type.capitalize()} Price Histogram',
            'xaxis': {
                'title': 'Price ($/bbl)'
            },
            'yaxis': {
                'title': 'Frequency'
            }
        }
    }

@app.callback(
    dash.dependencies.Output('price-boxplot', 'figure'),
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('energy-type-dropdown', 'value')]
)
def update_price_boxplot(n_clicks, energy_type):
    n_clicks = update_n_clicks(n_clicks)
    
    if energy_type == 'oil':
        data = oil_df
    else:
        data = gas_df

    return {
        'data': [{
            'y': data['Price'],
            'type': 'box',
            'name': energy_type
        }],
        'layout': {
            'title': f'{energy_type.capitalize()} Prices Distribution'
        }
    }


@app.callback(
    dash.dependencies.Output('price-scatterplot', 'figure'),
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('energy-type-dropdown', 'value')]
)
def update_price_scatterplot(n_clicks, energy_type):
    n_clicks = update_n_clicks(n_clicks)
    
    if energy_type == 'oil':
        data = oil_df
    else:
        data = gas_df

    return {
        'data': [{
            'x': data['Date'],
            'y': data['Price'],
            'mode': 'markers',
            'type': 'scatter',
            'name': energy_type
        }],
        'layout': {
            'title': f'{energy_type.capitalize()} Prices Over Time'
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
