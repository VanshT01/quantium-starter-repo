from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the formatted sales data
df = pd.read_csv("formatted_sales_data.csv")

# Create the Dash app
app = Dash(__name__, external_stylesheets=['style.css'])

# App Layout
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '20px'}, children=[
    html.H1('Pink Morsel Sales Visualizer', style={'textAlign': 'center', 'color': '#333'}),

    # Radio button for region filtering
    html.Div([
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '10px'}
        )
    ], style={'margin-bottom': '20px'}),

    # Sales graph
    dcc.Graph(id='sales-graph', style={'margin-top': '20px'}),
])

# Callback to update the graph based on the selected region
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter data based on selected region
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create the line chart
    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f"Sales Data for {selected_region.capitalize()} Region" if selected_region != 'all' else "Sales Data for All Regions",
        labels={'date': 'Date', 'sales': 'Total Sales'}
    )
    fig.update_layout(
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        font_color='#333',
        title_x=0.5
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
server = app.server