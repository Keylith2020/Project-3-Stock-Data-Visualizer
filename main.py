# main.py

import requests
import lxml
import pygal
import pandas as pd  # Standard alias for pandas
from datetime import datetime
from data_fetcher import fetch_stock_data  # Function to fetch stock data
from config import API_KEY  # API key for accessing the stock data API

def get_user_input():
    """Get user input for stock symbol, chart type, and time series type."""
    stock_symbol = input("Enter the stock symbol for the company you want data for: ")
    graph_num = input("Enter the chart type you would like (1: Bar | 2: Line): ")
    
    print("Select the Time Series of the chart you want to Generate: ")
    print("(1) Intraday | (2) Daily | (3) Weekly | (4) Monthly")
    time_type = input("Enter time series option (1, 2, 3, 4): ")
    
    return stock_symbol, graph_num, time_type

def validate_dates(start_date_str, end_date_str):
    """Validate the start and end dates."""
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None, None

    if start_date > end_date:
        print("End date must be after the start date.")
        return None, None

    return start_date, end_date

def get_validated_dates():
    """Get and validate start and end dates from user input."""
    while True:
        start_date_str = input("Enter the start Date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end Date (YYYY-MM-DD): ")
        
        start_date, end_date = validate_dates(start_date_str, end_date_str)
        if start_date and end_date:
            return start_date, end_date
        print("Please enter valid dates.")

def main():
    """Main application logic to fetch stock data and generate graphs."""
    yes_check = "y"
    while yes_check.lower() == "y":  # Convert to lowercase for consistency
        # Get user input
        stock_symbol, graph_num, time_type = get_user_input()

        # Map user input to API function strings
        time_series_function_map = {
            "1": "TIME_SERIES_INTRADAY",
            "2": "TIME_SERIES_DAILY",
            "3": "TIME_SERIES_WEEKLY",
            "4": "TIME_SERIES_MONTHLY"
        }

        # Get the corresponding time series function from the map
        time_series_function = time_series_function_map.get(time_type)

        if not time_series_function:
            print("Invalid time series option selected.")
            continue  # Reprompt the user if the input is invalid

        # Get validated start and end dates
        start_date, end_date = get_validated_dates()

        # Fetch stock data
        stock_data = fetch_stock_data(stock_symbol, time_series_function, start_date.date(), end_date.date())

        # Check if stock data was retrieved successfully
        if stock_data is None:
            print("No stock data found. Please try again.")
            continue  # Reprompt the user if data is not found

        # Generate a graph and open in the user's default browser
        # (Graph generation code would go here)

        # Ask user if they would like to view more data
        yes_check = input("Would you like to view more stock data? Press 'y' to continue: ")

if __name__ == "__main__":
    main()
