#Working Date Range, Symbol, and Graphs
import requests
import pygal
import webbrowser

# Define your API key
apikey = 'GC43PO0IB14QIJ4E'

# Prompt user for input
symbol = input("Choose a symbol (e.g., IBM, AAPL, TSLA): ")
start_date = input("Choose a start date (YYYY-MM-DD): ")
end_date = input("Choose an end date (YYYY-MM-DD): ")

# Prompt user for the type of graph
while True:
    graph_type = input("Choose a graph type: (1) Bar chart or (2) Line chart: ")
    if graph_type in ['1', '2']:
        break
    else:
        print("Invalid choice. Please enter 1 for Bar chart or 2 for Line chart.")

# Fetch daily stock data
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}&outputsize=full'
response = requests.get(url)
data = response.json()

# Check if the data has been fetched correctly
if "Time Series (Daily)" in data:
    time_series = data["Time Series (Daily)"]
else:
    print("Error fetching data:", data)
    exit()

# Filter the data based on date range
filtered_data = {}
for date, metrics in time_series.items():
    if start_date <= date <= end_date:
        filtered_data[date] = metrics

# Prepare data for graph
dates = list(filtered_data.keys())
open_prices = [float(filtered_data[date]["1. open"]) for date in dates]
close_prices = [float(filtered_data[date]["4. close"]) for date in dates]
high_prices = [float(filtered_data[date]["2. high"]) for date in dates]
low_prices = [float(filtered_data[date]["3. low"]) for date in dates]

# Reverse the data to display in ascending order
dates.reverse()
open_prices.reverse()
close_prices.reverse()
high_prices.reverse()
low_prices.reverse()

# Create the chart based on user's choice
if graph_type == '1':
    # Create a bar chart
    chart = pygal.Bar()
    chart.title = f'Stock Prices for {symbol} ({start_date} to {end_date})'
    chart.x_labels = dates  # Use dates as labels
    chart.add('Open Price', open_prices)
    chart.add('Close Price', close_prices)
    chart.add('High Price', high_prices)
    chart.add('Low Price', low_prices)
    output_file = 'stock_prices_bar_chart.svg'
else:
    # Create a line chart
    chart = pygal.Line()
    chart.title = f'Stock Prices for {symbol} ({start_date} to {end_date})'
    chart.x_labels = dates  # Use dates as labels
    chart.add('Open Price', open_prices)
    chart.add('Close Price', close_prices)
    chart.add('High Price', high_prices)
    chart.add('Low Price', low_prices)
    output_file = 'stock_prices_line_chart.svg'

# Render the chart to a file
chart.render_to_file(output_file)

# Open the generated graph in a default web browser
webbrowser.open(output_file)
