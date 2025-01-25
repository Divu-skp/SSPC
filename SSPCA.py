import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import yfinance as yf

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div(
    style={
        "backgroundColor": "#f7f9fc",
        "fontFamily": "Arial, sans-serif",
        "padding": "20px",
        "maxWidth": "800px",
        "margin": "auto",
        "borderRadius": "10px",
        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)"
    },
    children=[
        html.H1(
            "Stock Tracker",  # Title of the page
            style={
                "textAlign": "center",
                "color": "#007BFF",
                "marginBottom": "30px",
            },
        ),
        html.Div(
            [
                html.Label(
                    "Enter Stock Ticker:",  # Label for stock ticker input
                    style={
                        "fontSize": "16px",
                        "fontWeight": "bold",
                        "color": "#333",
                    },
                ),
                dcc.Input(
                    id="stock-ticker-input",  # Input field for stock ticker
                    type="text",
                    placeholder="e.g., AAPL, TSLA, MSFT",  # Example input
                    value="GOOGL",  # Default stock ticker
                    debounce=True,
                    style={
                        "width": "100%",
                        "padding": "10px",
                        "fontSize": "16px",
                        "marginTop": "10px",
                        "border": "1px solid #ccc",
                        "borderRadius": "5px",
                    },
                ),
            ],
            style={"marginBottom": "20px"},
        ),
        html.Div(
            [
                html.Label(
                    "Select Timeline:",  # Label for timeline selection
                    style={
                        "fontSize": "16px",
                        "fontWeight": "bold",
                        "color": "#333",
                    },
                ),
                dcc.Dropdown(
                    id="timeline-dropdown",  # Dropdown for selecting timeline
                    options=[
                        {"label": "Last 1 Month", "value": "1mo"},
                        {"label": "Last 3 Months", "value": "3mo"},
                        {"label": "Last 6 Months", "value": "6mo"},
                        {"label": "Last 1 Year", "value": "1y"},
                        {"label": "Last 5 Years", "value": "5y"},
                        {"label": "Max Available", "value": "max"},
                    ],
                    value="1y",  # Default timeline set to 1 year
                    clearable=False,
                    style={
                        "width": "100%",
                        "padding": "0px",
                        "fontSize": "16px",
                        "marginTop": "10px",
                        "borderRadius": "5px",
                    },
                ),
            ],
            style={"marginBottom": "10px"},
        ),
        html.Div(
            id="stock-graph-container",  # Div to hold the graph
            style={
                "backgroundColor": "#ffffff",
                "padding": "15px",
                "borderRadius": "10px",
                "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
            },
        ),
        # Footer section
        html.Div(
            "Created by Dwived Krishna P",  # Footer text
            style={
                "textAlign": "center",
                "fontSize": "14px",
                "color": "#888",
                "marginTop": "30px",
                "padding": "10px",
                "fontStyle": "italic",
            },
        ),
    ],
)

# Callback to update the graph based on stock ticker and timeline
@app.callback(
    Output("stock-graph-container", "children"),  # Output: Graph container
    [Input("stock-ticker-input", "value"), Input("timeline-dropdown", "value")],  # Inputs: Stock ticker and timeline
)
def update_stock_graph(stock_ticker, selected_timeline):
    if not stock_ticker:
        return html.Div(
            "Please enter a stock ticker to view data.",  # Error message if ticker is not provided
            style={"textAlign": "center", "color": "#888", "padding": "20px"},
        )

    try:
        # Fetch stock data from Yahoo Finance
        stock_data = yf.Ticker(stock_ticker)
        stock_df = stock_data.history(period=selected_timeline)  # Get data for selected timeline

        if stock_df.empty:
            return html.Div(
                f"No data found for stock ticker: {stock_ticker.upper()}",  # Error message if no data found
                style={"textAlign": "center", "color": "#888", "padding": "20px"},
            )

        # Create a Plotly figure for the stock price
        stock_price_graph = go.Figure(
            data=[
                go.Scatter(
                    x=stock_df.index,
                    y=stock_df["Close"],  # Plot the 'Close' price
                    mode="lines",  # Line plot for stock prices
                    name="Close Price",
                    line=dict(color="#007BFF"),
                )
            ],
            layout=go.Layout(
                title={
                    "text": f"Stock Data for {stock_ticker.upper()} ({selected_timeline})",  # Title showing ticker and timeline
                    "x": 0.5,
                    "xanchor": "center",
                    "font": {"size": 20, "color": "#333"},
                },
                xaxis=dict(title="Date", titlefont=dict(size=14), gridcolor="#f0f0f0"),
                yaxis=dict(title="Close Price (USD)", titlefont=dict(size=14), gridcolor="#f0f0f0"),
                paper_bgcolor="#ffffff",
                plot_bgcolor="#ffffff",
                margin=dict(l=40, r=40, t=60, b=40),
            ),
        )

        # Return the graph component to be displayed
        return dcc.Graph(id="stock-price-graph", figure=stock_price_graph)

    except Exception as error:
        # Display error message if an exception occurs
        return html.Div(
            f"An error occurred: {str(error)}",  # Display the error message
            style={"textAlign": "center", "color": "red", "padding": "20px"},
        )


# Run the app with debugging off
if __name__ == "__main__":
    app.run_server(debug=False)  # Debug mode disabled for production
