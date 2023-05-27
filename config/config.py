# config.py

# Trading parameters
TRADE_PARAMETERS = {
    "EMA_SHORT_PERIOD": 12,  # Period for the short-term exponential moving average
    "EMA_LONG_PERIOD": 26,  # Period for the long-term exponential moving average
    "RSI_PERIOD": 14,  # Period for the Relative Strength Index
    "STOP_LOSS": 0.02,  # Stop loss percentage
    "TAKE_PROFIT": 0.06,  # Take profit percentage
}

# Binance API parameters
BINANCE_API_PARAMETERS = {
    "API_URL": "https://api.binance.com",  # Binance API URL
    "STREAM_URL": "wss://stream.binance.com:9443/ws",  # Binance Stream URL
    "SYMBOL": "BTCUSDT",  # Trading symbol
}
