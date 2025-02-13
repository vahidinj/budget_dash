import pandas as pd


class Constants:
    DATA_PATH = "/Budget_Tracker.xlsm"


class DataSchema:
    DATE = "Date"
    YEAR = "Year"
    MONTH = "Month"
    MONTH_NAME = "Month Name"
    TYPE = "Type"
    CATEGORY = "Category"
    AMOUNT = "Amount"
    EFFECTIVE_DATE = "Effective Date"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(
        Constants.DATA_PATH,
        sheet_name="Budget Tracking",
        skiprows=8,
        dtype={
            DataSchema.TYPE: str,
            DataSchema.CATEGORY: str,
            DataSchema.AMOUNT: float,
        },
        parse_dates=[DataSchema.DATE],
    ).dropna(axis=1, how="all")
    df[DataSchema.YEAR] = df[DataSchema.DATE].dt.year
    df[DataSchema.MONTH] = df[DataSchema.DATE].dt.month
    df[DataSchema.MONTH_NAME] = df[DataSchema.DATE].dt.strftime("%b")  # Add month name
    return df
