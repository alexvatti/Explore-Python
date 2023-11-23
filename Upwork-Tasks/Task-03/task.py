#pip install robin_stocks
#pip install json

import json
from datetime import datetime
from robin_stocks import robinhood

# Initialize your Robinhood session
# Make sure to set up your Robinhood account and provide your login credentials
robinhood.login(username="your_username", password="your_password")

def get_options_prices(stock_symbols):
    option_data = []

    for symbol in stock_symbols:
        options = robinhood.options.find_options_by_symbol(symbol)

        for option in options:
            # Extract relevant information
            timestamp = int(datetime.utcnow().timestamp())
            expiration_date = option['expiration_date']
            bid_price = option['bid_price']
            ask_price = option['ask_price']
            day_high = option['high_price']
            day_low = option['low_price']
            option_type = option['type']
            strike_price = option['strike_price']

            # Determine if the option is a call or put
            option_label = 'Call' if option_type == 'call' else 'Put'

            # Save data to the list
            option_data.append({
                'timestamp': timestamp,
                'stock': symbol,
                'expiration_date': expiration_date,
                'bid_price': bid_price,
                'ask_price': ask_price,
                'day_high': day_high,
                'day_low': day_low,
                'option_type': option_label,
                'strike_price': strike_price
            })

    return option_data

def save_to_json(data, filename='options_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    # List of stock symbols
    stock_symbols = ['AAPL', 'GOOGL', 'MSFT']  # Add your desired stock symbols

    # Get options prices
    options_data = get_options_prices(stock_symbols)

    # Save data to JSON file
    save_to_json(options_data)
