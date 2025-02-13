import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Output, Input

from . import ids
from Data.loader import DataSchema


def render(app: Dash, df: pd.DataFrame) -> html.Div:
    try:
        # Extract unique years from the DataFrame
        Years = df[DataSchema.YEAR].drop_duplicates().tolist()
    except Exception as e:
        # Return an error message if data extraction fails
        return html.Div(f"Error loading data: {e}")

    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
    )
    def select_all_years(n_clicks) -> list[str]:
        print(f"Select All Years Button clicked {n_clicks} times")  # Debug statement
        if n_clicks:
            print(f"Returning Years: {Years}")  # Debug statement
            return Years
        return []

    # Return the layout for the year dropdown and select all button
    return html.Div(
        id=ids.YEAR_DROPDOWN_CONTAINER,
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in Years],
                value=[],
                multi=True,
            ),
            html.Button(
                id=ids.SELECT_ALL_YEARS_BUTTON,
                className="dropdown-button",
                children=["Select All"],
            ),
        ],
    )
