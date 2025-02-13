import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Output, Input

from . import ids
from Data.loader import DataSchema


def render(app: Dash, df: pd.DataFrame) -> html.Div:
    try:
        # Extract unique types from the DataFrame
        Types = df[DataSchema.TYPE].drop_duplicates().tolist()
    except Exception as e:
        # Return an error message if data extraction fails
        return html.Div(f"Error loading data: {e}")

    @app.callback(
        Output(ids.TYPE_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_TYPES_BUTTON, "n_clicks"),
    )
    def select_all_types(n_clicks) -> list[str]:
        print(f"Select All Types Button clicked {n_clicks} times")  # Debug statement
        if n_clicks:
            print(f"Returning Types: {Types}")  # Debug statement
            return Types
        return []

    # Return the layout for the type dropdown and select all button
    return html.Div(
        id=ids.TYPE_DROPDOWN_CONTAINER,
        children=[
            html.H6("Type"),
            dcc.Dropdown(
                id=ids.TYPE_DROPDOWN,
                options=[{"label": type, "value": type} for type in Types],
                value=[],
                multi=True,
            ),
            html.Button(
                id=ids.SELECT_ALL_TYPES_BUTTON,
                className="dropdown-button",
                children=["Select All"],
            ),
        ],
    )
