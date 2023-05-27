# Import necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

def create_lstm_model(input_shape, dropout=0.2, loss="mean_squared_error", optimizer="adam"):
    """
    Creates a Long Short-Term Memory (LSTM) model.
    
    :param input_shape: Tuple representing the shape of input data.
    :param dropout: Dropout rate for regularization. Default is 0.2.
    :param loss: Loss function for model training. Default is "mean_squared_error".
    :param optimizer: Optimizer for model training. Default is "adam".
    :return: A compiled LSTM model.
    """
    # Initialize the model
    model = Sequential()

    # Add LSTM layer with dropout for regularization
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(dropout))

    # Add another LSTM layer with dropout
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(dropout))

    # Add a Dense layer
    model.add(Dense(units=25))
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer=optimizer, loss=loss)

    return model

def train_lstm_model(model, x_train, y_train, epochs=20, batch_size=32):
    """
    Trains the LSTM model.
    
    :param model: The LSTM model.
    :param x_train: Training data.
    :param y_train: Training labels.
    :param epochs: Number of epochs for training. Default is 20.
    :param batch_size: Batch size for training. Default is 32.
    :return: The trained LSTM model.
    """
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

    return model

def predict_with_lstm(model, data):
    """
    Makes predictions using the LSTM model.
    
    :param model: The LSTM model.
    :param data: The data to make predictions on.
    :return: The model's predictions.
    """
    predictions = model.predict(data)

    return predictions
