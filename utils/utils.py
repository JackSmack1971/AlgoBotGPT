import pandas as pd
import robinstocks as r

def extract_list():
    # Extract the list of tickers from your holdings
    ticker_list = list(r.build_holdings().keys())
    return ticker_list

def visualize_price(ticker_list, span='year', bounds='regular'):
    # Visualize the price of the tickers over a given time period
    for t in range(len(ticker_list)):
        name = r.get_name_by_symbol(ticker_list[t])
        hist = r.stocks.get_historical(ticker_list[t], span=span, bounds=bounds)
        hist_df = pd.DataFrame()
        for i in range(len(hist)):
            df = pd.DataFrame(hist[i], index=[i])
            hist_df = pd.concat([hist_df, df])
        hist_df['begins_at'] = pd.to_datetime(hist_df['begins_at'], infer_datetime_format=True)
        hist_df['open_price'] = hist_df['open_price'].astype(float)
        hist_df['close_price'] = hist_df['close_price'].astype(float)
        hist_df['high_price'] = hist_df['high_price'].astype(float)
        hist_df['low_price'] = hist_df['low_price'].astype(float)
        ax = hist_df.plot(x='begins_at', y='open_price', figsize=(16, 8))
        ax.fill_between(hist_df['begins_at'], hist_df['low_price'], hist_df['high_price'], alpha=0.5)
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (USD)')
        ax.legend([ticker_list[t]])
        ax.set_title(name)
