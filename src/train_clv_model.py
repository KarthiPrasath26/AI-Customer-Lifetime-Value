import pandas as pd
import joblib
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Karthi_001@localhost:5432/online_retail')

df = pd.read_sql('SELECT * FROM customer_features', engine)

print(df.shape)

x = df[['recency', 'frequency', 'avg_order_value', 'lifetime_days', 't']]
y = df['monetary']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from xgboost import XGBRegressor
model = XGBRegressor(n_estimators=300, learning_rate=0.05, max_depth=5, random_state=42)

print(X_train.shape)
print(y_train.shape)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions[:10])

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
print("MSE:",mse)

import numpy as np
rmse = np.sqrt(mse)
print("RMSE:",rmse)

import matplotlib.pyplot as plt
from xgboost import plot_importance
plot_importance(model)
plt.show()

print(df.describe())

import joblib

joblib.dump(model, "models/clv_xgboost_model.pkl")

importance = model.feature_importances_

importance_df =pd.DataFrame({"feature": x.columns, "importance": importance})

importance_df = importance_df[importance_df["feature"] != "t"]

importance_df = importance_df.sort_values(by="importance", ascending=False)

print(importance_df)

importance_df.to_csv("D:/CLV suite/data/processed/feature_importance.csv", index=False)