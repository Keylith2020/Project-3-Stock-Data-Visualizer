import requests
import lxml
import pygal
import pandas as pd  # Standard alias for pandas
from datetime import datetime
from data_fetcher import fetch_stock_data  # Function to fetch stock data
from config import API_KEY  # API key for accessing the stock data API
from IPython.display import display, SVG
import webbrowser
import os
import platform

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
