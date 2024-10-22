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
	graphNum = 0
	timeType = 0
	# Ask the user to enter the stock symbol for the company they want data for
	stockSymbol = input("Enter the stock symbol for the company you want data for: ")

	# Ask the user for the chart type they would like
	while graphNum==0:
		print("Enter the chart type you would like (1, 2): ")
		graphNum = int(input("(1)Bar | (2) Line: "))
		if graphNum == 1:
			print("You chose 1!")
		elif graphNum == 2:
			print("You chose 2!")

	# Ask the user for the time series function they want the api to use
	print("Select the Time Series of the chart you want to Generate: ")
	print("(1)Intraday | (2)Daily | (3)Weekly | (4)Monthly")
	while timeType==0:
		timeType = int(input("Enter time series option (1, 2, 3, 4): "))
		if timeType == 1:
			print("You chose 1!")
		if timeType == 2:
			print("You chose 2!")
		if timeType == 3:
			print("You chose 3!")
		if timeType == 4:
			print("You chose 4!")

	# Ask the user for the beginning date in YYYY-MM-DD
	date1array = input("Enter the start Date (YYYY-MM-DD): ").split("-")
	date1 = datetime(int(date1array[0]), int(date1array[1]), int(date1array[2]))

	# Ask the user for the end date in YYY-MM-DD format
	date2array = input("Enter the end Date (YYYY-MM-DD): ").split("-")
	date2 = datetime(int(date2array[0]), int(date2array[1]), int(date2array[2]))

	# Check to make sure end date is not before if begin date
	# If it is, reprompt the user for the end date
	if date1 > date2:
		print("Please enter an end date that is after the start date.")
		continue

	# Generate a graph and open in the user's default browser

	# Ask user if they would like to view more data
	yesCheck = input("Would you like to view more stock data? Press 'y' to continue: ")
