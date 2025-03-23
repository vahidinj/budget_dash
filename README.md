# Budget Tracking Dashboard

This project is a budget tracking dashboard built using Plotly Dash. The dashboard provides an interactive way to monitor Income, Expense, and Savings over time through dynamic drop-downs, histograms, and line graphs.

## Features

- **Plotly Dash Integration**: Utilizes Plotly Dash to create an interactive web application.
- **Dynamic Drop-Downs**: Includes three dynamic drop-downs for selecting types, months, and years.
- **Data Visualization**: Generates histograms and line graphs to visualize Income, Expense, and Savings over time.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/vahidinj/budget_dash.git
    cd budget_dash
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Open the dashboard**:
    Open your web browser and go to `http://127.0.0.1:8050/`.

## Project Structure

- : Entry point for the application. Sets up and runs the Dash server.
- : Contains the layout and visualization components for the dashboard.
    - : Defines the layout of the dashboard.
    - `line_chart.py`: Generates the line chart for visualizing data.
    - `bar_chart.py`: Generates the bar chart for visualizing data.
    - `type_dropdown.py`: Creates the type selection drop-down.
    - `month_dropdown.py`: Creates the month selection drop-down.
    - `year_dropdown.py`: Creates the year selection drop-down.
- : Contains data loading and schema definitions.
    - : Loads the budget tracking data from an Excel file.
    - `DataSchema.py`: Defines the schema for the data.
- `assets/`: Contains any static assets (e.g., CSS files) used by the dashboard.

## Data

The data for the dashboard is loaded from an Excel file located at . The data includes columns for Date, Type, Category, Amount, and other relevant information.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Plotly Dash](https://plotly.com/dash/) for providing the framework for building interactive web applications.
- [Bootstrap](https://getbootstrap.com/) for styling the dashboard components.
