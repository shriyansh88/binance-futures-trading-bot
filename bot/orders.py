from bot.client import get_client
from bot.logging_config import logger


client = get_client()


def place_market_order(symbol, side, quantity):
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )


        logger.info(f"Market Order Response: {response}")

        return response

    except Exception as e:

        logger.error(f"Market Order Error: {e}")
        raise

def place_limit_order(symbol, side, quantity, price):
    try:

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        print("DEBUG RESPONSE:", response)
        print("DEBUG TYPE:", type(response))

        logger.info(f"Limit Order Response: {response}")

        return response

    except Exception as e:
        print("DEBUG ERROR:", e)
        logger.error(f"Limit Order Error: {e}")
        raise