# -*- coding: utf-8 -*-
"""Tech-A-Intern:Level_2-Task2:-Stock price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S3SjqXxXLXCrQ9PmkEzoR1Huuk0xvoCa

# **Stock price prediction Project**
  
  Building a stock price prediction model involves several steps, from data collection and preprocessing to model training and evaluation. Let's go through the process using the example of using LSTM (Long Short-Term Memory) neural networks for time series forecasting.

# Step 1: Data Collection
Collect historical stock price data, volume, and any other relevant features from reliable sources like Yahoo Finance, Alpha Vantage, or a financial data provider. For this example, we'll use the Python libraries 'pandas', 'numpy', and 'yfinance' to fetch and process the data.
"""

import pandas as pd
import numpy as np
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

# Define the stock symbol and time range
stock_symbol = 'AAPL'
start_date = '2010-01-01'
end_date = '2022-12-31'

# Fetch stock data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Save the data to a CSV file for future use
stock_data.to_csv('/content/TCS1.csv')

"""# Step 2: Data Preprocessing and Feature Engineering
Preprocess the data by handling missing values, scaling the features, and engineering additional relevant features such as moving averages, price changes, etc
"""

# Load the saved data
stock_data = pd.read_csv('/content/TCS1.csv', index_col='Date', parse_dates=True)

stock_data

# Handle missing values
stock_data.fillna(method='ffill', inplace=True)

# Normalize the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(stock_data[['Open', 'High', 'Low', 'Close', 'Volume']])

# Create sequences for LSTM input
sequence_length = 30
X = []
y = []
for i in range(sequence_length, len(scaled_data)):
    X.append(scaled_data[i-sequence_length:i])
    y.append(scaled_data[i, 3])  # Predicting the 'Close' price

X = np.array(X)
y = np.array(y)

"""# Step 3: Train-Test Split
Split the data into training and testing sets. Since this is a time series dataset, ensure that the splitting is done chronologically
"""

split_ratio = 0.8
split_index = int(split_ratio * len(X))

X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

"""# Step 4: Build and Train LSTM Model
Build an LSTM model using a deep learning framework like TensorFlow or PyTorch. Here, we'll use TensorFlow and Keras to create the model.
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=10, batch_size=32)

"""# Step 5: Evaluate the Model
Evaluate the model's performance using metrics like Mean Squared Error (MSE) or Mean Absolute Error (MAE).
"""

y_pred = model.predict(X_test)
y_pred = scaler.inverse_transform(np.concatenate((X_test[:, -1, :-1], y_pred), axis=1))[:, -1]

from sklearn.metrics import mean_squared_error, mean_absolute_error
mse = mean_squared_error(stock_data['Close'][split_index+sequence_length:], y_pred)
mae = mean_absolute_error(stock_data['Close'][split_index+sequence_length:], y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")