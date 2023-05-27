# Import necessary libraries
import numpy as np
import pandas as pd
from indicators import calculate_sma, calculate_ema

def trending_up_strategy(data, short_window=12, long_window=26):
    """
    Implements a trading strategy for trending up markets.
    
    :param data: Price data.
    :param short_window: Shorter window for EMA calculation. Default is 12.
    :param long_window: Longer window for EMA calculation. Default is 26.
    :return: A pandas DataFrame with signals.
    """
    # Initialize the DataFrame with the signal column
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Calculate short and long EMAs
    signals['short_ema'] = calculate_ema(data, short_window)
    signals['long_ema'] = calculate_ema(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_ema'][short_window:] > signals['long_ema'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['orders'] = signals['signal'].diff()

    return signals
