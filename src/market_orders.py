# # from utils.logger import logger

# # def test_logging():
# #     logger.info("Market order module initialized")
# #     logger.warning("This is a warning test")
# #     logger.error("This is an error test")

# # if __name__ == "__main__":
# #     test_logging()

# import sys
# from utils.logger import logger
# from utils.validator import (
#     validate_symbol,
#     validate_side,
#     validate_quantity,
# )
# def place_market_order(symbol, side, quantity):
#     try:
#         validate_symbol(symbol)
#         validate_side(side)
#         validate_quantity(quantity)
#         logger.info(f"Placing market order| Symbol:  {symbol}|Side: {side} | Qty: {quantity}")
#         print("Market order validated successfully")
#     except Exception as e:
#         logger.error(f"Market order failed: {str(e)}")
#         print(f"Error: {str(e)}")
    
# if __name__ == "__main__":
#     if len(sys.argv) !=4:
#         print("Usage python src/market_orders.py SYMBOL SIDE QUANTITY")
#         sys.exit(1)

#     symbol = sys.argv[1]
#     side = sys.argv[2]
#     quantity = float(sys.argv[3])

#     place_market_order(symbol, side, quantity)




# from utils.client import get_client
# from utils.logger import logger


# def test_connection():
#     try:
#         client = get_client()
#         balance = client.futures_account_balance()

#         logger.info("Fetched account balance successfully.")
#         print(" Connected successfully!")
#         print("Sample balance:", balance)


#     except Exception as e:
#         logger.error(f"Connection failed: {str(e)}")
#         print(" Connection failed:", str(e))


# if __name__ == "__main__":
#     test_connection()



# import sys
# from utils.logger import logger
# from utils.validator import (
#     validate_symbol,
#     validate_side,
#     validate_quantity,
# )
# from utils.client import get_client


# def place_market_order(symbol, side, quantity):
#     try:
#         # Validate input
#         validate_symbol(symbol)
#         validate_side(side)
#         validate_quantity(quantity)

#         # Get Binance client
#         client = get_client()

#         # Place order
#         order = client.futures_create_order(
#             symbol=symbol,
#             side=side,
#             type="MARKET",
#             quantity=quantity,
#         )

#         logger.info(f"Market order placed successfully: {order}")
#         print("Market order placed successfully!")
#         print(order)

#     except Exception as e:
#         logger.error(f"Market order failed: {str(e)}")
#         print(" Order failed:", str(e))


# if __name__ == "__main__":
#     if len(sys.argv) != 4:
#         print("Usage: python src/market_orders.py SYMBOL SIDE QUANTITY")
#         sys.exit(1)

#     symbol = sys.argv[1]
#     side = sys.argv[2]
#     quantity = float(sys.argv[3])

#     place_market_order(symbol, side, quantity)


import sys
import uuid
from datetime import datetime

from utils.logger import logger
from utils.validator import (
    validate_symbol,
    validate_side,
    validate_quantity,
)
from config import TEST_MODE


def simulate_market_order(symbol, side, quantity):
    """
    Simulates a Binance Futures MARKET order.
    """

    simulated_order = {
        "orderId": str(uuid.uuid4()),
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
        "status": "FILLED",
        "price": "SIMULATED_MARKET_PRICE",
        "timestamp": datetime.utcnow().isoformat(),
        "mode": "SIMULATION",
    }

    logger.info(f"[SIMULATION] Market order executed: {simulated_order}")
    return simulated_order


def place_market_order(symbol, side, quantity):
    try:
        # Validate inputs
        validate_symbol(symbol)
        validate_side(side)
        validate_quantity(quantity)

        logger.info(
            f"Placing MARKET order | Symbol: {symbol} | Side: {side} | Qty: {quantity}"
        )

        if TEST_MODE:
            order = simulate_market_order(symbol, side, quantity)
        else:
            raise NotImplementedError("Live API mode not enabled yet.")

        print("Market order executed successfully!")
        print(order)

    except Exception as e:
        logger.error(f"Market order failed: {str(e)}")
        print("Order failed:", str(e))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/market_orders.py SYMBOL SIDE QUANTITY")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])

    place_market_order(symbol, side, quantity)