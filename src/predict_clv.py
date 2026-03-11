import pandas as pd
import joblib
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Karthi_001@localhost:5432/online_retail")

df = pd.read_sql("SELECT * FROM customer_features", engine)

X = df[['recency', 'frequency', 'avg_order_value', 'lifetime_days', 't']]

model = joblib.load("models/clv_xgboost_model.pkl")

df["predicted_clv"] = model.predict(X)

df.to_csv("D:/CLV suite/data/processed/customer_clv_predictions.csv",index=False)

print("CLV predictions generated successfully.")

print(df[["customer_id", "predicted_clv"]].head())