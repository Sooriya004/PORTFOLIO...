from flask import Flask, render_template
import requests
import yfinance as yf

app = Flask(__name__)

def get_crypto_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return data["price"]

def get_index_price(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    return round(data["Close"].iloc[-1], 2)

@app.route("/")
def dashboard():
    prices = {
        "Bitcoin": get_crypto_price(),
        "Gold": get_index_price("GC=F"),
        "Silver": get_index_price("SI=F"),
        "Nifty 50": get_index_price("^NSEI"),
        "Sensex": get_index_price("^BSESN"),
        "Nasdaq": get_index_price("^IXIC"),
        "S&P 500": get_index_price("^GSPC"),
    }

    return render_template("dashboard.html", prices=prices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
