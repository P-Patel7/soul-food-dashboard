import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

DATA_PATH = "./formatted_data.csv"

app = Dash(__name__)

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

app.layout = html.Div([

    html.H1(
        "Pink Morsel Visualiser",
        style={
            "textAlign": "center",
            "color": "#1e1b4b"
        }
    ),

    # SINGLE MAIN BOX
    html.Div([

        # radio buttons (inside box)
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            style={
                "display": "flex",
                "justifyContent": "space-around",
                "marginBottom": "15px"
            }
        ),

        # graph (inside same box)
        dcc.Graph(id="sales-chart")

    ], style={
        "backgroundColor": "#c7d2fe",  # soft blue/purple box
        "padding": "20px",
        "borderRadius": "15px",
        "maxWidth": "900px",
        "margin": "20px auto",
        "boxShadow": "0 4px 10px rgba(0,0,0,0.15)"
    })

])


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):

    if region == "all":
        dff = df
    else:
        dff = df[df["region"] == region]

    dff = dff.sort_values("date")

    fig = px.line(
        dff,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        title_font=dict(color="#1e1b4b")
    )

    fig.update_traces(line=dict(color="#6366f1"))

    return fig


if __name__ == "__main__":
    app.run(debug=True)