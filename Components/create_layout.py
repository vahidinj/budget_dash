import pandas as pd
from dash import Dash, html
from .type_dropdown import render as render_type_dropdown
from .month_dropdown import render as render_month_dropdown
from .year_dropdown import render as render_year_dropdown
from Components import bar_chart
from Components import line_chart


def create_layout(app: Dash, df: pd.DataFrame) -> html.Div:
    # Register callbacks within the layout function
    type_dropdown_component = render_type_dropdown(app, df)
    month_dropdown_component = render_month_dropdown(app, df)
    year_dropdown_component = render_year_dropdown(app, df)
    bar_chart_component = bar_chart.render(app, df)
    line_chart_component = line_chart.render(app, df)

    return html.Div(
        className="app-div",
        style={"display": "flex", "flexDirection": "column", "gap": "20px"},
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                style={"display": "flex", "flexDirection": "row", "gap": "10px"},
                children=[
                    type_dropdown_component,
                    month_dropdown_component,
                    year_dropdown_component,
                ],
            ),
            bar_chart_component,
            line_chart_component,
        ],
    )
