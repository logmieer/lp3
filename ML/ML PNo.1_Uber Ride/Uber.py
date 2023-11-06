#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
# We don't want to see warnings
warnings.filterwarnings("ignore")

# Import data from "uber.csv"
data = pd.read_csv("uber.csv")

# Create a copy of the data
df = data.copy()

# Print the first few rows of the data
df.head()

# Get information about the data
df.info()

# Convert "pickup_datetime" to the required datetime format
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

# Check data information after conversion
df.info()

# View statistics of the data
df.describe()

# Count the number of missing values
df.isnull().sum()

# Calculate the correlation between columns
df.corr()

# Drop rows with missing values
df.dropna(inplace=True)

# Visualize a boxplot to identify outliers
plt.boxplot(df['fare_amount'])

# Remove outliers
q_low = df["fare_amount"].quantile(0.01)
q_hi = df["fare_amount"].quantile(0.99)
df = df[(df["fare_amount"] < q_hi) & (df["fare_amount"] > q_low)]

# Check for missing values again
df.isnull().sum()

# Prepare data for learning models
from sklearn.model_selection import train_test_split

# Select predictors (x) and the target variable (y)
x = df.drop("fare_amount", axis=1)
y = df['fare_amount']

# Convert "pickup_datetime" to a numeric format and keep only necessary columns
x['pickup_datetime'] = pd.to_numeric(pd.to_datetime(x['pickup_datetime']))
x = x.loc[:, x.columns.str.contains('^Unnamed')]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Import the Linear Regression model
from sklearn.linear_model import LinearRegression

# Create and train the Linear Regression model
lrmodel = LinearRegression()
lrmodel.fit(x_train, y_train)

# Make predictions
predict = lrmodel.predict(x_test)

# Check the root mean squared error (RMSE)
from sklearn.metrics import mean_squared_error
lrmodelrmse = np.sqrt(mean_squared_error(predict, y_test))
print("RMSE error for the Linear Regression model is", lrmodelrmse)

# Import the Random Forest Regressor model
from sklearn.ensemble import RandomForestRegressor

# Create and train the Random Forest Regressor model
rfrmodel = RandomForestRegressor(n_estimators=100, random_state=101)

# Fit the Random Forest model
rfrmodel.fit(x_train, y_train)
rfrmodel_pred = rfrmodel.predict(x_test)

# Calculate the RMSE for the Random Forest model
rfrmodel_rmse = np.sqrt(mean_squared_error(rfrmodel_pred, y_test))
print("RMSE value for Random Forest is:", rfrmodel_rmse)
