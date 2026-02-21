from flask import Flask, render_template, request
import sys
import os

# Allow importing from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.market_orders import place_market_order
from src.limit_orders import place_limit_order

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        order_type = request.form["order_type"]
        symbol = request.form["symbol"]
        side = request.form["side"]
        quantity = float(request.form["quantity"])

        try:
            if order_type == "MARKET":
                result = place_market_order(symbol, side, quantity)
            elif order_type == "LIMIT":
                price = float(request.form["price"])
                result = place_limit_order(symbol, side, quantity, price)
        except Exception as e:
            result = str(e)

    # return render_template("index.html", result=result)
    return render_template("index.html", result=result if isinstance(result, dict) else None)


if __name__ == "__main__":
    app.run(debug=True)