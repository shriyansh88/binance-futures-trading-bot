import argparse
from urllib import response

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def print_order_response(response):
    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Symbol       : {response.get('symbol')}")
    print(f"Side         : {response.get('side')}")
    print(f"Type         : {response.get('type')}")
    print(f"Executed Qty : {response.get('executedQty')}")

    if response.get("avgPrice"):
        print(f"Average Price: {response.get('avgPrice')}")

    print("====================================\n")


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders.")

            print(f"Price    : {price}")

        print("===================================\n")

        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print_order_response(response)

        print("✅ Order placed successfully.")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()