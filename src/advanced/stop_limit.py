import sys
import uuid
from datetime import datetime

from src.utils.logger import logger
from src.utils.validator import (
    validate_symbol,
    validate_side,
    validate_quantity,
    validate_price,
)
from src.config import TEST_MODE


def simulate_market_price():
    """
    Simulates current market price.
    In real mode, this would fetch from Binance API.
    """
    return 60000 


def simulate_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    current_price = simulate_market_price()

    logger.info(f"Current simulated market price: {current_price}")

    if current_price >= stop_price:
        logger.info("Stop price triggered. Placing limit order.")

        simulated_order = {
            "orderId": str(uuid.uuid4()),
            "symbol": symbol,
            "side": side,
            "type": "STOP_LIMIT",
            "quantity": quantity,
            "stop_price": stop_price,
            "limit_price": limit_price,
            "status": "TRIGGERED",
            "timestamp": datetime.utcnow().isoformat(),
            "mode": "SIMULATION",
        }

        logger.info(f"[SIMULATION] Stop-Limit executed: {simulated_order}")
        return simulated_order
    else:
        logger.info("Stop price not reached yet.")
        return {
            "status": "PENDING",
            "message": "Stop price not triggered.",
        }


def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_quantity(quantity)
        validate_price(stop_price)
        validate_price(limit_price)

        logger.info(
            f"Placing STOP-LIMIT order | Symbol: {symbol} | Side: {side} | Qty: {quantity} | Stop: {stop_price} | Limit: {limit_price}"
        )

        if TEST_MODE:
            order = simulate_stop_limit_order(
                symbol, side, quantity, stop_price, limit_price
            )
        else:
            raise NotImplementedError("Live API mode not enabled.")

        print(" Stop-Limit order processed!")
        return order

    except Exception as e:
        logger.error(f"Stop-Limit order failed: {str(e)}")
        # print(" Order failed:", str(e))
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python src/advanced/stop_limit.py SYMBOL SIDE QUANTITY STOP_PRICE LIMIT_PRICE")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    stop_price = float(sys.argv[4])
    limit_price = float(sys.argv[5])

    place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)