from config import config, secrets
from strategies import sideways, trending_up, trending_down
from indicators import indicator
from models import lstm
from utils import utils
import time
import pandas as pd
import robinstocks as r

class TradingBot:
    def __init__(self):
        self.api_key = secrets.API_KEY
        self.api_secret = secrets.API_SECRET
        self.api_url = config.API_URL
        self.trading_parameters = config.TRADING_PARAMETERS

    def connect_to_api(self):
        # Connect to the API
        r.login(self.api_key, self.api_secret)

    def get_market_data(self):
        # Get the current market data
        return r.build_holdings()

    def determine_market_trend(self, market_data):
        # Determine the market trend
        # This is a placeholder. You should replace this with your own logic.
        return 'sideways'

    def execute_sideways_strategy(self, market_data, trading_params):
        # Execute the sideways market strategy
        # This is a placeholder. You should replace this with your own logic.
        pass

    def execute_trending_up_strategy(self, market_data, trading_params):
        # Execute the trending up market strategy
        # This is a placeholder. You should replace this with your own logic.
        pass

    def execute_trending_down_strategy(self, market_data, trading_params):
        # Execute the trending down market strategy
        # This is a placeholder. You should replace this with your own logic.
        pass

    def manage_trades(self, trading_dict):
        # Manage trades
        holdings = r.build_holdings()
        holdings_df = pd.DataFrame()
        for i in range(len(holdings)):
            ticker = list(holdings.items())[i][0]
            holding_df = pd.DataFrame(list(holdings.items())[i][1], index=[i])
            holding_df['ticker'] = ticker
            holdings_df = pd.concat([holdings_df, holding_df])
        for j in range(len(trading_dict)):
            holding_df = holdings_df[holdings_df['ticker'] == list(trading_dict.keys())[j]]
            if holding_df['percent_change'].astype(float) <= list(trading_dict.values())[j][0]:
                print(f"Buying {holding_df['ticker'][0]} at {time.ctime()}")
                r.orders.order_buy_market(holding_df['ticker'][0], 1, time_in_force='gfd')
            if holding_df['percent_change'].astype(float) >= list(trading_dict.values())[j][1]:
                print(f"Selling {holding_df['ticker'][0]} at {time.ctime()}")
                r.orders.order_sell_market(holding_df['ticker'][0], 1, time_in_force='gfd')
