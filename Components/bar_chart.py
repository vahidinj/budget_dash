import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc
from dash.dependencies import Output, Input
from Data.loader import DataSchema
from . import ids


def render(app: Dash, df: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.TYPE_DROPDOWN, "value"),
        Input(ids.MONTH_DROPDOWN, "value"),
        Input(ids.YEAR_DROPDOWN, "value"),
    )
    def update_bar_chart(
        selected_types: list[str], selected_months: list[str], selected_years: list[str]
    ) -> html.Div:
        # Filter the DataFrame based on the selected types, months, and years
        filtered_df = df[
            df[DataSchema.TYPE].isin(selected_types)
            & df[DataSchema.MONTH_NAME].isin(selected_months)
            & df[DataSchema.YEAR].isin(selected_years)
        ]

        # Group by Type and sum the Amount
        df_grouped = (
            filtered_df.groupby([DataSchema.TYPE])[DataSchema.AMOUNT]
            .sum()
            .reset_index()
        )

        # Create a bar chart
        fig = px.bar(
            df_grouped,
            x=DataSchema.TYPE,
            y=DataSchema.AMOUNT,
            color=DataSchema.TYPE,
            color_discrete_map={
                "Income": "#00FF9A",
                "Expense": "#B22DB2",
                "Savings": "#6E53FF",
            },
        )
        fig.update_layout(
            title="Totals",
            yaxis_title="Amount",
            xaxis_title="Type",
            legend_title="Type",
        )

        return html.Div(children=[dcc.Graph(figure=fig)])

    return html.Div(id=ids.BAR_CHART)
