from dash import Dash, html
import dash_bootstrap_components as dbc

from Components.create_layout import create_layout
from Data.loader import load_data
from Data.loader import Constants


def main() -> None:
    df = load_data(Constants.DATA_PATH)
    app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "Budget Tracking APP"
    app.layout = create_layout(app, df)
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
