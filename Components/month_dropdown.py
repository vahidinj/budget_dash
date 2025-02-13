import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Output, Input

from . import ids
from Data.loader import DataSchema


def render(app: Dash, df: pd.DataFrame) -> html.Div:
    try:
        # Extract unique month names from the DataFrame
        Months = df[DataSchema.MONTH_NAME].drop_duplicates().tolist()
    except Exception as e:
        # Return an error message if data extraction fails
        return html.Div(f"Error loading data: {e}")

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks"),
    )
    def select_all_months(n_clicks) -> list[str]:
        print(f"Select All Months Button clicked {n_clicks} times")  # Debug statement
        if n_clicks:
            print(f"Returning Months: {Months}")  # Debug statement
            return Months
        return []

    # Return the layout for the month dropdown and select all button
    return html.Div(
        id=ids.MONTH_DROPDOWN_CONTAINER,
        children=[
            html.H6("Month"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=[{"label": month, "value": month} for month in Months],
                value=[],
                multi=True,
            ),
            html.Button(
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                className="dropdown-button",
                children=["Select All"],
            ),
        ],
    )
