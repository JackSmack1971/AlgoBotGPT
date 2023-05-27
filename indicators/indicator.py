# Import necessary libraries
import talib
import numpy as np

def calculate_sma(data, window):
    """
    Calculate Simple Moving Average (SMA)
    :param data: Price data.
    :param window: Rolling window for SMA calculation.
    :return: A numpy array of SMA values.
    """
    sma = talib.SMA(data, timeperiod=window)
    return sma

def calculate_ema(data, window):
    """
    Calculate Exponential Moving Average (EMA)
    :param data: Price data.
    :param window: Rolling window for EMA calculation.
    :return: A numpy array of EMA values.
    """
    ema = talib.EMA(data, timeperiod=window)
    return ema

def calculate_macd(data, short_window, long_window):
    """
    Calculate Moving Average Convergence Divergence (MACD)
    :param data: Price data.
    :param short_window: Shorter window for MACD calculation.
    :param long_window: Longer window for MACD calculation.
    :return: A tuple of numpy arrays representing MACD line and signal line.
    """
    macd_line, signal_line, _ = talib.MACD(data, fastperiod=short_window, slowperiod=long_window, signalperiod=9)
    return macd_line, signal_line

def calculate_rsi(data, window):
    """
    Calculate Relative Strength Index (RSI)
    :param data: Price data.
    :param window: Rolling window for RSI calculation.
    :return: A numpy array of RSI values.
    """
    rsi = talib.RSI(data, timeperiod=window)
    return rsi

def calculate_bollinger_bands(data, window):
    """
    Calculate Bollinger Bands
    :param data: Price data.
    :param window: Rolling window for Bollinger Bands calculation.
    :return: A tuple of numpy arrays representing upper band, middle band and lower band.
    """
    upper_band, middle_band, lower_band = talib.BBANDS(data, timeperiod=window)
    return upper_band, middle_band, lower_band
