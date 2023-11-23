
Very basic python script that I will run throughout the day to get options prices using this library:
https://www.robin-stocks.com/en/latest/robinhood.html#getting-option-information

I will have a small list of stocks, the script needs to go to the api, find current option price for all calls and
puts expiring this week (the stock symbols may have multiple expirations throughout the week). save it to structured json file: 
timestamp (unix utc), stock, expiration date, bid, ask, day high, day low, call or put, strike price
