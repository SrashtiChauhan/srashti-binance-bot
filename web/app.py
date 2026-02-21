from flask import Flask, render_template, request
import sys
import os

# Allow importing from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_order
from src.advanced.twap import place_twap_order

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

            elif order_type == "STOP_LIMIT":
                stop_price = float(request.form["stop_price"])
                limit_price = float(request.form["limit_price"])
                result = place_stop_limit_order(
                    symbol, side, quantity, stop_price, limit_price
                )

            elif order_type == "OCO":
                take_profit = float(request.form["take_profit"])
                stop_loss = float(request.form["stop_loss"])
                result = place_oco_order(
                    symbol, side, quantity, take_profit, stop_loss
                )

            elif order_type == "TWAP":
                duration = int(request.form["duration"])
                result = place_twap_order(
                    symbol, side, quantity, duration
                )

        except Exception as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)