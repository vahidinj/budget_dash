import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc
from dash.dependencies import Output, Input
from Data.loader import DataSchema
from . import ids


def render(app: Dash, df: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        Input(ids.TYPE_DROPDOWN, "value"),
        Input(ids.MONTH_DROPDOWN, "value"),
        Input(ids.YEAR_DROPDOWN, "value"),
    )
    def update_line_chart(
        selected_types: list[str], selected_months: list[str], selected_years: list[str]
    ) -> html.Div:
        # Filter the DataFrame based on the selected types, months, and years
        filtered_df = df[
            df[DataSchema.TYPE].isin(selected_types)
            & df[DataSchema.MONTH_NAME].isin(selected_months)
            & df[DataSchema.YEAR].isin(selected_years)
        ]

        # Group by Year, Month, and Type, and sum the Amount
        df_grouped = (
            filtered_df.groupby(
                [
                    DataSchema.YEAR,
                    DataSchema.MONTH,
                    DataSchema.MONTH_NAME,
                    DataSchema.TYPE,
                ]
            )[DataSchema.AMOUNT]
            .sum()
            .reset_index()
        )

        # Debug statement to check the grouped DataFrame
        print(f"Grouped DataFrame:\n{df_grouped}")

        # Create a line plot with spline interpolation
        fig = px.line(
            df_grouped,
            x=DataSchema.MONTH_NAME,  # Use month name for x-axis
            y=DataSchema.AMOUNT,
            color=DataSchema.TYPE,
            line_group=DataSchema.YEAR,
            markers=True,
            color_discrete_map={
                "Income": "#00FF9A",
                "Expense": "#B22DB2",
                "Savings": "#6E53FF",
            },
        )
        fig.update_traces(line_shape="spline", line=dict(width=3))

        # Update the layout of the figure
        fig.update_layout(
            title="Over Time",
            xaxis_title="Month",
            yaxis_title="Amount",
            legend_title="Type",
        )

        return html.Div(children=[dcc.Graph(figure=fig)])

    return html.Div(id=ids.LINE_CHART)
