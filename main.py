import requests
import lxml
import pygal
import pandas
from datetime import datetime

def user_input(): 

    return

def call_api():

    return

yesCheck = "y"
while yesCheck == "y":
	stockSymbol = input("Enter the stock symbol for the company you want data for: ")

	print("Enter the chart type you would like (1, 2): ")
	graphNum = input("(1)Bar | (2) Line: ")

	print("Select the Time Series of the chart you want to Generate: ")
	print("(1)Intraday | (2)Daily | (3)Weekly | (4)Monthly")
	timeType = input("Enter time series option (1, 2, 3, 4): ")

	date1 = input("Enter the start Date (YYYY-MM-DD): ")

	date2 = input("Enter the end Date (YYYY-MM-DD): ")

	yesCheck = input("Would you like to view more stock data? Press 'y' to countinue: ")

