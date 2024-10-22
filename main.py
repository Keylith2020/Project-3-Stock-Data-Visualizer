import requests
import lxml
import pygal
import pandas as pd  # Standard alias for pandas
from datetime import datetime
from data_fetcher import fetch_stock_data  # Function to fetch stock data
from config import API_KEY  # API key for accessing the stock data API

def get_user_input():
    # Get user input for stock symbol, chart type, and time series type
    stockSymbol = input("Enter the stock symbol for the company you want data for: ")
    graphNum = input("Enter the chart type you would like (1: Bar | 2: Line): ")
    
    print("Select the Time Series of the chart you want to Generate: ")
    print("(1) Intraday | (2) Daily | (3) Weekly | (4) Monthly")
    timeType = input("Enter time series option (1, 2, 3, 4): ")
    
    return stockSymbol, graphNum, timeType

def validate_dates(start_date_str, end_date_str):
    # Create start datetime object
	start_date_array = start_date_str.split("-")
	start_date = datetime(int(start_date_array[0]), int(start_date_array[1]), int(start_date_array[2]))

	# Create end datetime object
	end_date_array = end_date_str.split("-")
	end_date = datetime(int(end_date_array[0]), int(end_date_array[1]), int(end_date_array[2]))

	# Check if end date is before start date
	if start_date > end_date:
		return False
	else:
		return True

def get_validated_dates():
    """Get and validate start and end dates from user input."""
    while True:
        start_date_str = input("Enter the start Date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end Date (YYYY-MM-DD): ")
        
        start_date, end_date = validate_dates(start_date_str, end_date_str)
        if start_date and end_date:
            return start_date, end_date
        print("Please enter valid dates.")

# Main application logic to fetch stock data and generate graphs.
def main():
    yesCheck = "y"
    while yesCheck.lower() == "y":  # Convert to lowercase for consistency
        # Get user input
        stockSymbol, graphNum, timeType = get_user_input()

        # Map user input to API function strings
        time_series_function_map = {
            "1": "TIME_SERIES_INTRADAY",
            "2": "TIME_SERIES_DAILY",
            "3": "TIME_SERIES_WEEKLY",
            "4": "TIME_SERIES_MONTHLY"
        }

        # Get the corresponding time series function from the map
        time_series_function = time_series_function_map.get(timeType)
        interval = '5min' if time_series_function == "TIME_SERIES_INTRADAY" else None

        if not time_series_function:
            print("Invalid time series option selected.")
            continue  # Reprompt the user if the input is invalid

        # Ask the user for the beginning and end dates in YYYY-MM-DD
        start_date_str = input("Enter the start Date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end Date (YYYY-MM-DD): ")

        # Validate dates
        date1, date2 = validate_dates(start_date_str, end_date_str)
        if date1 is None or date2 is None:
            continue  # Reprompt if dates are invalid

        # Fetch stock data
        stock_data = fetch_stock_data(stockSymbol, time_series_function, date1.date(), date2.date(), interval)

        # Check if stock data was retrieved successfully
        if stock_data is None:
            print("No stock data found. Please try again.")
            continue  # Reprompt the user if data is not found
        
	# Send api request and get json data returned
    url = f'https://alphavantageapi.co/timeseries/analytics?SYMBOLS={stockSymbol}&RANGE={date1}&RANGE={date2}&INTERVAL={timeSeries}&CALCULATIONS=MIN,MAX,MEAN,MEDIAN&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)

	# Generate a graph and open in the user's default browser

    # Ask user if they would like to view more data
    yesCheck = input("Would you like to view more stock data? Press 'y' to continue: ")

if __name__ == "__main__":
    main()
