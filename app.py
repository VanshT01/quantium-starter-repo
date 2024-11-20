from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Load the processed sales data
df = pd.read_csv("formatted_sales_data.csv")

# Convert the 'date' column to datetime and sort the data
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Create the line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Sales Over Time by Region",
    labels={"date": "Date", "sales": "Sales ($)"}
)

# Add vertical line for price change using add_shape
fig.add_shape(
    type="line",
    x0=pd.Timestamp("2021-01-15"),
    x1=pd.Timestamp("2021-01-15"),
    y0=0,
    y1=df['sales'].max(),  # Extend the line to the max Y-axis value
    line=dict(
        color="red",
        dash="dash"
    ),
    xref="x",
    yref="y"
)

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(
        children="Soul Foods Pink Morsel Sales Visualizer",
        style={"textAlign": "center"}
    ),
    html.P(
        children="Visualizing Pink Morsel sales data to answer: Were sales higher before or after the price change?",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run the Dash app
if __name__ == "__main__":
    app.run(debug=True)
