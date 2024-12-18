import requests
import pandas as pd
import pygal
from config import API_KEY  # Import API_KEY from config.py
from datetime import datetime

# Validate the start and end dates provided by the user
def validate_dates(start_date_str, end_date_str):
	try:
		# Create start datetime object
		start_date_array = start_date_str.split("-")
		start_date = datetime(int(start_date_array[0]), int(start_date_array[1]), int(start_date_array[2]))

		# Create end datetime object
		end_date_array = end_date_str.split("-")
		end_date = datetime(int(end_date_array[0]), int(end_date_array[1]), int(end_date_array[2]))
          
		# Check if end date is before start date
		if start_date > end_date:
			print("Error: Start date must be before end date")
			return False
		else:
			return True
	except:
		print("Error: Please enter dates in the format YYYY-MM-DD")
		return False

# Query stock data api with selected filters
def fetch_stock_data(symbol, time_series_function, start_date, end_date, graphType, interval='5min'):
    # Construct the base URL
    base_url = "https://www.alphavantage.co/query"
    
    # Set parameters for the API call
    params = {
        "function": time_series_function,
        "symbol": symbol,
        "apikey": API_KEY,  # Use the imported API_KEY here
    }

    if time_series_function == "TIME_SERIES_INTRADAY":
        params["interval"] = interval

    # Make the API call
    print("Fetching data with the following parameters:", params)  # Debugging line
    response = requests.get(base_url, params=params)

    # Print the response status and content for debugging
    print("Response Status Code:", response.status_code)  # Debugging line
    print("Response Content:", response.text)  # Debugging line

    # Check if the request was successful
    if response.status_code != 200:
        print("Error: Unable to fetch data from API.")  # Debugging line
        return None

    # Parse the JSON response
    data = response.json()

    # Check for specific error messages in the API response
    if "Error Message" in data:
        print("Error from API:", data["Error Message"])  # Debugging line
        return None

    # Extract and process the time series data based on the function used
    time_series_key = None
    if time_series_function == "TIME_SERIES_INTRADAY":
        time_series_key = f"Time Series ({interval})"  # Adjust based on the interval
    elif time_series_function == "TIME_SERIES_DAILY":
        time_series_key = "Time Series (Daily)"
    elif time_series_function == "TIME_SERIES_WEEKLY":
        time_series_key = "Weekly Time Series"
    elif time_series_function == "TIME_SERIES_MONTHLY":
        time_series_key = "Monthly Time Series"

    if time_series_key not in data:
        print("Error: Expected time series data not found in response.")  # Debugging line
        return None

    # Convert to pandas DataFrame
    df = pd.DataFrame.from_dict(data[time_series_key], orient='index', columns=['1. open', '2. high', '3. low', '4. close', '5. volume'])
    df.index = pd.to_datetime(df.index)

    # Convert data types explicitly (ensure no strings are present)
    df['1. open'] = df['1. open'].astype(float)
    df['2. high'] = df['2. high'].astype(float)
    df['3. low'] = df['3. low'].astype(float)
    df['4. close'] = df['4. close'].astype(float)
    df['5. volume'] = df['5. volume'].astype(int)

    # Convert start_date and end_date to pandas Timestamps
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    # Filter the DataFrame based on the date range
    df = df[(df.index >= start_date) & (df.index <= end_date)]

    dates = df.index.strftime('%b %d').tolist()
    opens = df['1. open'].tolist()
    highs = df['2. high'].tolist()
    lows = df['3. low'].tolist()
    closes = df['4. close'].tolist()
    volumes = df['5. volume'].tolist()
    
    # Generate a graph and return chart as svg string
    if(graphType == "bar"):
        bar_chart = pygal.Bar(x_label_rotation=45, show_minor_x_labels=False)
        bar_chart.title = 'Stock Volume'
        bar_chart.x_labels = dates
        bar_chart.add('Volume', volumes)
        svg_data = bar_chart.render(is_unicode=True)
    elif(graphType == "line"):
        line_chart = pygal.Line(x_label_rotation=45, show_minor_x_labels=False)
        line_chart.title = 'Stock Prices (OHLC)'
        line_chart.x_labels = dates
        line_chart.add('Open', opens)
        line_chart.add('High', highs)
        line_chart.add('Low', lows)
        line_chart.add('Close', closes)
        svg_data = line_chart.render(is_unicode=True)
    
    return svg_data
