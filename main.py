import pygal
import pandas as pd  # Standard alias for pandas
from datetime import datetime
from data_fetcher import fetch_stock_data  # Function to fetch stock data
from config import API_KEY  # API key for accessing the stock data API
from IPython.display import display, SVG
import os
import platform
   
# Get user input for stock symbol, chart type, and time series type
def get_user_input():
	
	graphNum = 0
	timeType = 0
	
    # Get stock symbol from user
	stockSymbol = input("Enter the stock symbol for the company you want data for: ")

    # Get chart type from user
	while True:
		try:
			print("Enter the chart type you would like (1, 2): ")
			graphNum = int(input("(1) Bar | (2) Line: "))
			
			if graphNum in [1, 2]:
				break
			else:
				print("Invalid choice. Please enter 1 or 2.")
				continue
		except ValueError:
			print("Invalid input. Please enter a number (1 or 2).")
			continue
		
	# Get time series from user
	while True:
		try:
			print("Select the Time Series of the chart you want to generate: ")
			print("(1) Intraday | (2) Daily | (3) Weekly | (4) Monthly")
			timeType = int(input("Enter time series option (1, 2, 3, 4): "))
			
			if timeType in [1, 2, 3, 4]:
				break
			else:
				print("Invalid choice, please enter 1, 2, 3, or 4.")
				continue
		except ValueError:
			print("Invalid input. Please enter a number (1, 2, 3, or 4).")
			continue
	
	return stockSymbol, graphNum, timeType

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
			return None, None
		else:
			return start_date, end_date
	except:
		print("Error: Please enter dates in the format YYYY-MM-DD")
		return None, None

# Get valid start and end dates from user
def get_validated_dates():
    while True:
        start_date_str = input("Enter the start Date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end Date (YYYY-MM-DD): ")
		
        start_date, end_date = validate_dates(start_date_str, end_date_str)
        if start_date and end_date:
            return start_date, end_date
		
        print("Please enter valid dates.")

# Main application logic
# Main application logic
def main():
    yesCheck = "y"
    while yesCheck.lower() == "y":
        # Get user input
        stockSymbol, graphNum, timeType = get_user_input()

        # Map user input to API function strings
        time_series_function_map = {
            1: "TIME_SERIES_INTRADAY",
            2: "TIME_SERIES_DAILY",
            3: "TIME_SERIES_WEEKLY",
            4: "TIME_SERIES_MONTHLY"
        }

        # Get the corresponding time series function from the map
        time_series_function = time_series_function_map.get(timeType)  # Convert to string
        interval = '5min' if time_series_function == "TIME_SERIES_INTRADAY" else None

        if not time_series_function:
            print("Invalid time series option selected.")
            continue  # Reprompt the user if the input is invalid

        # Ask the user for the beginning and end dates in YYYY-MM-DD
        start_date, end_date = get_validated_dates()

        # Fetch stock data
        stock_data = fetch_stock_data(stockSymbol, time_series_function, start_date, end_date, interval)

        # Check if stock data was retrieved successfully
        if stock_data is None:
            print("No stock data found. Please try again.")
            continue  # Reprompt the user if data is not found

        dates = stock_data.index.strftime('%b %d').tolist()
        opens = stock_data['1. open'].tolist()
        highs = stock_data['2. high'].tolist()
        lows = stock_data['3. low'].tolist()
        closes = stock_data['4. close'].tolist()
        volumes = stock_data['5. volume'].tolist()
		
		  # Reverse the stock data by sorting the index (dates)
        stock_data = stock_data.sort_index()  # Ensure data is sorted by date

        dates = stock_data.index.strftime('%b %d').tolist()
        opens = stock_data['1. open'].tolist()
        highs = stock_data['2. high'].tolist()
        lows = stock_data['3. low'].tolist()
        closes = stock_data['4. close'].tolist()
        volumes = stock_data['5. volume'].tolist()

        # Reverse the lists to display in ascending order
        dates.reverse()
        opens.reverse()
        highs.reverse()
        lows.reverse()
        closes.reverse()
        volumes.reverse()

        # Generate a graph and open in the user's default browser
        if(graphNum == 1):
            bar_chart = pygal.Bar(x_label_rotation=45, show_minor_x_labels=False)
            bar_chart.title = 'Stock Volume'
            bar_chart.x_labels = dates
            bar_chart.add('Volume', volumes)
            bar_chart_filename = "stock_prices_bar_chart.svg"
            bar_chart.render_to_file(bar_chart_filename)
            absolute_path = os.path.abspath(bar_chart_filename)
        elif(graphNum == 2):
            line_chart = pygal.Line(x_label_rotation=45, show_minor_x_labels=False)
            line_chart.title = 'Stock Prices (OHLC)'
            line_chart.x_labels = dates
            line_chart.add('Open', opens)
            line_chart.add('High', highs)
            line_chart.add('Low', lows)
            line_chart.add('Close', closes)
            line_chart_filename = "stock_prices_line_chart.svg"
            line_chart.render_to_file(line_chart_filename)
            absolute_path = os.path.abspath(line_chart_filename)

        system = platform.system()
		
        if(system == "Windows"):
            os.startfile(absolute_path)
        elif(system == "Darwin"):
            os.system(f'open "{absolute_path}"')
        elif(system == "Linux"):
            os.system(f'xdg-open "{absolute_path}"')

        # Ask user if they would like to view more data
        yesCheck = input("Would you like to view more stock data? Press 'y' to continue: ")


if __name__ == "__main__":
    main()
