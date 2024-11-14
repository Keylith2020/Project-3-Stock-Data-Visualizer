import data_fetcher
import pandas
from flask import Flask, render_template, request, flash

# make a flask app object
app = Flask(__name__)
app.config["DEBUG"] = True

# load the csv file at start
df = pandas.read_csv('stocks.csv')
symbols = df['Symbol'].tolist()

# use app.route() declaration to create flask view called index()
@app.route('/')
def index():
    return render_template('index.html', symbols=symbols)

@app.route('/submit', methods=['POST'])
def submit():
    # get user input from form
    symbol = request.form['symbol']
    chart = request.form['chart']
    time = request.form['time']
    start = request.form['start']
    end = request.form['end']

    valid = data_fetcher.validate_dates(start, end)

    # if not symbol, chart, time, start, end, or valid dates flash error
    if not symbol:
        flash("Symbol is required.")
    elif not chart:
        flash("Chart type is required.")
    elif not time:
        flash("Time series is required.")
    elif not start:
        flash("Start date is required.")
    elif not end:
        flash("End date is required.")
    elif not valid:
        flash("Start data must be before end date")
    else:
        # send input to data fetcher
        svg_data = data_fetcher.fetch_stock_data(symbol, time, start, end, chart)
        return render_template('index.html', symbols=symbols, svg_data=svg_data)

if __name__ == '__main__':
    app.run()
