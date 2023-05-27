# Import necessary libraries
import numpy as np
import pandas as pd
from indicators import calculate_bollinger_bands

def sideways_strategy(data, window=20):
    """
    Implements a trading strategy for sideways markets.
    
    :param data: Price data.
    :param window: Rolling window for Bollinger Bands calculation. Default is 20.
    :return: A pandas DataFrame with signals.
    """
    # Initialize the DataFrame with the signal column
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Calculate Bollinger Bands
    signals['upper_band'], signals['middle_band'], signals['lower_band'] = calculate_bollinger_bands(data, window)

    # Create signals
    signals['signal'] = np.where(data < signals['lower_band'], 1.0, 0.0)  # Buy signal
    signals['signal'] = np.where(data > signals['upper_band'], -1.0, signals['signal'])  # Sell signal

    # Generate trading orders
    signals['orders'] = signals['signal'].diff()

    return signals
