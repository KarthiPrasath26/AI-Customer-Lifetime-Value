import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Karthi_001@localhost:5432/online_retail")

df = pd.read_sql("SELECT * FROM customer_features", engine)

df["clv_score"] = df["frequency"] * df["avg_order_value"]

# Segment customers
df["segment"] = pd.qcut(
    df["clv_score"],
    q=4,
    labels=["Low Value", "Mid Value", "High Value", "VIP"]
)

# Segment counts
print(df["segment"].value_counts())

# Segment behavior
print(
    df.groupby("segment")[
        ["frequency", "avg_order_value", "monetary", "recency"]
    ].mean()
)

# Save results
df.to_csv(r"D:/CLV suite/data/processed/customer_segments.csv", index=False)
