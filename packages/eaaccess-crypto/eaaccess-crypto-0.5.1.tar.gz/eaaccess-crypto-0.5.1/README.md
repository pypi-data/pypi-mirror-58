# EAAccess-Crypto Beta

This is a platform package for cryptocurrency trading. 

EAAccess-crypto provide a programming platform to do the Live trading, Paper trading and Backtesting
based on CCXT libraries. CCXT is A JavaScript / Python / PHP cryptocurrency trading API with support 
for more than 120 bitcoin/altcoin exchanges (https://github.com/ccxt/ccxt), CCXT is a perferct unified
API for hundred of exchanges, but not support WebSockect yet until 2019/12/31. EAAccess-crypto use
binance's raw websocket API to support Ticker and Candlesticks real-time data refresh. So, EAAccess-cyrpto
version 0.5.x beta only support binance. When CCXT support unified websocket API, EAAccess-crypto 
will support the same exchanges with CCXT.