from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'B9JPJUGRL6GORK7M'
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    time_series = data.get('Time Series (5min)', {})
    if not time_series:
        raise ValueError(f"No se encontraron datos para el símbolo {symbol}")
    latest_time = sorted(time_series.keys())[0]
    latest_data = time_series[latest_time]
    if '1. open' not in latest_data:
        raise ValueError(f"No se encontraron datos de precio para el símbolo {symbol}")
    return latest_data['1. open']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', stock_data={})

    stock_data = {}
    symbols = request.form.get('symbols')
    symbols = [sym.strip() for sym in symbols.split(',')]
    for symbol in symbols:
        try:
            price = get_stock_price(symbol)
            stock_data[symbol] = price
        except Exception as e:
            stock_data[symbol] = str(e)
    return render_template('index.html', stock_data=stock_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
