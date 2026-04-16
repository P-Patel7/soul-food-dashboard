import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

DATA_PATH = "./formatted_data.csv"

app = Dash()

df = pd.read_csv(DATA_PATH)

df = df.sort_values(by="date", ascending=True)

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

app.layout = html.Div(children=[
    html.Div([
        html.H1("Pink Morsel Visualiser")
    ]),

    html.Div([
        dcc.Graph(id="sales-line-chart", figure=fig)
    ])
])

if __name__ == "__main__":
    app.run(debug=True)