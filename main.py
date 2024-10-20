import requests
import lxml
import pygal
import pandas
from datetime import datetime

def user_input(): 

    return

def call_api():

    return

# Application logic
yesCheck = "y"
while yesCheck == "y":
	# Ask the user to enter the stock symbol for the company they want data for
	stockSymbol = input("Enter the stock symbol for the company you want data for: ")

	# Ask the user for the chart type they would like
	print("Enter the chart type you would like (1, 2): ")
	graphNum = input("(1)Bar | (2) Line: ")

	# Ask the user for the time series function they want the api to use
	print("Select the Time Series of the chart you want to Generate: ")
	print("(1)Intraday | (2)Daily | (3)Weekly | (4)Monthly")
	timeType = input("Enter time series option (1, 2, 3, 4): ")

	# Ask the user for the beginning date in YYYY-MM-DD
	date1 = input("Enter the start Date (YYYY-MM-DD): ")

	# Ask the user for the end date in YYY-MM-DD format
	date2 = input("Enter the end Date (YYYY-MM-DD): ")

	# Check to make sure end date is not before if begin date
	# If it is, reprompt the user for the end date

	# Generate a graph and open in the user's default browser

	# Ask user if they would like to view more data
	yesCheck = input("Would you like to view more stock data? Press 'y' to continue: ")

